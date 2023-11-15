from django.shortcuts import render

clothes = [
  {'type': 'Pants', 'material': 'denim', 'description': 'black denim, wide-legged, baggy, no rips', 'size': 27},
  {'type': 'T-shirt', 'material': 'cotton', 'description': 'cream graphic tee', 'size': 'Large'},
]
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def clothes_index(request):
  return render(request, 'clothes/index.html', {
    'clothes': clothes
  })
