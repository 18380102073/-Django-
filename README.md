# -Django-
基于Django网页框架，开发一个对目标网页元素进行手动选择爬取的爬取器

python=3.8.5

Django=3.2.8

requests=2.24.0

beautifulsoup4=4.9.3

在文件Jspider/settings.py中将属性ALLOWED_HOSTS添加你的本机ip，例如“127.0.0.1”或“localhost”，命令行进入项目层，如示图
![QQ图片20220704194026](https://user-images.githubusercontent.com/50491296/177148509-8954a75f-bd64-491a-9056-06e34b8b5646.png)
输入命令python manage.py runserver 0.0.0.0:80开启Django网络server，出现示图结果即证明成功开启

在浏览器输入“你添加的ip/killer/userLogin.html”，例如“localhost/killer/userLogin.html”进入登录页面，输入用户名以及密码，该类信息都存储在数据库sqlite中，使用工具sqlitestudio可进行可视化。我这里的用户名以及密码分别是byby和88888888，输入用户名和密码，进入操作页面（页面美化功能放在未来处理）

![QQ图片20220704195424](https://user-images.githubusercontent.com/50491296/177149750-3af8287c-4ded-4ba6-a5b7-9a94d6c71ae0.png)
输入要处理的网址，获取目标网页

![QQ图片20220704200532](https://user-images.githubusercontent.com/50491296/177151354-18f536dc-fb16-4dc2-a451-74b245af8240.png)

例如新浪网主页，用鼠标框选页面元素，获取该元素所在祖父节点到该元素所在节点的html文本元素

![QQ图片20220704200812](https://user-images.githubusercontent.com/50491296/177153389-564278fb-d523-416e-836f-1a42a14bf838.png)
