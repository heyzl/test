import urllib
import re,os


def getImages(myurl): 
    imgSum = 0
    badImg = 0
    urlStr = urllib.urlopen(myurl).read()
    hrefCmp = re.compile("""<img.*?src="(.*?)".*?>""")
    hreflist = hrefCmp.findall(urlStr)
    drive = "F:\\抓图"
    if not os.path.exists(drive):
        os.mkdir(drive)
    for href in hreflist:
        if href.find("""http://""")==0:
            imageName = href[href.rindex("/")+1:]
            try:
                urllib.urlretrieve(href, os.path.join(drive,imageName))
                imgSum += 1
                print imageName + "    OK"
            except:
                print "cannot download this image:"+imageName
        else:
            badImg += 1
            print href
    print "Sucess:", imgSum, "    Failed:", badImg
if __name__=="__main__":
    imgurl =raw_input("url ->")
    getImages(imgurl)
    
