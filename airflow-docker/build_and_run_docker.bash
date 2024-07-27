# Build the Docker image
docker-compose build


# Initialize the Airflow database
docker-compose up airflow-init

# Start the Airflow services
docker-compose up -d
