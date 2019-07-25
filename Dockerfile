# Use an official Python runtime as a parent image
FROM python:3.7

# Set environment varibles for build.
ENV PYTHONUNBUFFERED 1

RUN apt-get clean \
    && apt-get update -y \
    && apt-get install -y software-properties-common \
    && apt-get update -y \
    && add-apt-repository ppa:maxmind/ppa \
    && apt-get install -y \
        libmaxminddb-dev \
        libmaxminddb0 \
        libpq-dev \
        mmdb-bin

# Set the working directory to /code/
WORKDIR /code/

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

ADD GeoLite2-City_20190716.tar.gz geodata/
ADD GeoLite2-Country_20190716.tar.gz geodata/

# Copy the current directory contents into the container at /code/
COPY manage.py .
COPY casa casa/
COPY home home/
COPY activity activity/

RUN useradd jay
RUN chown -R jay /code
USER jay

EXPOSE 8000
CMD exec gunicorn casa.wsgi:application --bind 0.0.0.0:8000 --workers 3
