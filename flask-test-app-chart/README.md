# Develop

```bash
helm install flask-test-app-develop ./flask-test-app-chart -f ./flask-test-app-chart/values-develop.yaml --create-namespace
```

# Staging

```bash
helm install flask-test-app-staging ./flask-test-app-chart -f ./flask-test-app-chart/values-staging.yaml --create-namespace
```

# Production

```bash
helm install flask-test-app-production ./flask-test-app-chart -f ./flask-test-app-chart/values-production.yaml --create-namespace
```

# List helm releases

```bash
helm list -aq
```

# Unistall helm release

```bash
helm uninstall <release name>
```
