#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Server name with a timestamp to ensure uniqueness across runs
SERVER_NAME="test-runner-$(date +%s)"

echo "🚀 Creating ephemeral machine in Hetzner Cloud..."

# Execute server creation via hcloud CLI
hcloud server create \
  --name "$SERVER_NAME" \
  --type cx21 \
  --image ubuntu-24.04 \
  --location nbg1 \
  --label "scope=ephemeral-test" \
  --user-data-from-file infra/cloud-config.yaml

echo "✅ Server $SERVER_NAME successfully created and is now being provisioned."