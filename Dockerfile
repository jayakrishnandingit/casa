# Use an official Python runtime as a parent image
FROM python:3.7

# Set environment varibles for build.
ENV PYTHONUNBUFFERED 1
# ENV DJANGO_ENV prod
ENV DJANGO_ENV dev
ENV DJANGO_SETTINGS_MODULE casa.settings.$DJANGO_ENV
ENV AWS_STORAGE_BUCKET_NAME casa-$DJANGO_ENV-files

RUN apt-get clean \
    && apt-get update -y \
    && apt-get install -y software-properties-common \
    && apt-get update -y \
    && add-apt-repository ppa:maxmind/ppa \
    && apt-get install -y \
        libmaxminddb-dev \
        libmaxminddb0 \
        libpq-dev \
        mmdb-bin \
        libtiff5-dev \
        libjpeg62-turbo-dev \
        libopenjp2-7-dev \
        zlib1g-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libwebp-dev \
        tcl8.6-dev \
        tk8.6-dev

# upgrade pip to the latest version.
RUN pip install --upgrade pip
# install gunicorn WSGI server.
RUN pip install gunicorn

# Set the working directory to /code/
WORKDIR /code/

COPY requirements requirements/
# Install required python packages.
RUN pip install -r requirements/$DJANGO_ENV.txt

ADD GeoLite2-City_20190716.tar.gz geodata/
ADD GeoLite2-Country_20190716.tar.gz geodata/

# Copy the current directory contents into the container at /code/
COPY manage.py .
COPY activity activity/
COPY start.sh .
COPY casa casa/
COPY home home/

RUN useradd jay
RUN chown -R jay /code
USER jay

EXPOSE 8000
CMD ["sh", "start.sh"]
