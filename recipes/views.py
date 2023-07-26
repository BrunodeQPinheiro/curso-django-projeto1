from django.shortcuts import render


# HTTP Request
def home(request):
    return render(request, 'recipes/pages/home.html')
    # return HTTP Response


# HTTP Request
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
    # return HTTP Response
