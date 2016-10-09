# -*- coding: utf-8 -*-
# This file is auto-generated with the script make_family.py
# if you find something wrong please fix the script
# otherwise your edit will be overwritten
#
from pywikibot import family
from pywikibot.tools import deprecated

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikitolearn'
        self.langs = {
            'it': 'it.wikitolearn.org',
            'en': 'en.wikitolearn.org',
            'de': 'de.wikitolearn.org',
            'es': 'es.wikitolearn.org',
            'fr': 'fr.wikitolearn.org',
            'pt': 'pt.wikitolearn.org',
            'sv': 'sv.wikitolearn.org',
            'ca': 'ca.wikitolearn.org',
            'meta': 'meta.wikitolearn.org',
            'pool': 'pool.wikitolearn.org',
            'devit': 'it.wikitolearn.vodka',
            'deven': 'en.wikitolearn.vodka',
            'devde': 'de.wikitolearn.vodka',
            'deves': 'es.wikitolearn.vodka',
            'devfr': 'fr.wikitolearn.vodka',
            'devpt': 'pt.wikitolearn.vodka',
            'devsv': 'sv.wikitolearn.vodka',
            'devca': 'ca.wikitolearn.vodka',
            'devmeta': 'meta.wikitolearn.vodka',
            'devpool': 'pool.wikitolearn.vodka',
            'testit': 'it.tuttorotto.org',
            'testen': 'en.tuttorotto.org',
            'testde': 'de.tuttorotto.org',
            'testes': 'es.tuttorotto.org',
            'testfr': 'fr.tuttorotto.org',
            'testpt': 'pt.tuttorotto.org',
            'testsv': 'sv.tuttorotto.org',
            'testca': 'ca.tuttorotto.org',
            'testmeta': 'meta.tuttorotto.org',
            'testpool': 'pool.tuttorotto.org',
            'localit': 'it.tuttorotto.biz',
            'localen': 'en.tuttorotto.biz',
            'localde': 'de.tuttorotto.biz',
            'locales': 'es.tuttorotto.biz',
            'localfr': 'fr.tuttorotto.biz',
            'localpt': 'pt.tuttorotto.biz',
            'localsv': 'sv.tuttorotto.biz',
            'localca': 'ca.tuttorotto.biz',
            'localmeta': 'meta.tuttorotto.biz',
            'localpool': 'pool.tuttorotto.biz',
        }

    def scriptpath(self, code):
        return ''

    @deprecated('APISite.version()')
    def version(self, code):
        return u'1.27.0'

    def protocol(self, code):
        return {
            'it': u'https',
            'en': u'https',
            'de': u'https',
            'es': u'https',
            'fr': u'https',
            'pt': u'https',
            'sv': u'https',
            'ca': u'https',
            'meta': u'https',
            'pool': u'https',
            'devit': u'http',
            'deven': u'http',
            'devde': u'http',
            'deves': u'http',
            'devfr': u'http',
            'devpt': u'http',
            'devsv': u'http',
            'devca': u'http',
            'devmeta': u'http',
            'devpool': u'http',
            'testit': u'http',
            'testen': u'http',
            'testde': u'http',
            'testes': u'http',
            'testfr': u'http',
            'testpt': u'http',
            'testsv': u'http',
            'testca': u'http',
            'testmeta': u'http',
            'testpool': u'http',
            'localit': u'http',
            'localen': u'http',
            'localde': u'http',
            'locales': u'http',
            'localfr': u'http',
            'localpt': u'http',
            'localsv': u'http',
            'localca': u'http',
            'localmeta': u'http',
            'localpool': u'http',
        }[code]
