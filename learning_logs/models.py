from django.db import models
#参考Django Model Field Reference

# Create your models here.
class Topic(models.Model):
	"""用户学习的主题"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Entry(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""返回模型8的字符串表示"""
		show_text = self.text[:50]
		"""文本长于50，结尾添加省略号"""
		if len(self.text) >= 50:
			show_text = show_text + "..."
		return show_text