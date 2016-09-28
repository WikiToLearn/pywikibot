FROM wikitolearn/python35:0.1
ADD ./sources.list /etc/apt/sources.list

MAINTAINER wikitolearn sysadmin@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN pip3 install pywikibot==2.0rc4
ADD ./wikitolearn_family.py /usr/local/lib/python3.5/site-packages/pywikibot/families/
ADD ./wtlpywikibot.py /opt/

WORKDIR /opt/
CMD ["bash"]
