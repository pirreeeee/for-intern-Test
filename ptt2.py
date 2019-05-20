import requests
from pyquery import PyQuery as pq

cookies = {"over18": "1"}
url = input('the url of the broad you want:')
pageNum = input('the amount of page:')

# https://www.ptt.cc/bbs/Gossiping/index.html
res = requests.get(url,
                  cookies = cookies)
mainPageDoc = pq(res.text)

# dateList = []
# authorList = []
# titleList = []
# contentList = []


for i in range(int(pageNum)):
    for each in mainPageDoc('#main-container div > div.title > a').items():
        mainPageDoc.make_links_absolute(base_url=res.url)
#         print(each.attr('href'))
        
#         print(each.text(), each.parent().siblings()('.meta>.author').text())
#         dateList.append(each.parent().siblings()('.meta>.date').text())
#         authorList.append(each.parent().siblings()('.meta>.author').text())
#         titleList.append(each.text())
        res_content = requests.get(each.attr('href'),
                      cookies = cookies)
        secPageDoc = pq(res_content.text)
        print(secPageDoc.text())
        

    res = requests.get(mainPageDoc('#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)').attr('href'),
                      cookies = cookies)
    mainPageDoc = pq(res.text)