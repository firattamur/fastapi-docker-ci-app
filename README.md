# Dockerize a FastAPI App

🚀 Introduction
---------------
This project demonstrates how to dockerize a simple application, push it to Docker Hub, and automatically update the Docker image using CI/CD with GitHub Actions upon merging changes into the main branch. 

- The application is a simple Python FastAPI app that displays a random quote from the [Forismatic API](https://forismatic.com/en/api/).

- The Docker image is hosted on Docker Hub [here](https://hub.docker.com/r/ftamur/fastapi-docker-ci-app).

📝 Goals: 
--------------------
- [x] 📝 Write a simple Python FastAPI app.
- [x] 📦 Dockerize the application.
- [x] 🚢 Push the Docker image to Docker Hub.
- [ ] 🤖 Automate the process of updating the Docker image using CI/CD with GitHub Actions.

🔧 Technology Stack
-------------------
- Application Framework: 
    - Python 3.9
    - FastAPI
- Containerization: 
    - Docker
- CI/CD: 
    - GitHub Actions

🔨 Steps to Build the Docker Image
-----------------------
Detailed steps to build the Docker image and run it locally.

- Create a Dockerfile with the following content:
    ```dockerfile
    FROM python:3.9

    WORKDIR /app

    COPY app/ ./app
    COPY start.sh ./
    COPY requirements.txt ./

    RUN pip install -r requirements.txt

    EXPOSE 8000

    CMD ["bash", "start.sh"]
    ```

- Run the following command to build the Docker image:
    ```bash
    docker build -t yourname/fastapi-docker-ci-app:version_number .
    ```

- Run the following command to run the Docker container:
    ```bash
    docker run -d -p 8000:8000 yourname/fastapi-docker-ci-app:version_number
    ```

    - -d means detached mode, which runs the container in the background.
    - -p 8000:8000 means map port 8000 of the host to port 8000 of the container.

- Open your browser and go to `http://localhost:8000/` to see the app running.

🔨 Steps to Push the Docker Image to Docker Hub

- Create a Docker Hub account [here](https://hub.docker.com/).

- Create a repository on Docker Hub.

- Run the following command to tag the Docker image:
    ```bash
    docker tag yourname/fastapi-docker-ci-app:version_number yourdockerhubusername/fastapi-docker-ci-app:version_number
    ```

- Run the following command to push the Docker image to Docker Hub:
    ```bash
    docker push yourdockerhubusername/fastapi-docker-ci-app:version_number
    ```

🔨 Steps to Automate the Process of Updating the Docker Image Using CI/CD with GitHub Actions

📜 License
----------
This project is licensed under the terms of the MIT license.