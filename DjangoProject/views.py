from django.shortcuts import render

def home(request):
    return render(request, "base.html", {})
# The block above is a function based view where {} is a dictionary
# to pass an object from backend to frontend
# Template = Frontend , View = Backend
# Proceed to Link views to a URL path, don't forget to import your views to url
