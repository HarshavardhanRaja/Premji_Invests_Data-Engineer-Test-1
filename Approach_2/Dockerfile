# Use the official Airflow image as a base
FROM apache/airflow:latest

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow

# Install additional dependencies if needed
USER airflow
RUN pip install --upgrade pip
RUN pip install apache-airflow-providers-docker


# Copy the Airflow configuration file if you have any custom settings
COPY airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# Set the working directory
WORKDIR ${AIRFLOW_HOME}

# Initialize the database
RUN airflow db init

# Expose ports
EXPOSE 8080

# Run Airflow webserver and scheduler
CMD ["airflow", "webserver"]
