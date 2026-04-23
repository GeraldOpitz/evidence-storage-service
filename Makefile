.PHONY: install run test build up down swarm-deploy swarm-down clean

# Install dependencies
install:
	pip install .

# Run API locally
run:
	uvicorn app.main:app --reload

# Run tests
test:
	pytest

# Build docker image
build:
	docker build -t evidence-service .

# Docker compose up
up:
	docker-compose up --build

# Docker compose down
down:
	docker-compose down

# Swarm deploy
swarm-deploy:
	docker swarm init || true
	docker build -t evidence-service:latest .
	docker stack deploy -c docker-stack.yml evidence-stack

# Swarm remove
swarm-down:
	docker stack rm evidence-stack

# Clean environment
clean:
	docker system prune -f
