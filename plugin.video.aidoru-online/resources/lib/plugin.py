# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# noinspection PyUnresolvedReferences
from codequick import Route, Resolver, Listitem, utils, run
from codequick.utils import urljoin_partial, bold
import requests
import urlquick
import xbmcgui
import resolveurl
from bs4 import BeautifulSoup as bs
import logger #logger.debug(FUNCION O VARIABLE A DEBUGUEAR)
import xbmc
import os
from time import sleep as wait
import random
from random import uniform
import xbmcaddon
import xbmcvfs
import tools
import urllib


username = tools.getSetting("username")
password = tools.getSetting("password")

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

characters = letras + numeros

cookie = []

for i in range(32):
    caracter_random = random.choice(characters)
    cookie.append(caracter_random)

    ufp = "".join(cookie)

cookie = [str(r) for r in cookie] #Para quitar las u'
cookie = ''.join(cookie) #Para concatenar todos los elementos de la lista con un separador que elijamos entre comillas    
cookies = 'flog=6; ufp='+ str(cookie)
# logger.debug(cookies)

URL = "https://aidoru-online.me/"
url_constructor = urljoin_partial(URL)
a_moment = uniform(2, 10)

s = requests.session()

HEADERS = {
    'authority': 'aidoru-online.me',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://aidoru-online.me',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://aidoru-online.me/login.php',
    'accept-language': 'es-419,es;q=0.9,en;q=0.8',
    'cookie': cookies,
}

params = (
    ('type', 'login'),
)

data = {
  'username': username,
  'password': password,
  'do': 'login',
  'language': 'en'
}
url = url_constructor("login.php?type=login")
response = s.post(url, headers=HEADERS, data=data)


@Route.register
def root(plugin, content_type="segment"):
    item = Listitem()
    item.label = "Please first enter your Username and Password in the addon settings. If you already did, ignore this message"
    yield item
    
    yield Listitem.search(search_Content)
    
    item = Listitem()
    item.label = "Show All"
    pcat_url = url_constructor("get_ttable.php?pcat=ShowAll&typ=both")
    item.set_callback(sub_Categories, pcat_url=pcat_url)
    yield item
    
    item = Listitem()
    item.label = "48g"
    pcat_url = url_constructor("get_ttable.php?pcat=48G&typ=both")
    item.set_callback(sub_Categories, pcat_url=pcat_url)
    yield item
    
    item = Listitem()
    item.label = "H!P"
    pcat_url = url_constructor("get_ttable.php?pcat=H!P&typ=both")
    item.set_callback(sub_Categories, pcat_url=pcat_url)
    yield item
    
    item = Listitem()
    item.label = "Stardust"
    pcat_url = url_constructor("get_ttable.php?pcat=Stardust&typ=both")
    item.set_callback(sub_Categories, pcat_url=pcat_url)
    yield item
        
        
    item = Listitem()
    item.label = "Other"
    pcat_url = url_constructor("get_ttable.php?pcat=Other&typ=both") 
    item.set_callback(sub_Categories, pcat_url=pcat_url)
    yield item
        
        
@Route.register
def sub_Categories(plugin, pcat_url):
     
    item = Listitem()    
    item.label = "BD/DVDISO"
    scat_url = url_constructor(pcat_url + "&scat=1")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()      
    item.label = "BD/DVD-RIP"
    scat_url = url_constructor(pcat_url + "&scat=2")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "TV"
    scat_url = url_constructor(pcat_url + "&scat=3")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "Performance/Concerts"
    scat_url = url_constructor(pcat_url + "&scat=4")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "MV/PV(Music Videos)"
    scat_url = url_constructor(pcat_url + "&scat=5")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "Webstream"
    scat_url = url_constructor(pcat_url + "&scat=6")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "Image"
    scat_url = url_constructor(pcat_url + "&scat=7")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "Audio"
    scat_url = url_constructor(pcat_url + "&scat=8")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "Album"
    scat_url = url_constructor(pcat_url + "&scat=9")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "Single"
    scat_url = url_constructor(pcat_url + "&scat=10")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "Radio"
    scat_url = url_constructor(pcat_url + "&scat=11")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()  
    item.label = "Misc"
    scat_url = url_constructor(pcat_url + "&scat=12")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()
    item.label = "Subtitled"
    scat_url = url_constructor(pcat_url + "&subbed=1")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()
    item.label = "Freeleech"
    scat_url = url_constructor(pcat_url + "&fl=1")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item
    
    item = Listitem()
    item.label = "Resurrected"
    scat_url = url_constructor(pcat_url + "&resd=1")
    item.set_callback(all_Content, scat_url=scat_url)
    yield item


@Route.register
def all_Content(plugin, scat_url):
    _url = url_constructor(scat_url)
    resp = bs(s.get(_url).text, 'html.parser')
    wait(a_moment)
    root_Content = resp.find_all(class_="t-row")
     
    for elem in root_Content:
        item = Listitem()
        elem_router = elem.find("td", valign="middle")
        item.label = elem_router.find_next_sibling("td").find("a").get("title")
        url = url_constructor(elem_router.find_next_sibling("td").find("a").get("href"))
        img = bs(s.get(url).text, 'html.parser')
        fanarts = img.find_all(class_="image-link")
        thumbnails = img.find_all(class_="torrent-image")
        
        for art in fanarts:
            img_link = art.get("src").replace('640x480q90', '4032x3024q90').replace('/th/','/img/')
            item.art['fanart'] = img_link
        for thumb in thumbnails:
            img_link = thumb.get("data-imgurl").replace('640x480q90', '4032x3024q90')
            item.art['thumb'] = img_link
        item.set_callback(details_Content, url=url)
        yield item 
        
        
    NextPageTree = resp.find_all("p", align="center")
    for page in NextPageTree:
        nextPageP = page.find_all("a", class_="page-link")[-1].get("data-pagenum")
        yield Listitem.next_page(nextPage=url_constructor(_url+"&p="+nextPageP),callback=get_Content)
        
        
