from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

# welcome 이라는 함수를 요청하면 이 함수는 render 라는 함수로 welcome.html 을 띄워준다. request는 서로의 약속.

def hello(request):
    userName = request.GET["name"]
    return render(request, "hello.html", {'userName' : userName})
