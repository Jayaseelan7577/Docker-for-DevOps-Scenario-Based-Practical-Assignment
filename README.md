# Docker for DevOps – Scenario-Based Practical Assignment

## Overview

This repository contains the practical implementation and documentation for six Docker and DevOps scenarios.

## Scenarios Covered

1. Container Crash in Staging
2. Legacy Python Application
3. Docker Compose – Node.js + MySQL
4. Data Persistence with MySQL
5. Production Rollback with Docker Swarm
6. Docker in CI Pipeline

## Scenario 1 – Container Crash in Staging

### Tasks Completed

- Diagnosed a restarting container.
- Inspected container state and restart history.
- Reviewed container logs.
- Identified and corrected the missing DB_HOST environment variable.
- Simulated and resolved a host port 8080 conflict.

The application crash was simulated using a lightweight Docker container because the original application image was not provided.

## Scenario 2 – Legacy Python Application

Directory: scenario-2-legacy-python/

### Tasks Completed

- Created a Python Flask application.
- Created an optimized Dockerfile using python:3.11-slim.
- Demonstrated Docker layer caching.
- Compared optimized and legacy-style Docker image sizes.
- Ran the application using APP_ENV=staging.

The optimized image was approximately 222 MB, while the legacy-style image was approximately 1.62 GB.

## Scenario 3 – Docker Compose

Directory: scenario-3-docker-compose/

### Services

- Node.js Orders API
- MySQL 8.0

### Tasks Completed

- Environment variables
- Named volume
- Custom network
- MySQL healthcheck
- Service dependency using health status
- Orders API health endpoint
- Scaled Orders API to 3 replicas
- Service-specific logs
- Combined logs

## Scenario 4 – Data Persistence

Directory: scenario-4-data-persistence/

### Tasks Completed

- Explained container filesystem data loss.
- Created and used a named MySQL volume.
- Accessed MySQL CLI.
- Copied schema.sql into the container.
- Created the ordersdb database and orders table.
- Verified the database schema.

## Scenario 5 – Production Rollback

### Tasks Completed

- Initialized Docker Swarm.
- Created versioned demo images 1.9 and 2.0.
- Created a Swarm service using version 2.0.
- Performed a Docker Swarm rollback.
- Verified version 1.9 became the active version.
- Documented immutable image versioning.

The rollback demonstration used locally tagged Nginx images to simulate versioned coffee-api releases because the original production images were not provided.

## Scenario 6 – Docker in CI Pipeline

Directory: scenario-6-ci-pipeline/

### Pipeline Stages

Checkout → Build & Test → Docker Build → Vulnerability Scan → Docker Hub Push

### Security

- Jenkins credentials are referenced instead of hard-coded Docker Hub credentials.
- Docker login uses --password-stdin.
- Trivy scans the Docker image for HIGH and CRITICAL vulnerabilities before push.

The local image scan identified HIGH severity vulnerabilities in the current base image dependencies. Therefore, the configured pipeline would block the Docker Hub push when the vulnerability gate fails.

The Jenkinsfile is a CI/CD pipeline configuration template. Jenkins, Docker Hub credentials, and an actual Docker Hub push were not configured during this practical session.

## Technologies Used

- Docker
- Docker Compose
- Docker Swarm
- Jenkins
- Docker Hub
- Trivy
- Python
- Flask
- Node.js
- Express
- MySQL
- Linux / Ubuntu

## Repository Structure

```text
.
├── README.md
├── scenario-2-legacy-python
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── Dockerfile.large
├── scenario-3-docker-compose
│   ├── docker-compose.yml
│   └── orders-api
│       ├── Dockerfile
│       ├── package.json
│       └── server.js
├── scenario-4-data-persistence
│   └── schema.sql
└── scenario-6-ci-pipeline
    ├── Dockerfile
    ├── Jenkinsfile
    └── index.html# Docker for DevOps – Scenario-Based Practical Assignment

## Overview

This repository contains the practical implementation and documentation for six Docker and DevOps scenarios.

## Scenarios Covered

1. Container Crash in Staging
2. Legacy Python Application
3. Docker Compose – Node.js + MySQL
4. Data Persistence with MySQL
5. Production Rollback with Docker Swarm
6. Docker in CI Pipeline

## Scenario 1 – Container Crash in Staging

### Tasks Completed

- Diagnosed a restarting container.
- Inspected container state and restart history.
- Reviewed container logs.
- Identified and corrected the missing DB_HOST environment variable.
- Simulated and resolved a host port 8080 conflict.

The application crash was simulated using a lightweight Docker container because the original application image was not provided.

## Scenario 2 – Legacy Python Application

Directory: scenario-2-legacy-python/

### Tasks Completed

- Created a Python Flask application.
- Created an optimized Dockerfile using python:3.11-slim.
- Demonstrated Docker layer caching.
- Compared optimized and legacy-style Docker image sizes.
- Ran the application using APP_ENV=staging.

The optimized image was approximately 222 MB, while the legacy-style image was approximately 1.62 GB.

## Scenario 3 – Docker Compose

Directory: scenario-3-docker-compose/

### Services

- Node.js Orders API
- MySQL 8.0

### Tasks Completed

- Environment variables
- Named volume
- Custom network
- MySQL healthcheck
- Service dependency using health status
- Orders API health endpoint
- Scaled Orders API to 3 replicas
- Service-specific logs
- Combined logs

## Scenario 4 – Data Persistence

Directory: scenario-4-data-persistence/

### Tasks Completed

- Explained container filesystem data loss.
- Created and used a named MySQL volume.
- Accessed MySQL CLI.
- Copied schema.sql into the container.
- Created the ordersdb database and orders table.
- Verified the database schema.

## Scenario 5 – Production Rollback

### Tasks Completed

- Initialized Docker Swarm.
- Created versioned demo images 1.9 and 2.0.
- Created a Swarm service using version 2.0.
- Performed a Docker Swarm rollback.
- Verified version 1.9 became the active version.
- Documented immutable image versioning.

The rollback demonstration used locally tagged Nginx images to simulate versioned coffee-api releases because the original production images were not provided.

## Scenario 6 – Docker in CI Pipeline

Directory: scenario-6-ci-pipeline/

### Pipeline Stages

Checkout → Build & Test → Docker Build → Vulnerability Scan → Docker Hub Push

### Security

- Jenkins credentials are referenced instead of hard-coded Docker Hub credentials.
- Docker login uses --password-stdin.
- Trivy scans the Docker image for HIGH and CRITICAL vulnerabilities before push.

The local image scan identified HIGH severity vulnerabilities in the current base image dependencies. Therefore, the configured pipeline would block the Docker Hub push when the vulnerability gate fails.

The Jenkinsfile is a CI/CD pipeline configuration template. Jenkins, Docker Hub credentials, and an actual Docker Hub push were not configured during this practical session.

## Technologies Used

- Docker
- Docker Compose
- Docker Swarm
- Jenkins
- Docker Hub
- Trivy
- Python
- Flask
- Node.js
- Express
- MySQL
- Linux / Ubuntu

## Repository Structure

```text
.
├── README.md
├── scenario-2-legacy-python
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── Dockerfile.large
├── scenario-3-docker-compose
│   ├── docker-compose.yml
│   └── orders-api
│       ├── Dockerfile
│       ├── package.json
│       └── server.js
├── scenario-4-data-persistence
│   └── schema.sql
└── scenario-6-ci-pipeline
    ├── Dockerfile
    ├── Jenkinsfile
    └── index.html
