# Docker Workshop

This is the code for Tiket.com workshop for Docker in July 2023.

## Pre-requisite
1. Docker (of course)

## How-to
1. Clone this repository
2. To build the image: `docker build -t kubeflow-demo:v1.0.0 .` --> Please include the period "."
3. To instantiate the container from the image: `docker run kubeflow-demo:v1.0.0`

## Notes
1. You can't run this in Kubeflow since Kubeflow vscode/jupyter is just another container. You can't instantiate a container from container :)
2. Python version from base image would affect your package version. Please decide the versions carefully.
3. You don't need to do `docker stop` since our example here is not a server. It will exit automatically.
4. To see list of Docker images you have in your machine, you can run `docker images`
