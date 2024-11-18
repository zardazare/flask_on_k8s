# Monitoring setup - TBA

```bash
kubectl apply -f config/prometheus_config.yml
kubectl apply -f config/alert_rules_config.yml

kubectl apply -f prometheus_deployment.yml
kubectl apply -f grafana_deployment.yml
```
