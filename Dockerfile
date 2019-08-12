FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

 RUN export http_proxy=http://10.159.0.3:8678 && \
     export https_proxy=http://10.159.0.3:8678 && \
     pip install Flask
