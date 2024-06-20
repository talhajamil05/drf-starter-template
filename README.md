# DRF Starter Template

## Description

This repository provides a Django Rest Framework (DRF) starter template designed to speed up the development of RESTful APIs. It includes a simple implementation of SimpleJWT authentication and a health check endpoint. The template aims to provide a solid foundation for building scalable and secure API services with minimal setup. The repository also has a directory structure to support applications at scale.

### Key Features:
- **Simple JWT**: Secure your API endpoints with JWT based authentication. Integrated with `djangorestframework-simplejwt` for secure authentication.
- **Health Check Endpoint**: Easily monitor the health status of your API service.
- **Modular Structure**: Organized and clean project structure for maintainable code.
- **Ready to Use**: Pre-configured settings and dependencies to get you started quickly.
- **Postgresql configuration**: Pre-configured settings for postgresql to get up and running quickly.
- **Swagger UI**: Project configured with drf-yasg to provide swagger and redoc UI which can be used to test the API endpoints.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/talhajamil05/drf-starter-template.git
    cd drf-starter-template
    ```

2. **Create and activate a virtual environment using Python 3.10+:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Setup Database (Postgresql):**
    - Create a .env file
    - Copy the contents of .env.example in .env
    - Add the required keys/values in .env as per the Postgresql configuration
    
5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

### Running the Server

To start the development server, run:
```bash
python manage.py runserver
```

### Swagger Documentation

The API has drf-yasg integrated which provides a seamless swagger and redoc documentation to test the API endpoints. After the running the server, the swagger UI can be accessed at http://localhost:8000/swagger
