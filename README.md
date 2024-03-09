# Compliance Document Management API

This project is an API for managing compliance documents. It allows you to create, update, delete, and retrieve compliance documents in a structured and efficient manner.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installation

# Clone the repository

git clone https://github.com/ziebamikolaj/compliance-compass.git

# Navigate to the directory

cd compliance-compass

# Use Docker Compose to start the services

docker-compose build

docker-compose up -d

This command will start all the services defined in your `docker-compose.yml` file. Once the services are up and running, you can access the API at `http://localhost:8000` (or whatever port you have configured).

### Usage

To use the API, you can send HTTP requests to the endpoints defined in the API. Here are some examples:

#### Create a new compliance document

POST /documents

Request body:

{
"title": "Document Title",
"content": "Document content",
"category": "Category Name"
}

#### Get a compliance document

GET /documents/{id}

#### Update a compliance document

PUT /documents/{id}

Request body:

{
"title": "New Document Title",
"content": "New Document content",
"category": "New Category Name"
}

#### Delete a compliance document

DELETE /documents/{id}

Please refer to the API documentation for more detailed information about the request and response formats.
Once the API is running, you can use it to manage your compliance documents. Here are some example
