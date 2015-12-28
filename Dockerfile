FROM python:3.4

MAINTAINER wikitolearn sysadmin@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN pip install --target=/pywikibot/ pywikibot==2.0rc3 
ADD ./wikitolearn_family.py /pywikibot/pywikibot/families/

CMD ["bash"]
