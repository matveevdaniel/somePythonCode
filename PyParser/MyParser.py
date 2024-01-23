import requests
from bs4 import BeautifulSoup

def parseWebToHtml():
    url = "https://davinagaz.by/" 
    accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
    headers = {"Accept":accept,"User-Agent": user_agent}
    
    req = requests.get(url, headers = headers)         # с асептом и агентом 
    #req = requests.get(url)
                                                        #req.encoding = "utf-8-sig"
    src = req.text

    
    with open("c:/Users/Danik/pythonProjects/PyParser/index.html","w",encoding="utf-8-sig") as file:        #надо  раскоментить
        file.write(src)



def parseOfflineHtml():

    with open("c:/Users/Danik/pythonProjects/PyParser/index.html",encoding="utf-8-sig") as file:
         src_read = file.read()

    soup = BeautifulSoup(src_read,'lxml')
    all_subnav_item = soup.find_all(class_= "_subnav__item_cgju7_1")


    all_subnav_item_dict = {}


    for count, item in enumerate(all_subnav_item):           #for item in all_subnav_item
        item_text = item.text
        
        print(item)
        item_href = "_subnav__item_cgju7_1" + item.get("href")
    
        all_subnav_item_dict[count] = item_href
   
    #print(all_subnav_item_dict)
    
    
   
#for item in all_subnav_item_dict:
#    print(all_subnav_item)

    


 
 
#print(soup.text)

# for el in soup.select(".items > .article-summary"):
#     title = el.select('.caption > a')
#     print(title[0].text)

#name = soup.find("article", class_="_card_6bcao_1 _card--autoheight-mobile_6bcao_474")
#print(name)

def main():
   parseWebToHtml()
   #parseOfflineHtml()
    
if __name__ == '__main__':
    main()