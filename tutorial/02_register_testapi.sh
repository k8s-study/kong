#!/bin/bash

testapi_spec=$(kubectl get svc/test-api -o json)
echo '-- testapi k8s spec'
echo $testapi_spec | jq

upstream_url=$(
  kubectl get svc/test-api -o json | \
  jq -r '.spec.clusterIP + ":" + (.spec.ports[0].port|tostring)'
)
echo '-- testapi upstream url'
echo $upstream_url

api_create_payload='{
  "name": "testapi",
  "uris": "/hello",
  "methods": "GET",
  "upstream_url": "http://'$upstream_url'"
}'
echo '-- apigw create api payload'
echo $api_create_payload | jq

echo '-- request to apigw'
cd kong-cli
inv api-create -d "$(echo $api_create_payload | sed -e 's/\n//g')" | jq

echo '-- get api list'
inv api-list | jq

apigw_host=$(
  kubectl get ing -n kong-apigw -o json | \
  jq -r '.items[0].spec.rules[0].host')

echo '-- check new apigw endpoint'
cmd="curl $apigw_host/hello"
echo $cmd
${cmd}

echo
echo '-- done'
