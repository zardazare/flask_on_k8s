FROM python:3.13.0-alpine

WORKDIR /var/app
# Expose the port on which the Flask app will run
EXPOSE 5000

# Copy Pipfile and Pipfile.lock first for caching
COPY Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade --no-cache-dir pip pipenv && \
    pipenv install --deploy

COPY . .

# Run the app with Gunicorn WSGI
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

# Run the app without WSGI
# CMD ["python", "app.py"]
