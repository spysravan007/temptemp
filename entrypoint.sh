systemctl unmask docker
service docker start
cd /app
docker-compose up -d
