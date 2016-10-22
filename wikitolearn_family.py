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

    def ignore_certificate_error(self, code):
        return {
            'it': 'False',
            'en': 'False',
            'de': 'False',
            'es': 'False',
            'fr': 'False',
            'pt': 'False',
            'sv': 'False',
            'ca': 'False',
            'meta': 'False',
            'pool': 'False',
            'devit': 'True',
            'deven': 'True',
            'devde': 'True',
            'deves': 'True',
            'devfr': 'True',
            'devpt': 'True',
            'devsv': 'True',
            'devca': 'True',
            'devmeta': 'True',
            'devpool': 'True',
            'testit': 'True',
            'testen': 'True',
            'testde': 'True',
            'testes': 'True',
            'testfr': 'True',
            'testpt': 'True',
            'testsv': 'True',
            'testca': 'True',
            'testmeta': 'True',
            'testpool': 'True',
            'localit': 'True',
            'localen': 'True',
            'localde': 'True',
            'locales': 'True',
            'localfr': 'True',
            'localpt': 'True',
            'localsv': 'True',
            'localca': 'True',
            'localmeta': 'True',
            'localpool': 'True',
        }[code]

    @deprecated('APISite.version()')
    def version(self, code):
        return u'1.27.0'

    def protocol(self, code):
        return u'https'
