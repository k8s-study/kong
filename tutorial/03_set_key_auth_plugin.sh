#!/bin/bash

# check available plugins 
inv node-information | jq .plugins.available_on_server

# enable plugin
curl -XPOST apigw-admin.pong.com/apis/testapi/plugins --data "name=key-auth"
# {"created_at":1522588319000,"config":{"key_in_body":false,"run_on_preflight":true,"anonymous":"","hide_credentials":false,"key_names":["apikey"]},"id":"1cfb7097-f928-40a1-8af0-38b60b10488a","name":"key-auth","api_id":"2aa6408d-0201-4ab9-aad7-e937cce66295","enabled":true}

# create consumer
inv consumer-create -d '{"username":"testuser"}'

# create apikey for consumer
curl -XPOST apigw-admin.pong.com/consumers/testuser/key-auth -d ''

# {"id":"5fb06363-ef77-4d2c-b6fe-7699e84284a2","created_at":1522588493000,"key":"ORVIslQ6SmcsKABMicUxRSDEOpihnWrT","consumer_id":"3702e361-3e27-47a7-85b8-2135669cf554"}

# test request to endpoint with apikey
curl apigw.pong.com/hello -H 'apikey: ORVIslQ6SmcsKABMicUxRSDEOpihnWrT'
