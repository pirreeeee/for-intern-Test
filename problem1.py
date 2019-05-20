urlList = []
while True:
    urls = input('please type in the url, type 1 to stop')
    if urls == '1':
        break
    else:
        urlList.append(urls)

def findTop3(urlList):
    filenameList = []
    for each in urlList:
        split1 = each.split('/')

        
        filenameList.append(split1[-1])
        uniFilename = set(filenameList)

    resultDict = {}
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in uniFilename:

        count = 0
        for each in filenameList:
            if each == i:
                count = count + 1
        resultDict[i] = count
    
    L = sorted(resultDict.items(),key=lambda item:item[1],reverse=True)

    L = L[:3]
    dictdata = {}
    for l in L:
        dictdata[l[0]] = l[1]
 
    


    for key, value in dictdata.items():
        print(key, value)
findTop3(urlList)