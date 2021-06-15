from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Animal, Category, Classification
from django.db.models import Q, query


class Top(ListView):
    template_name = 'red_list/animal.html'
    model = Animal
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            category = Category.objects.filter(name__contains=query)
            classification = Classification.objects.filter(name__contains=query)
            object_list = Animal.objects.filter(
                Q(japanese_name__contains=query) | Q(scientific_name__contains=query) | Q(category__in=category) | Q(classification__in=classification))
        else:
            object_list = Animal.objects.all()
        return object_list


class Rule(TemplateView):
    template_name = 'red_list/rule.html'