@Route.register
def get_Content(plugin,nextPage):
    _url = url_constructor(nextPage)
    resp = bs(s.get(_url).text, 'html.parser')
    wait(a_moment)
    root_Content = resp.find_all(class_="t-row")
     
    for elem in root_Content:
        item = Listitem()
        elem_router = elem.find("td", valign="middle")
        item.label = elem_router.find_next_sibling("td").find("a").get("title")
        url = url_constructor(elem_router.find_next_sibling("td").find("a").get("href"))
        img = bs(s.get(url).text, 'html.parser')
        fanarts = img.find_all(class_="image-link")
        thumbnails = img.find_all(class_="torrent-image")
        
        for art in fanarts:
            img_link = art.get("src").replace('640x480q90', '4032x3024q90').replace('/th/','/img/')
            item.art['fanart'] = img_link
        for thumb in thumbnails:
            img_link = thumb.get("data-imgurl").replace('640x480q90', '4032x3024q90')
            item.art['thumb'] = img_link
        item.set_callback(details_Content, url=url)
        yield item  
        
        
    NextPageTree = resp.find_all("p", align="center")
    for page in NextPageTree:
        nextPageP = page.find_all("a", class_="page-link")[-1].get("data-pagenum")
        yield Listitem.next_page(nextPage=url_constructor(_url+"&p="+nextPageP),callback=get_Content)


@Route.register
def search_Content(plugin, search_query):
    url = url_constructor("get_ttable.php?pcat=ShowAll&typ=both&searchstr={}&deadlive=1".format(search_query))
    return all_Content(plugin, url)


@Route.register
def details_Content(plugin,url):
    url = s.get(url_constructor(url))
    resp = bs(url.text, 'html.parser')
    covers = resp.find_all(class_="image-link")
    images = resp.find_all(class_="torrent-image")
    wait(a_moment)
    
    item = Listitem()
    item.label = "STREAM|PLAY"
    url_router = resp.find(id="ty-button")
    url = url_constructor(url_router.find_previous_sibling("div").find("a").get("href"))
    item.set_callback(play_Torrent, url=url)
    yield item
    
    counter = 1
    for cover in covers:
        item = Listitem()
        item.label = "COVER" + str(counter)
        img_link = cover.get("src").replace('640x480q90', '4032x3024q90').replace('/th/','/img/')
        url = img_link
        # logger.debug(url)
        item.art['thumb'] = img_link
        item.art['fanart'] = img_link
        item.set_callback(show_Photos, url=url)
        counter += 1
        yield item
        
    counter = 1
    for image in images:
        item = Listitem()
        item.label = "IMAGE" + str(counter)
        img_link = image.get("data-imgurl").replace('640x480q90', '4032x3024q90')
        url = img_link
        # logger.debug(url)
        item.art['thumb'] = img_link
        item.art['fanart'] = img_link
        item.set_callback(show_Photos, url=url)
        counter += 1
        yield item
    
    
@Route.register
def play_Torrent(plugin,url):
    url_ = url_constructor(url)
    url = s.get(url_)
    video = ""
    torrent_title = url.headers.get("Content-Disposition").split('filename=')[1].replace('"','').replace(' ','')
    logger.debug(str(torrent_title))
    
    profile = xbmc.translatePath("special://userdata/addon_data/plugin.video.laboratory/").decode("utf-8") #Cambiarlo a xbmcvfs.translatePath
    directory = "temp\\"
    parent_dir = profile
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
        logger.debug("Directory '%s' created" %directory)
    except OSError as error:
        logger.debug(error)
    
    torrent = open(profile+directory+torrent_title, 'wb')
    torrent.write(url.content)
    torrent.close()
    torrent_file = profile+directory+torrent_title
    logger.debug(torrent_file)
    
    if tools.getSetting("torrent_player") == "Torrentin":
        xbmc.executebuiltin('Dialog.Close(all,true)')
        xbmc.executebuiltin( "PlayMedia("+"plugin://plugin.video.torrentin/?uri=%s" % "file://"+( urllib.quote_plus(torrent_file, safe='') )+")" )
        
    elif tools.getSetting("torrent_player") == "Elementum":
        xbmc.executebuiltin('Dialog.Close(all,true)')
        xbmc.executebuiltin( "PlayMedia("+"plugin://plugin.video.elementum/play?uri=%s" % ( urllib.quote_plus(torrent_file, safe='') )+")" )
         
    elif tools.getSetting("torrent_player") == "Torrest":
        xbmc.executebuiltin('Dialog.Close(all,true)')
        xbmc.executebuiltin( "PlayMedia("+"plugin://plugin.video.torrest/play_path?path=%s" % ( urllib.quote_plus(torrent_file, safe='') )+")" )
    
    item = Listitem()
    item.label = "Enjoy Your Video! =)"
    yield item
       

    
@Resolver.register
def show_Photos(plugin,url):
    url = url
    xbmc.executebuiltin("ShowPicture(" + url +")")
    plugin = plugin.extract_source(url)
    return Listitem().from_dict(**{
        "label" : "Showing",
        "callback" : plugin,
    })   