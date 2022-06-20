from django.shortcuts import render

# Create your views here.

#from appThree.models import User

from appThree.forms import NewUserForm


def index(request):
    return render(request, 'appThree/index.html')


def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)  # return index view of the request which will basically take it to home page
        else:
            print("FORM INVALID")

    return render(request, 'appThree/users.html', {'form': form})
