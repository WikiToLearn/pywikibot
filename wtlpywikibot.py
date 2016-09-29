import os

os.environ["PYWIKIBOT2_NO_USER_CONFIG"] = "1"

from pywikibot.data import api
from pywikibot.site import LoginStatus
from pywikibot import textlib
import pywikibot
import requests
import urllib.parse as urlparse
import time

pywikibot.family.Family.load('wikitolearn')

# allow login to the website the easy way, without user-config.py
# return True if the login was successfull, False otherwise
def login(site, username, password, sysop=False, retry=True):
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

def get_category_status(site, page, cat):
    state = False
    old_text = page.text
    cats = textlib.getCategoryLinks(old_text)
    catpl = pywikibot.Category(site, cat)
    for c in cats:
        if c.title() == catpl.title():
            state = True
    return state

def set_category_status(site, page, cat, status):
    old_text = page.text
    cats = textlib.getCategoryLinks(old_text)
    catpl = pywikibot.Category(site, cat)

    if status:
        if catpl not in cats:
            cats.append(catpl)
    else:
        if catpl in cats:
            cats.remove(catpl)
    text = textlib.replaceCategoryLinks(page.text, cats, site=site)
    if old_text != text:
        page.text = text
        page.save(minor=True, botflag=True)
        return True
    return False


def checkPDFforPage(site,page_title,oldid=None,debug=False):
    result_bool = None
    result_text = None
    try:
        headers = {
            'User-Agent': 'PDF Check - WikiToLearn'
        }

        if oldid == None:
            page = pywikibot.Page(site,page_title)
            oldid = urlparse.parse_qs(urlparse.urlparse(page.permalink()).query)['oldid']
        args = {'title': 'Special:Book', 'oldid': oldid, 'bookcmd': 'render_article', 'returnto': page_title, 'arttitle': page_title, 'writer': 'rdf2latex'}
        url =  site.family.protocol(site.code) + "://" + site.family.hostname(site.code) + "/index.php?" + urlparse.urlencode(args)
        collection_id_request_with_redirects = requests.head(url, headers=headers, allow_redirects=True)

        collection_id_request = collection_id_request_with_redirects.history[len(collection_id_request_with_redirects.history)-1]

        collection_id_data = urlparse.parse_qs(urlparse.urlparse(collection_id_request.headers['Location']).query)

        if debug:
            print(collection_id_data)
        collection_id = collection_id_data['collection_id'][0]

        url_check = site.family.protocol(site.code) + "://" + site.family.hostname(site.code) + "/index.php?action=ajax&rs=wfAjaxGetMWServeStatus&rsargs%5B%5D=" + collection_id + "&rsargs%5B%5D=rdf2latex";

        checks = 0
        if debug:
            print("Checking PDF Generation Status")

        last_progress = None
        last_status = None
        count_last_progress_and_status = 0
        running = True
        while running:
            if debug:
                print("Requesting Status " + str(checks) + "...")
            r_checkStatus = requests.get(url_check, headers=headers)
            checks+=1

            status = r_checkStatus.json()[u"status"]

            if debug:
                print(status)
                print(count_last_progress_and_status)
            if status["progress"] == "100.00":
                result_bool = True
                result_text = "PDF OK"
                running = False
                if debug:
                    print("FINISH")
            elif count_last_progress_and_status >= 60 or "error" in status["status"].lower() or "died" in status["status"].lower():
                result_bool = False
                result_text = status['status']
                running = False
                if debug:
                    print("FAIL")
                    print(status)
            else:
                if status["status"] == last_status and status["progress"] == last_progress:
                    count_last_progress_and_status = count_last_progress_and_status + 1
                last_status = status["status"]
                last_progress = status["progress"]
                time.sleep(1)

    except requests.exceptions.RequestException as e:
        result_bool = False
        result_text = str(e)
    return result_bool,result_text
