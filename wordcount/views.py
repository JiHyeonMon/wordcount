from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext'] #원문 글 전체를 뜻함
    words=text.split()
    word_dic={}

    for word in words:
        if word in word_dic:
            word_dic[word]+=1
        else:
            word_dic[word]=1

    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dic.items()})