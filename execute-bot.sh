#!/bin/bash
export W2L_INSTANCE_NAME="w2l-dev"

docker run  --rm -e PYTHONPATH="/pywikibot" -e PYWIKIBOT2_DIR="/pywikibot/configs"  -ti --name pywikibot --hostname pywikibot \
 --link ${W2L_INSTANCE_NAME}-websrv:www.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:pool.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:meta.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:it.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:en.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:de.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:es.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:fr.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:pt.wikitolearn.org \
 --link ${W2L_INSTANCE_NAME}-websrv:sv.wikitolearn.org \
-v $(pwd)/configs/:/pywikibot/configs/ wikitolearn/pywikibot

