"""URL model for learning_logs """
#将URL映射到视图
from django.conf.urls import url
#从当前文件夹导入视图
from . import views
#包含项目中的应用程序的URL
urlpatterns = [
	#index page
	url(r'^$', views.index, name='index'),
	#显示所有主题
	url(r'^topics/$', views.topics, name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	#添加新主题的网页
	url(r'^new_topic/$', views.new_topic, name='new_topic'),
	#用于添加新条目的页面
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	#用于编辑条目的页面
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
"""
	URL接收三个实参：
	1.正则表达式
		r 	将接下来的字符串视为原始字符串 
		''	内是正则表达式
		^	查看字符串的开头
		$ 	查看字符串的末尾
	2.指定调用的视图函数
	3.指定该URL模式的名称
"""