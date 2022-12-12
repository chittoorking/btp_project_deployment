# BTP Deployment

- First, using the Flask a simple Web Application was made.
- Used Docker to run the project.
```bash
docker build -t <name> . # This is the command to build the docker image from the Dockerfile.
docker run -d -p 5000:5000 <name> # To run the application in docker container.
```
