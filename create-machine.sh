#!/bin/bash


FLY_API_HOSTNAME="https://api.machines.dev"
APP="ta-ion"
if [ -z "$FLY_ACCESS_TOKEN" ]; then
    echo "There's no FLY_ACCESS_TOKEN"
    exit 1
fi

curl -i -X POST \
  -H "Authorization: Bearer ${FLY_ACCESS_TOKEN}" -H "Content-Type: application/json" \
  "${FLY_API_HOSTNAME}/v1/apps/${APP}/machines" \
  -d @machine.json
