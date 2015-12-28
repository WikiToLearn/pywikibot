FROM python:3.4

MAINTAINER wikitolearn sysadmin@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN git clone --recursive https://gerrit.wikimedia.org/r/pywikibot/core.git /pywikibot
WORKDIR /pywikibot

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install -r requirements.txt --allow-external pYsearch --allow-unverified pYsearch

CMD ["bash"]
