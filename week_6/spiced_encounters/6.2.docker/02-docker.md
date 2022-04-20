# Docker

08/02/2022

## What is docker

* [Intro on Docker](https://www.infoworld.com/article/3204171/what-is-docker-the-spark-for-the-container-revolution.html) 
* Isolated container
* Lightweight VM ("without OS")    

## Idea

1. Run one app on one computer/server (several instances possible but not independent)
   Very expensive, many servers needed

2. Virtualization (VMware) (several independent instances per server)
   Resource allocation is expensive (better hardware needed)
   Several kernels, several OS

3. Containerization (Docker) (several independent container [instances] per server)

   Lightweight, portable, fast, **no hypervisor** needed

<img src="/home/jens/repos/DS_courses/week06/02_docker/virtualmachines-vs-containers-100727624-large.webp" alt="Docker" style="zoom: 50%;" /> 

## Ports

*   Port ranges from 0 - 65535 ($2^{16}-1$)

## Dockerfile

To set up your own images you can write a `Dockerfile` containing the definitions        

Example: 

```{docker}
# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]
```


## Commands

* Look for docker images by app name

```{shell}
docker search <app-name>
```

*   Check locally installed images

```{shell}
docker images
```

*   Check running docker container [instances]

```{shell}
docker ps
```

*   Control container
    *   `docker inspect <name>`  	- inspect container
    *   `docker exec -it <name> <command>`  	- run command, e.g. `/bin/bash`
    *   `docker restart <name>` 	- restart container    
    *   `docker stop <name>`     - stop container
    *   `docker kill <name>`   	- kill container

*   Run docker image 
    * `-d` 	- run in background 
    * `-it` 	- with terminal
    * `-p <host-port>:<container-port>` 	- publish (ports)
    * `-v <host-dir>:<container-dir>` 	- connect volume


```{shell}
docker run -d --name <name> -p <host-port>:<container-port> <image>:<version> 
```



## Software

* [Install Docker](https://docs.docker.com/engine/install/ubuntu/)

* [Docker and Amazon](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)

* [Video on Docker](https://www.youtube.com/watch?v=JSLpG_spOBM)

  

## Examples

1. Run a container and check functions
2. Python script flask
3. Python connected flask -> requests