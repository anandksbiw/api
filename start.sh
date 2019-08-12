#!/bin/bash
docker build -t  app .
docker run   -p 56733:80 app
