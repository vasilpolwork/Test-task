#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Define directories and server naming
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVER_NAME="test-runner-$(date +%s)"

# Export variables for envsubst
export REPO_URL="https://github.com/${GITHUB_REPOSITORY}"

echo "🚀 Fetching GitHub Runner registration token..."
export REG_TOKEN=$(curl -s -X POST -H "Authorization: token ${GH_PAT}" \
  "https://api.github.com/repos/${GITHUB_REPOSITORY}/actions/runners/registration-token" | jq -r .token)

if [ "$REG_TOKEN" == "null" ]; then
  echo "❌ Error: Failed to fetch registration token. Check GH_PAT permissions."
  exit 1
fi

echo "🚀 Preparing cloud-config with dynamic secrets..."
# Substitute variables in the template
envsubst < "$SCRIPT_DIR/cloud-config.yaml" > "$SCRIPT_DIR/cloud-config.tmp.yaml"

echo "🚀 Creating ephemeral CX23 machine in Hetzner Cloud (nbg1)..."
hcloud server create \
  --name "$SERVER_NAME" \
  --type cx23 \
  --image ubuntu-24.04 \
  --location nbg1 \
  --label "scope=ephemeral-test" \
  --user-data-from-file "$SCRIPT_DIR/cloud-config.tmp.yaml"

# Clean up temporary sensitive file
rm "$SCRIPT_DIR/cloud-config.tmp.yaml"

echo "✅ Server $SERVER_NAME created successfully. Provisioning takes ~2 minutes."