#!/bin/bash
set -e

SERVER_NAME="test-runner-$(date +%s)"

echo "🚀 Creating ephemeral machine in Hetzner Cloud..."

hcloud server create \
  --name "$SERVER_NAME" \
  --type cx23 \
  --image ubuntu-24.04 \
  --location nbg1 \
  --label "scope=ephemeral-test" \
  --user-data-from-file infra/cloud-config.yaml

echo "✅ Server $SERVER_NAME successfully created."