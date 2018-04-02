#!/bin/bash

API_NAME=testapi
API_CONSUMER=testuser

cd kong-cli
echo -- check available plugins 
inv node-information | jq .plugins.available_on_server

echo -- enable plugin
curl -XPOST apigw-admin.pong.com/apis/$API_NAME/plugins --data "name=key-auth" | jq

echo -- create consumer
payload='{"username":"'$API_CONSUMER'"}'
inv consumer-create -d "$(echo -e $payload)" | jq

echo -- create apikey for consumer
curl -XPOST apigw-admin.pong.com/consumers/$API_CONSUMER/key-auth -d '' | jq
# {"id":"5fb06363-ef77-4d2c-b6fe-7699e84284a2","created_at":1522588493000,"key":"ORVIslQ6SmcsKABMicUxRSDEOpihnWrT","consumer_id":"3702e361-3e27-47a7-85b8-2135669cf554"}

sleep 3
echo -- test request to endpoint with apikey
api_key=$(curl apigw-admin.pong.com/consumers/$API_CONSUMER/key-auth | jq -r .data[0].key)
headers="apikey:$api_key"
curl apigw.pong.com/hello -H $headers 

echo
echo -- done
