from django.shortcuts import render, get_object_or_404, Http404

# Create your views here.

def home(request):
    context = {}
    return render(request, "website/index.html", context=context)
