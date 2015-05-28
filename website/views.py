from django.shortcuts import render, get_object_or_404, Http404
from website.models import Room

# Create your views here.

def home(request):
    context = {
        "rooms": Room.objects.order_by('-price'),
    }
    return render(request, "website/index.html", context=context)
