from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from cats.models import Description_of_the_cat, Species, Photo

def indexu(request):
    number = Description_of_the_cat.objects.all().count()
    print(request)
    context = {
        'number': number,
    }
    return render(request, 'index.html', context=context)

class FilmListView(ListView):
    print(ListView)
    model = Description_of_the_cat
    context_object_name = 'cats_photo'
    template_name = 'index.html'
    paginate_by = 12

    def get_queryset(self):
        return Description_of_the_cat.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = len(self.get_queryset())
        context['nazev'] = 'Karty koček'
        context['nazev_poctu'] = 'Počet záznamů :'
        return context
