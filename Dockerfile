# start docker with 3.11
FROM python:3.11.6-slim-bullseye




#setup linux python
ENV PYTHONUNBUFFERED = 1



#update linux kernel && setuptools 
RUN apt-get update && apt-get -y install gcc libpq-dev


# folder project 
WORKDIR /app

#copy & install requirements
COPY requirements.txt /app/requirements.txt


#install requirements.txt
RUN pip install -r /app/requirements.txt

#copy project folder
COPY . /app/