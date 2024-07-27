docker build -t my-airflow-image .

docker run -d -p 8081:8080 --name my-airflow-container my-airflow-image
