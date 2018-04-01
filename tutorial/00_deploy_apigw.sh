#!/bin/bash

echo "-- create kong-apigw namespace"
kubectl create -f k8s/kong-apigw/namespace_kong-apigw.yml

echo "-- create kong-apigw database"
kubectl create -f k8s/kong-apigw/svc_kong-database.yml

echo "-- create kong database migration job"
sleep 5
kubectl create -f k8s/kong-apigw/job_kong-migration.yml

echo "-- deploy apigw services"
sleep 5
kubectl create -f k8s/kong-apigw/deploy_kong-apigw.yml
kubectl create -f k8s/kong-apigw/svc_kong-apigw.yml
kubectl create -f k8s/kong-apigw/ingress_kong-apigw.yml
