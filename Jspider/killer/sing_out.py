from django.http import JsonResponse,HttpResponse
import pprint
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, render, redirect
import requests
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent
def pick_charset(html):
    """
    从文本中提取 meta charset
    :param html:
    :return:
    """
    charset = None
    m = re.compile('<meta .*(http-equiv="?Content-Type"?.*)?charset="?([a-zA-Z0-9_-]+)"?', re.I).search(html)
    if m and m.lastindex == 2:
        charset = m.group(2).lower()
    return charset

def decomposeScript(soup):
    body = soup.find("body")
    list_a=soup.find_all("a")
    list_form=soup.find_all("form")
    list_iframe=soup.find_all("iframe")
    body_children = body.children
    for i in body_children:
        if i.name == "script":
            i.decompose()
    for j in list_a:
        if j.name=="a":
            # print(j)
            j['href']="####"
            j['onclick']="return false;"
    for form in list_form:
        form['action']=""
    for iframe in list_iframe:
        iframe['src']=""
    head = soup.head
    body = soup.body
    newtag = soup.new_tag("script", src="https://code.jquery.com/jquery-3.1.1.min.js")
    newtagtest = soup.new_tag("script", type="text/javascript")
    newtagtest.string = '$(document).click(function(e) {var txt=$(e.target).text();var tagName = $(e.target).prop("nodeName");var parent_tagName=$(e.target).parent().prop("nodeName");var grandpa_tagName=$(e.target).parent().parent().prop("nodeName");alert(tagName);$.ajax({url:"test1",type:"post",data:{"tagName":tagName,"tagText":txt,"parent_tagName":parent_tagName,"grandpa_tagName":grandpa_tagName,},success:function(data){parent.$("#contentId").val(data); alert(data)}})})'
    body.append(newtagtest)
    head.append(newtag)
    return soup.prettify()

def writeHtml(file,html_text):
    f = open(file, "w", encoding="utf-8")
    f.writelines(html_text)
    f.close()
def test(request):
    urlToOperate = request.POST.get('urlToOperate')
    pprint.pprint(urlToOperate)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    html=requests.get(urlToOperate,headers=header)
    html.encoding=pick_charset(html.text)
    html_text=html.text
    soup=BeautifulSoup(html_text,"html.parser")
    writeHtml("template/killer/welcometest.html", soup.prettify())
    html_text = decomposeScript(soup)
    writeHtml("template/killer/mytest.html",html_text)
    # return HttpResponse('<IFRAME src="./mytest.html" id="jf_id" name="operate_iframe" style="width: 1020px;height: 1000px;" scrolling="no"></IFRAME>')
    return HttpResponse('./mytest.html')
# 登录处理
def signin(request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')
    pprint.pprint("fuck")
    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)

    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'

                return redirect('operate.html')
            else:
                return JsonResponse({'ret': 1, 'msg': '请使用管理员账户登录'})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})

    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})

def find_obj(tagName,parent_tagName,tagText,grandpa_tagName):
    f=open("./template/killer/welcometest.html","r",encoding="utf-8")
    soup=BeautifulSoup(f.read(),"html.parser")
    f.close()
    body=soup.body
    objs=body.find_all(tagName)
    for obj in objs:
        if obj.text==tagText and obj.parent.name==parent_tagName and obj.parent.parent.name==grandpa_tagName:
            print(obj)
            return str(obj)
def test1(request):
    obj_tagname=str.lower(request.POST.get("tagName"))
    obj_parentTagname= str.lower(request.POST.get("parent_tagName"))
    obj_text=request.POST.get("tagText")
    obj_grandpaTageName=str.lower(request.POST.get("grandpa_tagName"))
    obj=find_obj(obj_tagname,obj_parentTagname,obj_text,obj_grandpaTageName)
    return HttpResponse(obj)

# 登出处理
def signout(request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})

def loadLabelData(request):
    content=request.POST.get("content")
    attribute = request.POST.get("attribute")
    return HttpResponse(content+attribute)