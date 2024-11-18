from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route("/")

def hello():
    return jsonify({"Message": "Hello from Flask with gunicorn WSGI"})

# If you want additional metrics (e.g., for specific endpoints):
@app.route('/endpoint')
@metrics.counter('endpoint_counter', 'Count of requests to /endpoint')
def endpoint():
    return "Endpoint!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
