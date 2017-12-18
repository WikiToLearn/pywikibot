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
            'devit': 'it.developtest.wikitolearn-test.org',
            'deven': 'en.developtest.wikitolearn-test.org',
            'devde': 'de.developtest.wikitolearn-test.org',
            'deves': 'es.developtest.wikitolearn-test.org',
            'devfr': 'fr.developtest.wikitolearn-test.org',
            'devpt': 'pt.developtest.wikitolearn-test.org',
            'devsv': 'sv.developtest.wikitolearn-test.org',
            'devca': 'ca.developtest.wikitolearn-test.org',
            'devmeta': 'meta.developtest.wikitolearn-test.org',
            'devpool': 'pool.developtest.wikitolearn-test.org',
            'localit': 'it.local.wikitolearn-test.org',
            'localen': 'en.local.wikitolearn-test.org',
            'localde': 'de.local.wikitolearn-test.org',
            'locales': 'es.local.wikitolearn-test.org',
            'localfr': 'fr.local.wikitolearn-test.org',
            'localpt': 'pt.local.wikitolearn-test.org',
            'localsv': 'sv.local.wikitolearn-test.org',
            'localca': 'ca.local.wikitolearn-test.org',
            'localmeta': 'meta.local.wikitolearn-test.org',
            'localpool': 'pool.local.wikitolearn-test.org',
            'testit': 'it.broken-site.org',
            'testen': 'en.broken-site.org',
            'testde': 'de.broken-site.org',
            'testes': 'es.broken-site.org',
            'testfr': 'fr.broken-site.org',
            'testpt': 'pt.broken-site.org',
            'testsv': 'sv.broken-site.org',
            'testca': 'ca.broken-site.org',
            'testmeta': 'meta.broken-site.org',
            'testpool': 'pool.broken-site.org',
        }

    def scriptpath(self, code):
        return ''

    def ignore_certificate_error(self, code):
        return {
            'it': False,
            'en': False,
            'de': False,
            'es': False,
            'fr': False,
            'pt': False,
            'sv': False,
            'ca': False,
            'meta': False,
            'pool': False,
            'devit': True,
            'deven': True,
            'devde': True,
            'deves': True,
            'devfr': True,
            'devpt': True,
            'devsv': True,
            'devca': True,
            'devmeta': True,
            'devpool': True,
            'localit': True,
            'localen': True,
            'localde': True,
            'locales': True,
            'localfr': True,
            'localpt': True,
            'localsv': True,
            'localca': True,
            'localmeta': True,
            'localpool': True,
            'testit': True,
            'testen': True,
            'testde': True,
            'testes': True,
            'testfr': True,
            'testpt': True,
            'testsv': True,
            'testca': True,
            'testmeta': True,
            'testpool': True,
        }[code]

    @deprecated('APISite.version()')
    def version(self, code):
        return u'1.28.0'

    def protocol(self, code):
        return u'https'
