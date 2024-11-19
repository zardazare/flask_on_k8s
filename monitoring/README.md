# Monitoring Setup

This folder contains all the necessary files and instructions to set up monitoring for the project, including Prometheus and Grafana configurations.

## Prerequisites

Ensure the following tools are installed:
- Docker
- kubectl
- Kubernetes cluster (minikube for testing)

## Deployment Instructions

*Run the following commands from the `project_root/monitoring/` folder.*

To deploy monitoring tools (Prometheus and Grafana), follow these steps:

1. Apply the Prometheus configuration:

    ```bash
    kubectl apply -f config/prometheus_config.yml
    ```

2. Apply alert rules configuration:

    ```bash
    kubectl apply -f config/alert_rules_config.yml
    ```

3. Deploy Prometheus:

    ```bash
    kubectl apply -f prometheus_deployment.yml
    ```

    *Note: Use DaemonSet if you deploy node-level monitoring agents (e.g., Node Exporter) that need to run on every node.*

4. Deploy Grafana:

    ```bash
    kubectl apply -f grafana_deployment.yaml
    ```

## Accessing the Tools

To test the tools locally, you can use port-forwarding to expose the services on your localhost.

1. Prometheus: Run the following command to forward Prometheus to http://localhost:9090:

    ```bash
    kubectl port-forward svc/prometheus-service 9090:9090
    ```

2. Grafana: Run the following command to forward Grafana to http://localhost:3000 (default credentials: admin/admin):

    ```bash
    kubectl port-forward svc/grafana-service 3000:3000
    ```
    
## Simplified Deployment

To simplify deployment everything can be combined into one YAML file (Prometheus, Grafana, and alert rules) and applied with a single command, e.g.

```bash
kubectl apply -f monitoring.yml
```

*monitoring.yml not created in project at this point*

If you prefer to keep YAML files separate, a shell script can simplify the process.

```bash
chmod +x deploy_monitoring.sh

./deploy_monitoring.sh
```
