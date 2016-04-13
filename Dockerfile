FROM python:3.4

MAINTAINER wikitolearn sysadmin@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN pip install --target=/w2lbot/ pywikibot==2.0rc4
ADD ./wikitolearn_family.py /w2lbot/pywikibot/families/

CMD ["bash"]
