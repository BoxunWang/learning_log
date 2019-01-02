from django import forms
from .models import Topic
class TopicForm(forms.ModelForm):
	class Meta:
		"""告诉Django,根据那个模型创建表单,在表单中包含哪些字段"""
		model = Topic 		#以模型opic 创建表单
		fields = ['text']	#包含字段
		labels = {'text': ''}#'text'字段的标签为空