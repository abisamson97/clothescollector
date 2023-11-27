from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Clothes, Accessory
from .forms import WearingForm

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def clothes_index(request):
  clothes = Clothes.objects.all()
  return render(request, 'clothes/index.html', {
    'clothes': clothes
  })

def clothes_detail(request, clothes_id):
  clothes = Clothes.objects.get(id=clothes_id)
  id_list = clothes.accessories.all().values_list('id')
  accessories_clothes_doesnt_have = Accessory.objects.exclude(id__in=id_list)
  wearing_form = WearingForm()
  return render(request, 'clothes/detail.html', { 
    'clothes': clothes, 'wearing_form': wearing_form,
    'accessories': accessories_clothes_doesnt_have
  })

class ClothesCreate(CreateView):
  model = Clothes
  fields = ['type', 'material', 'description', 'size']

class ClothesUpdate(UpdateView):
  model = Clothes
  fields = ['material', 'description', 'size']

class ClothesDelete(DeleteView):
  model = Clothes
  success_url = '/clothes'

def add_wearing(request, clothes_id):
  form = WearingForm(request.POST)
  if form.is_valid():
    new_wearing = form.save(commit=False)
    new_wearing.clothes_id = clothes_id
    new_wearing.save()
  return redirect('detail', clothes_id=clothes_id)

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

def assoc_accessory(request, cat_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Clothes.objects.get(id=clothes_id).accessories.add(accessory_id)
  return redirect('detail', clothes_id=clothes_id)
