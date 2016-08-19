import os

os.environ["PYWIKIBOT2_NO_USER_CONFIG"] = "1"

from pywikibot.data import api
from pywikibot.site import LoginStatus
import pywikibot

# allow login to the website the easy way, without user-config.py
# return True if the login was successfull, False otherwise
def login(family, lang, username, password, sysop=False, retry=True):
    site = pywikibot.Site(lang,'wikitolearn')

    site._loginStatus = LoginStatus.IN_PROGRESS
    if hasattr(site, "_userinfo"):
        del site._userinfo

    loginMan = api.LoginManager(site=site, sysop=sysop,
                         user=username, password=password)
    
    if loginMan.login(retry):
        site._username[sysop] = loginMan.username
        if hasattr(site, "_userinfo"):
            del site._userinfo
        site.getuserinfo()
        site._loginstatus = (LoginStatus.AS_SYSOP if sysop else LoginStatus.AS_USER)
        return True
    else:
        site._loginstatus = LoginStatus.NOT_LOGGED_IN
        return False

