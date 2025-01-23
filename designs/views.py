from django.shortcuts import render

# Create your views here.
# views.py
from .models import team  # Adjust this import based on your app name


def standings_view(request):
    teams = team.objects.all().order_by('-points')  # Example: Ordered by points descending
    return render(request, 'standings.html', {'teams': teams})
