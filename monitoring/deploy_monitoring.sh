#!/bin/bash

# Navigate to the monitoring folder

echo "Applying Prometheus ConfigMap..."
kubectl apply -f config/prometheus_config.yml

echo "Applying Alert Rules ConfigMap..."
kubectl apply -f config/alert_rules_config.yml

echo "Deploying Prometheus..."
kubectl apply -f prometheus_deployment.yml

echo "Deploying Grafana..."
kubectl apply -f grafana_deployment.yml

echo "Monitoring setup completed!"
