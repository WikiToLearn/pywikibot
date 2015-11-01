FROM debian:8

MAINTAINER wikitolearn sysadmin@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update && apt-get -y install zip unzip nano apt-utils curl rsync git && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete

RUN apt-get update && apt-get -y --force-yes install python && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete
RUN apt-get update && apt-get -y --force-yes install python-pip && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete
RUN apt-get update && apt-get -y --force-yes install python-dev && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete
RUN apt-get update && apt-get -y --force-yes install libffi-dev && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete
RUN apt-get update && apt-get -y --force-yes install libssl-dev && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete
RUN apt-get update && apt-get -y --force-yes install libffi-dev && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete
RUN apt-get update && apt-get -y --force-yes install libjpeg-dev && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete
RUN apt-get update && apt-get -y --force-yes install libmysqlclient-dev && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete

RUN git clone --recursive https://gerrit.wikimedia.org/r/pywikibot/core.git /pywikibot
WORKDIR /pywikibot

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install -r requirements.txt --allow-external pYsearch --allow-unverified pYsearch

CMD ["bash"]
