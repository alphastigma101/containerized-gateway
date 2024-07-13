export $(grep -v '^#' .env | xargs)
cd app/
docker compose up -d --build
