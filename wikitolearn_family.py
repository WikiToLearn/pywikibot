# -*- coding: utf-8 -*-
from pywikibot import family
from pywikibot.tools import deprecated

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'wikitolearn'
        self.langs = {
            'it': 'it.wikitolearn.org',
            'en': 'en.wikitolearn.org',
            'meta': 'meta.wikitolearn.org',
            'pool': 'pool.wikitolearn.org',
            'devit': 'it.wikitolearn.vodka',
            'deven': 'en.wikitolearn.vodka',
            'devmeta': 'meta.wikitolearn.vodka',
            'devpool': 'pool.wikitolearn.vodka',
            'localit': 'it.tuttorotto.biz',
            'localen': 'en.tuttorotto.biz',
            'localpool': 'pool.tuttorotto.biz',
            'testit' : 'it.tuttorotto.org',
            'testen' : 'en.tuttorotto.org',
            'testpool' : 'pool.tuttorotto.org'
        }

    def scriptpath(self, code):
        return {
            'it': '',
            'en': '',
            'meta': '',
            'pool': '',
            'devit': '',
            'deven': '',
            'devmeta': '',
            'devpool': '',
            'localit': '',
            'localen': '',
            'localpool': '',
            'testit': '',
            'testen': '',
            'testpool': '',
        }[code]

    @deprecated('APISite.version()')
    def version(self, code):
        return {
            'it': u'1.27.0',
            'en': u'1.27.0',
            'meta': u'1.27.0',
            'pool': u'1.27.0',
            'devit': u'1.27.0',
            'deven': u'1.27.0',
            'devmeta': u'1.27.0',
            'devpool': u'1.27.0',
            'localit': u'1.27.0',
            'localen': u'1.27.0',
            'localpool': u'1.27.0',
            'testit': u'1.27.0',
            'testen': u'1.27.0',
            'testpool': u'1.27.0'

        }[code]

    def protocol(self, code):
        return {
            'it': u'http',
            'en': u'http',
            'meta': u'http',
            'pool': u'http',
            'devit': u'http',
            'deven': u'http',
            'devmeta': u'http',
            'devpool': u'http',
            'localit': u'http',
            'localen': u'http',
            'localpool': u'http',
            'testit': u'http',
            'testen': u'http',
            'testpool': u'http',
        }[code]
