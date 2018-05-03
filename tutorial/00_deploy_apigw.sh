#!/bin/bash

echo "-- create kong-apigw database"
kubectl create -f k8s/kong-apigw/00_service__kong-database.yml

echo "-- create kong database migration job"
sleep 5
kubectl create -f k8s/kong-apigw/01_job__kong-migration.yml

echo "-- deploy apigw services"
sleep 5
kubectl create -f k8s/kong-apigw/02_deployment__kong-apigw.yml
kubectl create -f k8s/kong-apigw/03_service__kong-apigw.yml
kubectl create -f k8s/kong-apigw/04_ingress__kong-apigw.yml
