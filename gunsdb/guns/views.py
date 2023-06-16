from django.shortcuts import render
from .models import Gun, Type
from django.views.generic import ListView, DetailView


def index(request):
    num_guns = Gun.objects.all().count()
    typ = 'Útočné pušky'
    context = {
        'nadpis': typ,
        'num_guns': num_guns,
        'guns': Gun.objects.order_by('name').filter(type__name=typ),
        'types': Type.objects.all()
    }
    return render(request, 'index.html', context=context)


class GunListView(ListView):
    model = Gun
    context_object_name = 'guns_list'
    template_name = 'gun/list.html'


class GunDetailView(DetailView):
    model = Gun
    context_object_name = "gun_detail"
    template_name = 'gun/detail.html'
