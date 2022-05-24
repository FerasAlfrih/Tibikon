import xml.etree.ElementTree as etree
from bs4 import BeautifulSoup


class Bible(object):
    """docstring for Bible"""

    def __init__(self, nm, chp, ver):
        self.nm = nm
        self.chp = chp
        self.ver = ver
        self.text = self.finder()

    def finder(self):
        soup = BeautifulSoup(
            open('static/files/arbible.xml', encoding='utf8'), "lxml")
        bks = soup.findAll("b")
        names = [bn['id'] for bn in bks]
        name = [n for n in names if n == self.nm]
        text = "Not Found"
        for book in bks:
            if book['id'] == name[0]:
                chapters = book.findAll('c')
                cap = [cp['n'] for cp in chapters]
                chapter = [n for n in cap if n == str(self.chp)]
                for capt in chapters:
                    if capt['n'] == chapter[0]:
                        verss = capt.findAll('v')
                        v = [vr['n'] for vr in verss]
                        vers = [n for n in v if n == str(self.ver)]
                        text = vers[0] + verss[int(vers[0])-1].text
        return text
