# -*- coding: utf-8 -*-
#-------------LicenseHeader--------------
# plugin.video.Mediathek - Gives acces to the most video-platforms from german public service broadcaster
# Copyright (C) 2010  Raptor 2101 [raptor2101@gmx.de]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 
import re, time;
from mediathek import *
from xml.dom import minidom;
regex_dateString = re.compile("\\d{4}-\\d{2}-\\d{2}");
class WDRMediathek(Mediathek):
  def __init__(self, simpleXbmcGui):
    self.gui = simpleXbmcGui;
    self.rootLink = "http://www.wdr.de"
    self.menuTree = (
                      TreeNode("0","Neuste Videos",self.rootLink+"/mediathek/rdf/regional/index.xml",True),
                      TreeNode("1","Sendungen von A-Z","",False,
                        (
                          TreeNode("1.0","A40","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=A40",True),
                          TreeNode("1.1","Aktuelle Stunde","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Aktuelle+Stunde",True),
                          TreeNode("1.2","Am Sonntag","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+2+-+Der+Sonntag",True),
                          
                          TreeNode("1.3","Cosmo","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Funkhaus+Europa+-+Cosmo",True),
                          
                          TreeNode("1.4",u"daheim & unterwegs","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=daheim+%26+unterwegs",True),
                          TreeNode("1.5","die story","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=die+story",True),
                          TreeNode("1.6","Dittsche","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Dittsche",True),
                          
                          TreeNode("1.7","eins zu eins","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=eins+zu+eins",True),
                          
                          TreeNode("1.8","frauTV","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=frauTV",True),
                          
                          TreeNode("1.9","hier und heute","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Hier+und+Heute",True),
                          TreeNode("1.10","Kabarett","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+2+-+Kabarett",True),
                          
                          TreeNode("1.11","Lokalzeit aus Aachen","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+aus+Aachen",True),
                          TreeNode("1.12",u"Lokalzeit aus Düsseldorf","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+aus+D%FCsseldorf",True),
                          TreeNode("1.13","Lokalzeit OWL","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+OWL+aktuell",True),
                          TreeNode("1.14","Lokalzeit aus Bonn","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+aus+Bonn",True),
                          TreeNode("1.15","Lokalzeit aus Köln","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+aus+K%F6ln",True),
                          TreeNode("1.16","Lokalzeit Ruhr","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+Ruhr",True),
                          TreeNode("1.17","Lokalzeit aus Dortmund","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+aus+Dortmund",True),
                          TreeNode("1.18","Lokalzeit Bergisches Land","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+Bergisches+Land",True),
                          TreeNode("1.19","Lokalzeit Südwestfalen","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+S%FCdwestfalen",True),
                          TreeNode("1.20","Lokalzeit aus Duisburg","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+aus+Duisburg",True),
                          TreeNode("1.21","Lokalzeit Münsterland","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Lokalzeit+M%FCnsterland",True),
                          
                          TreeNode("1.22","markt","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=markt",True),
                          TreeNode("1.23","Menschen hautnah","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Menschen+hautnah",True),
                          TreeNode("1.24","Mittagsecho","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+5+-+Mittagsecho",True),
                          TreeNode("1.25","Mittagsmagazin","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+2+-+Mittagsmagazin",True),
                          TreeNode("1.26","mittwochs live","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=mittwochs+live",True),
                          TreeNode("1.27","Morgenecho","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+5+-+Morgenecho",True),
                          TreeNode("1.28","Morgenmagazin","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+2+-+Morgenmagazin",True),
                          TreeNode("1.29","Mosaik","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+3+-+Mosaik",True),
                          
                          TreeNode("1.30","Piazza","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Funkhaus+Europa+-+Piazza",True),
                          TreeNode("1.31","Platz der Republik","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+5+-+Platz+der+Republik",True),
                          
                          TreeNode("1.32","Quarks & Co","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Quarks+%26+Co",True),
                          
                          TreeNode("1.33","Resonanzen","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+3+-+Resonanzen",True),
                          
                          TreeNode("1.34","Scala","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+5+-+Scala",True),
                          TreeNode("1.35","schön hier","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=sch%F6n+hier",True),
                          TreeNode("1.36","Servicezeit","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Servicezeit",True),
                          TreeNode("1.37","sport inside","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=sport+inside",True),
                          TreeNode("1.38","Stichtag","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+2+-+Stichtag",True),
                          
                          
                          TreeNode("1.39","Thema NRW","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+5+-+Thema+NRW",True),
                          
                          
                          TreeNode("1.40","WDR aktuell","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+aktuell",True),
                          TreeNode("1.41","WDR sport aktuell","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+sport+aktuell",True),
                          TreeNode("1.42","west.art","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=West.art",True),
                          TreeNode("1.43","Westblick","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+5+-+Westblick",True),
                          TreeNode("1.44","WESTPOL","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WESTPOL",True),
                          TreeNode("1.45","Westzeit","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+2+-+Westzeit",True),
                          
                          TreeNode("1.46","Zeiglers wunderbare Welt des Fußballs","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Zeiglers+wunderbare+Welt+des+Fu%DFballs",True),
                          TreeNode("1.47","ZeitZeichen","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+3+%2F+WDR+5+-+ZeitZeichen",True),
                          TreeNode("1.48","Zimmer Frei!","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=Zimmer+Frei%21",True),
                          TreeNode("1.49","Zwischen Rhein und Weser","http://www.wdr.de/mediathek/html/regional/ergebnisse/sendung.xml?rankingtype=sendung&rankingvalue=WDR+2+-+Zwischen+Rhein+und+Weser",True),
                        )
                      ),
                      TreeNode("2","Themen","",False,
                        (
                          TreeNode("2.0","Politik","http://www.wdr.de/mediathek/html/regional/ergebnisse/schlagwort.xml?rankingvalue=Politik",True),
                          TreeNode("2.1","Wirtschaft","http://www.wdr.de/mediathek/html/regional/ergebnisse/schlagwort.xml?rankingvalue=Wirtschaft",True),
                          TreeNode("2.2","Kultur","http://www.wdr.de/mediathek/html/regional/ergebnisse/schlagwort.xml?rankingvalue=Kultur",True),
                          TreeNode("2.3","Panorama","http://www.wdr.de/mediathek/html/regional/ergebnisse/schlagwort.xml?rankingvalue=Panorama",True),
                          TreeNode("2.4","Service","http://www.wdr.de/mediathek/html/regional/ergebnisse/schlagwort.xml?rankingvalue=Service",True),
                          TreeNode("2.5","Freizeit","http://www.wdr.de/mediathek/html/regional/ergebnisse/schlagwort.xml?rankingvalue=Freizeit",True),
                          TreeNode("2.6","Sport","http://www.wdr.de/mediathek/html/regional/ergebnisse/schlagwort.xml?rankingvalue=Sport",True),
                        )
                      ),
                    )
                    
                    
    self._regex_extractTitle = re.compile("<title>.*?</title>");                
    self._regex_extractDescription = re.compile("<meta name=\"description\" content=\"(.|\\s)*?\" />");
    self._regex_extractPicture = re.compile("<link rel=\"image_src\" href=\".*?\" />");
    self._regex_extractDate = re.compile("<meta name=\"DC.Date\" content=\".*?\" />");
    
    self._regex_extractVideoPage = re.compile("<a href=\"/mediathek/html/.*?\\.xml\" title=\".*?\".*?>");
    self._regex_extractLink = re.compile("/mediathek/html/.*?\\.xml");
    
    
    self._regex_extractAudioLink = re.compile(self.rootLink+"/mediathek/.*?\\.mp3");
    self._regex_extractVideoLink = re.compile("dslSrc=rtmp://.*?\\.(mp4|flv)");
    
    self.replace_html = re.compile("<.*?>");
    self.replace_tag = re.compile("(<meta name=\".*?\" content=\"|<link rel=\"image_src\" href=\"|\" />)");
    
    
    
    
  @classmethod
  def name(self):
    return "WDR";
  def isSearchable(self):
    return False;
    
  def searchVideo(self, searchText):
    pass;
  
    
    
  def buildPageMenu(self, link, initCount, subLink = False):
    self.gui.log(link);
    mainPage = self.loadPage(link);
    
    if(mainPage.startswith("<?xml version=\"1.0\"")):
      self.parseXml(mainPage);
    else:
      self.parseHtml(mainPage);
  
  def parseHtml(self, htmlPage):
    videoPageLinks  = list(self._regex_extractVideoPage.finditer(htmlPage));
    
    for videoPageLink in videoPageLinks:
      link = self._regex_extractLink.search(videoPageLink.group()).group();
      print link;
      displayObject = self.generateDisplayObject(self.rootLink+link);
      self.gui.buildVideoLink(displayObject,self,len(videoPageLinks));
  
  def readText(self,node,textNode):
    try:
      node = node.getElementsByTagName(textNode)[0].firstChild;
      return unicode(node.data);
    except:
      return "";
  
  def parseDate(self,dateString):
    dateString = regex_dateString.search(dateString).group();
    return time.strptime(dateString,"%Y-%m-%d");
    
  def parseXml(self, xmlPage):
    xmlPage = minidom.parseString(xmlPage);  
    items = xmlPage.getElementsByTagName("item");
    for itemNode in items:
      link = self.readText(itemNode,"link");
      displayObject = self.generateDisplayObject(link);
      self.gui.buildVideoLink(displayObject,self,len(items));
      
  def generateDisplayObject(self,videoPageLink):
    mainPage = self.loadPage(videoPageLink);
    print mainPage
    title = unicode(self._regex_extractTitle.search(mainPage).group(),'ISO-8859-1');
    description = unicode(self._regex_extractDescription.search(mainPage).group(),'ISO-8859-1');
    picture = unicode(self._regex_extractPicture.search(mainPage).group(),'ISO-8859-1');
    date = self._regex_extractDate.search(mainPage).group();

    title =  self.replace_html.sub("", title);
    description = self.replace_tag.sub("",description);
    picture = self.replace_tag.sub("",picture);
    date = self.parseDate(self.replace_tag.sub("",date));
    
    link = self._regex_extractVideoLink.search(mainPage);
    if( link != None):
      link = link.group();
      link = link.replace("dslSrc=","");
    else:
      link = self._regex_extractAudioLink.search(mainPage).group();
     
    return DisplayObject(title,"",picture,description,{0:SimpleLink(link, 0)},True, date)
   
   