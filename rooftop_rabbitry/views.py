from django.shortcuts import render
from .forms import *
from .models import *
from django.views.generic import *
# Create your views here.

def home(request):
    return render(request, 'rooftop_rabbitry/index.html')

def contact_us(request):
    return render(request, 'rr/contact_us.html')

def fish_farm(request):
    return render(request, 'rr/fish_farm.html')

def rabbit_farm(request):
    my_rabbits = Rabbit.objects.all()
    rabbit_breeds = RabbitBreed.objects.all()
    return render(request, 'rr/rabbit_farm.html',{'rabbits':my_rabbits, 'breeds':rabbit_breeds})

def add_rabbit(request):
    if request.method == 'POST':
        form = RabbitForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RabbitForm()
    return render(request, 'rooftop_rabbitry/rabbit_create.html', {'form': form})

def add_breed(request):
    if request.method == 'POST':
        form = breedForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = breedForm()
    return render(request, 'rooftop_rabbitry/breed_create.html', {'form': form})


# class RabbitListView(ListView):
#     model = Rabbit
#     template_name = 'index.html'
#     context_object_name = 'rabbits'

# class rabbitDetailView(DetailView):
#     model = Rabbit
#     template_name = 'rabbit_detail.html'
#     context_object_name = 'rabbits'

# class rabbitCreateView(CreateView):
#     model = Rabbit
#     template_name = 'rooftop_rabbitry/rabbit_create.html'
#     context_object_name = 'rabbits'

# class rabbitUpdateView(UpdateView):
#     model = Rabbit
#     template_name = 'rabbit_update.html'
#     context_object_name = 'rabbits'

# class rabbitDeleteView(DeleteView):
#     model = Rabbit
#     template_name = 'rabbit_delete.html'
#     context_object_name = 'rabbits'