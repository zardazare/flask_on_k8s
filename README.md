# Flask with Gunicorn in Minikube

This is a simple setup for running a Flask application with Gunicorn on Minikube and Docker.

## Prerequisites

- [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed and running.
- [Docker](https://docs.docker.com/get-docker/) installed.

## Steps

1. **Build the Docker image**

    ```bash
    docker build -t flask_on_k8s:latest .
    ```
    * After building the image, add it to Minikube's cache so it’s available for deployment:

    ```bash
    minikube image load flask_on_k8s:latest 
    ``` 

    * You can verify that the image is loaded with this command:

    ```bash
    minikube image list
    ```

    *Note: Cached images will have the `docker.io/library/` prefix.*

2. **Deploy to Minikube**

    Apply the Kubernetes deployment and service:

    ```bash
    kubectl apply -f deployment.yml
    ```

    - **Hint:** Example for starting multiple nodes:
    
    ```bash
    minikube start --nodes 3 -p multinode-test
    ```

3. **Access the Application**

    Get the URL of the service:

    ```bash
    minikube service flask-test-app-service --url
    ```

    Open the URL in a browser or use curl to see the response.

4. **Cleanup**

    To delete the deployment and service, run:

    ```bash
    kubectl delete -f deployment.yml
    ```

## Run Without Kubernetes

If you’d like to run the Docker container independently (outside Kubernetes) for testing, you can run it on a different external port (e.g., `9000`).

### Run container

- **Detached mode**

    ```bash
    docker run -d -p 9000:5000 --name=flask_with_gunicorn_localhost flask_on_k8s:latest
    ```

- **Interactive mode**

    ```bash
    docker run -it -p 9000:5000 --name=flask_with_gunicorn_localhost flask_on_k8s:latest sh
    ```

## Useful commands

- **Execute commands in container/pod**

    ```bash
    kubectl exec -it <pod name> -- /bin/sh
    ```

- **Restart deployment**

    ```bash
    kubectl rollout restart deployment/flask-test-app-deployment
    ```

- **Logs from container in deployment**

    ```bash
    kubectl logs deployment/flask-test-app-deployment -c flask-test-app
    ```
