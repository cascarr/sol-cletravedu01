from django.shortcuts import render

# Create your views here.
def homepg(request):
    return render(request, 'mainApp/cletravedu/frontend/index.html')

# Loads the enquiry.html page
def enquirypg(request):
    return render(request, 'mainApp/cletravedu/frontend/enquiry.html')

# Loads the about.html page
def aboutpg(request):
    return render(request, 'mainApp/cletravedu/frontend/about.html')

# Loads the news.html page
def newspg(request):
    return render(request, 'mainApp/cletravedu/frontend/news.html')