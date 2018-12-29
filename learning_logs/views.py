from django.shortcuts import render

# Create your views here.
def index(request):
	"""学习笔记的index"""
	return render(request, 'learning_logs/index.html')
