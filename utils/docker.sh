#! /bin/sh

# docker base
# docker build -f ./utils/Dockerfile.base -t sexism-in-movies:base .
# docker run -ti sexism-in-movies:base /bin/bash

# docker build
docker build --no-cache -f ./utils/Dockerfile -t aga-ml:latest .

# docker run
docker run -ti aga-ml:latest /bin/bash


# kill all 
docker rm -f $(docker ps -aq)