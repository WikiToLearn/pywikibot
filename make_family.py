#!/usr/bin/env python3
import sys
import os
import os.path

if len(sys.argv) != 2:
    print("You have to run this script using {} <path of wikitolearn>".format(sys.argv[0]))
    sys.exit(1)

pywikibot_repo_path=os.path.dirname(os.path.realpath(__file__))
wtl_repo_path = sys.argv[1]

pywikibot_wikitolearn_family_file = "{}/wikitolearn_family.py".format(pywikibot_repo_path)
wtl_databases_conf_file = "{}/databases.conf".format(wtl_repo_path)

if not os.path.isfile(pywikibot_wikitolearn_family_file):
    print("The file {} don't exists".format(pywikibot_wikitolearn_family_file))
    sys.exit(1)

if not os.path.isfile(wtl_databases_conf_file):
    print("The file {} don't exists".format(wtl_databases_conf_file))
    sys.exit(1)

databases = []
with open(wtl_databases_conf_file) as f:
    databases = f.readlines()
    f.close()
domains = [
    "wikitolearn.org",
    "developtest.wikitolearn-test.org",
    "local.wikitolearn-test.org",
    "broken-site.org",
]

domain_code = {
    "wikitolearn.org": "",
    "developtest.wikitolearn-test.org": "dev",
    "local.wikitolearn-test.org": "local",
    "broken-site.org": "test",
}

domain_to_ignore_certificate_error = {
    "wikitolearn.org": "False",
    "developtest.wikitolearn-test.org": "True",
    "local.wikitolearn-test.org": "True",
    "broken-site.org": "True",
}
langs = []

for database in databases:
    new_lang = database.strip().replace("wikitolearn","")
    if new_lang != "shared":
        langs.append(new_lang)

output = ""
output = output + "# -*- coding: utf-8 -*-" + "\n"
output = output + "# This file is auto-generated with the script make_family.py" + "\n"
output = output + "# if you find something wrong please fix the script" + "\n"
output = output + "# otherwise your edit will be overwritten" + "\n"
output = output + "#" + "\n"
output = output + "from pywikibot import family" + "\n"
output = output + "from pywikibot.tools import deprecated" + "\n"
output = output + "\n"
output = output + "class Family(family.Family):" + "\n"
output = output + "    def __init__(self):" + "\n"
output = output + "        family.Family.__init__(self)" + "\n"
output = output + "        self.name = 'wikitolearn'" + "\n"
output = output + "        self.langs = {" + "\n"
for domain in domains:
    for lang in langs:
        output = output + "            '{}': '{}',".format(domain_code[domain]+lang,lang+"."+domain) + "\n"
output = output + "        }" + "\n"
output = output + "\n"
output = output + "    def scriptpath(self, code):" + "\n"
output = output + "        return ''" + "\n"
output = output + "\n"
output = output + "    def ignore_certificate_error(self, code):" + "\n"
output = output + "        return {" + "\n"
for domain in domains:
    for lang in langs:
        output = output + "            '{}': {},".format(domain_code[domain]+lang,domain_to_ignore_certificate_error[domain]) + "\n"
output = output + "        }[code]" + "\n"
output = output + "\n"
output = output + "    @deprecated('APISite.version()')" + "\n"
output = output + "    def version(self, code):" + "\n"
output = output + "        return u'1.28.0'" + "\n"
output = output + "\n"
output = output + "    def protocol(self, code):" + "\n"
output = output + "        return u'https'" + "\n"

text_file = open(pywikibot_wikitolearn_family_file, "w")
text_file.write(output)
text_file.close()
