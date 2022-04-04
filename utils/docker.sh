#! /bin/sh

# docker base
# docker build -f ./utils/Dockerfile.base -t sexism-in-movies:base .
# docker run -ti sexism-in-movies:base /bin/bash

# docker build
docker build --no-cache -f ./utils/Dockerfile -t sexism-in-movies:latest .

# docker run
docker run -ti sexism-in-movies:latest /bin/bash

# kill all 
# docker rm -f $(docker ps -aq)