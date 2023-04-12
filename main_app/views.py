from django.shortcuts import render
from .models import Finch

finches = [
  {'name': 'Birdie', 'breed': 'House finch', 'description': 'will stay and pose for photographs', 'age': 3},
  {'name': 'Feathers', 'breed': 'European goldfinch', 'description': 'loves dandelions', 'age': 2},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    #  this is passing in data for our render
    'finches': finches
  })

def finches_detail(request, finch_id):
   finch = Finch.objects.get(id=finch_id)
   return render(request, 'finches/detail.html', {'finch': finch})