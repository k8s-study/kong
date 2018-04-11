#!/bin/bash

echo "-- build testapi on minikube"
eval $(minikube docker-env)
docker-compose build
unset DOCKER_TLS_VERIFY DOCKER_HOST DOCKER_CERT_PATH DOCKER_API_VERSION

echo "-- deploy testapi"
kubectl create -f k8s/default

