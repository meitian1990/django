import urllib.request
import re
url = "http://www.highpin.cn/job/b30615.html"
def getnowresult(url):
    result = urllib.request.urlopen(url).read().decode("utf-8")
    title = re.search("<title>(.*?)</title>",result).group(1)
    description = re.search('<meta name="description" content="(.*?)" />',result).group(1)
    keywords = re.search('<meta name="keywords" content="(.*?)" />',result).group(1)
    nowresult={"title":title,"description":description,"keywords":keywords}
##    print("title:{0[title]}\ndescription:{0[description]}\nkeywords:{0[keywords]}".format(nowresult))
    return nowresult
def getexpectresult(url):
    result = urllib.request.urlopen(url).read().decode("utf-8")
    workpalce = re.search("class='byecity-event-a'>(.*?)</a>",result).group(1)
    postitonName = re.search('class="postitonName" title="(.*?)"',result).group(1)
    salary = re.search("target='_blank' class='byecity-event-a'>(.*?)</a>",result).group(1)
    expecttitle = "【"+workpalce+postitonName+"招聘】最新"+workpalce+postitonName+"招聘信息_工资待遇_岗位职责_年薪"+salary+" - 智联卓聘"
    expectdescription = "【"+workpalce+postitonName+"招聘】由智联卓聘网为您提供最新年薪"+salary+"的"+workpalce+postitonName+"招聘信息大全,包括"+workpalce+postitonName+"招聘岗位要求,工资待遇,岗位职责等信息."
    expectkeywords = postitonName+","+postitonName+"招聘,"+postitonName+"招聘信息"
    expectresult={"expecttitle":expecttitle,"expectdescription":expectdescription,"expectkeywords":expectkeywords}
##    print("title:{0[expecttitle]}\ndescription:{0[expectdescription]}\nkeywords:{0[expectkeywords]}".format(expectresult))
    return expectresult
def compare(now,expect):
    try:
        assert(now["title"]==expect["expecttitle"])
    except AssertionError:
        print("Title结果错误！\n实际结果：{0}\n期望结果：{1}".format(now["title"],expect["expecttitle"]))
    else:
        print("Title结果正确~")
    try:
        assert(now["description"]==expect["expectdescription"])
    except AssertionError:
        print("Description结果错误！\n实际结果：{0}\n期望结果：{1}".format(now["description"],expect["expectdescription"]))
    else:
        print("Description结果正确~")
    try:
        assert(now["keywords"]==expect["expectkeywords"])
    except AssertionError:
        print("Keywords结果错误！\n实际结果：{0}\n期望结果：{1}".format(now["keywords"],expect["expectkeywords"])
    else:
        print("Keywords结果正确~")

now = getnowresult(url)
expect = getexpectresult(url)
compare(now,expect)
