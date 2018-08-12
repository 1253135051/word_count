#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	#return  HttpResponse('你好')
	return  render(request,'firstpage.html')


def count(request):
	#print(len(request.GET['text'])) # 获取输入字符串总长度，在命令行打印出来
	user_text =  request.GET['text']
	total_count = len(request.GET['text'])

	word_dict = {}
	for word in user_text:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1
	sorted_dict =\
			sorted(word_dict.items(), key = lambda w:w[1], reverse = True)

	return  render(request,'secpage.html', 
		   {'count': total_count,'text':user_text,'word': word_dict,'sorted': sorted_dict})
	


def login(request):
	return render(request, 'login.html')