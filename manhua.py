import urllib.request,os
import re
from bs4 import BeautifulSoup
def get_each_comic_url(url):
    
    page = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})

    html=urllib.request.urlopen(page).read()
    soup = BeautifulSoup(html,"html.parser")
    body = soup.find_all(class_="preview-row")
    reg = r'src="(http://[^>]+\.(?:jpeg|jpg))"'
    urlre = re.compile(reg)
    url_comcis = re.findall(urlre,str(body))
    return url_comcis

def get_url_list(http):
    page = urllib.request.urlopen(http)
    html = page.read()
    soup = BeautifulSoup(html,"html.parser")
    body = soup.find_all(class_="preview-row")
    reg = r'href="\w*\.html"'
    urlre = re.compile(reg)
    urlist = re.findall(urlre,str(body))
    return urlist

'''

'''
os.mkdir('gouis')
os.chdir(os.path.join(os.getcwd(), 'gouis'))
'''
for li in urlist:   
    url = 
    try:
        url_com = get_each_comic_url(url)[0]
        urllib.request.urlretrieve(url_com, str(i)+'.jpg')
        print("Success to download")
    except:
        print('get_error')

    i+=1

'''
i = 0
url_comcis = get_each_comic_url()
for coms in url_comcis:
    #print(coms)
    
    #try:
    '''
    page = urllib.request.Request(coms ,headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(page)
    f = open('sjkg','wb')
    f.write(response.read())
    f.close()
    print("Success to download")

    #except:
        #print('get_error')
    '''
    try:
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(coms, str(i)+'.jpg') 
        print("Success to download")
    except:
        print('get_error')
    i+=1

