#/bin/bash
docker rm fitness
docker pull migsking/fitness:latest
docker run -p 5000:5000 --name fitness migsking/fitness:latest