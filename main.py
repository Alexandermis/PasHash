import sys
import hashlib
import webbrowser

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def getUrl():

    return "https://www.spotify.com/"
#     # Update. Better way to open Firefox in debugging mode (defaults to port 6000):
#
# #firefox.exe --start-debugger-server --profile C:\FirefoxTEMP
#     #Connect to a existing firefox with –connect-existing and –marionette-port
#     driver.get("https://www.youtube.com/watch?v=9ye7srmAnMU")
#     print(driver.currenturl)
#     return "https://studmail.htw-aalen.de/login.php"
def startVal(a,b):
    if ((len(a) + len(b)) % 2 == 0):
        return a+b
    else:
        return b+a

def salt(a):
    hash=calc_hash_list()
    a=superHash(a[::-1])
    return a[0:64]

def order(a):
    x=0
    for c in a:
        x += ord(c)
    return x

def calc_hash_list():
    hash = []
    m1 = hashlib.sha256()
    m2 = hashlib.sha3_512()
    m3 = hashlib.sha3_384()
    m4 = hashlib.sha3_256()
    m5 = hashlib.blake2b()
    m6 = hashlib.blake2s()
    m7 = hashlib.md5()
    hash.append(m1), hash.append(m2), hash.append(m3), hash.append(m4), hash.append(m5), hash.append(m6), hash.append(m7)
    return  hash

def superHash(startval):
    hash = calc_hash_list()
    while (len(hash) != 0):
        x = order(startval)
        hash[x % len(hash)].update(startval.encode())
        startval = hash[x % len(hash)].hexdigest()
        hash.remove(hash[x % len(hash)])
    return startval
if __name__ == '__main__':
    if len(sys.argv)!= 2:
        exit(-1)
    else:
        url=getUrl()
        startval = startVal(url, sys.argv[1])
        startval=superHash(startval)
        if len(startval)==64:
            startval+=salt(startval)
        print(f"Password.len: {len(startval)} Password: {startval}")