FROM python:3.4
ADD ./sources.list /etc/apt/sources.list

MAINTAINER wikitolearn sysadmin@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN pip install --target=/opt/ pywikibot==2.0rc4
ADD ./wikitolearn_family.py /opt/pywikibot/families/
ADD ./user-config.py /opt/

WORKDIR /opt/
CMD ["bash"]
