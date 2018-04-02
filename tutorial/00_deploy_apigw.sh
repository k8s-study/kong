#!/bin/bash

echo "-- create kong-apigw namespace"
kubectl create -f k8s/kong-apigw/00_namespace__kong-apigw.yml

echo "-- create kong-apigw database"
kubectl create -f k8s/kong-apigw/01_service__kong-database.yml

echo "-- create kong database migration job"
sleep 5
kubectl create -f k8s/kong-apigw/02_job__kong-migration.yml

echo "-- deploy apigw services"
sleep 5
kubectl create -f k8s/kong-apigw/03_deploy__kong-apigw.yml
kubectl create -f k8s/kong-apigw/04_service__kong-apigw.yml
kubectl create -f k8s/kong-apigw/05_ingress__kong-apigw.yml
