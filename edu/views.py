from django.shortcuts import render
from . import views

# Create your views here.
def skills(request):
    context = {'skills':'active'}
    return render(request, "edu/skills.html", context)