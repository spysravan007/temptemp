FROM ubuntu:16.04
RUN apt update && apt install -y docker.io docker-compose
WORKDIR /app
COPY kanban-board /app
COPY entrypoint.sh /app
ENTRYPOINT ["/app/entrypoint.sh"]
EXPOSE 4200 80 8080 5432

