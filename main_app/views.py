from django.shortcuts import render

finches = [
  {'name': 'Birdie', 'breed': 'House finch', 'description': 'will stay and pose for photographs', 'age': 3},
  {'name': 'Feathers', 'breed': 'European goldfinch', 'description': 'loves dandelions', 'age': 2},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def finches_index(request):
  return render(request, 'finches/index.html', {
    #  this is passing in data for our render
    'finches': finches
  })