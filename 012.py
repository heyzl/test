import urllib
import re,os


def getImages(myurl): #定义抓取网页图片的函数
    imgSum = 0
    #初始化抓取的图片的总数
    badImg = 0
    #初始化不能抓取的图片的总数
    urlStr = urllib.urlopen(myurl).read()
    #读取myurl的内容
    hrefCmp = re.compile("""<img.*?src="(.*?)".*?>""")
    #将括号里的正则表达式编译成正则表达式对象，便于重复利用
    hreflist = hrefCmp.findall(urlStr)
    #findall函数返回正则表达式在字符串中所有匹配结果的列表，即有关图片的结果
    drive = "F:\\抓图"
    #初始化抓取的图片所保存的具体地址



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
    
