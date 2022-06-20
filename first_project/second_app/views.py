from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# part 1
# def index(request):
#     return HttpResponse("This is the second app home page")
# def secondpage(request):
#     return HttpResponse("This is second page for the website")
# def helloworld(request):
#     return HttpResponse("hello world")
# def regex(request):
#     return HttpResponse("This is regex")
# =========================
# # Part 2
def index(request):
    my_dict = {'insert_me': "Now I am coming from first_app/index.html! but from index1",
               'topic_name': "Django Tutorial"}
    return render(request, 'first_app/index.html', context=my_dict)

def index1(request):
    my_dict = {'insert_me': "Now I am coming from first_app/index.html! but from index1",
               'topic_name': "Django Tutorial"}
    return render(request, 'first_app/index.html', context=my_dict)


#
def helloworld(request):
    return HttpResponse("hello world")

# A Context is a dictionary with variable names as the key and their values as the value.
