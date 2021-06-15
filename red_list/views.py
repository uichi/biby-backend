from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Animal, Category, Classification
from django.db.models import Q
from functools import reduce
import operator


class Top(ListView):
    template_name = 'red_list/animal.html'
    model = Animal
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            category = Category.objects.filter(reduce(operator.or_, (Q(name__contains=keyword) for keyword in query.split())))
            classification = Classification.objects.filter(reduce(operator.or_, (Q(name__contains=keyword) for keyword in query.split())))
            object_list = Animal.objects.filter(
                reduce(operator.or_, (Q(japanese_name__contains=keyword) for keyword in query.split())) |
                reduce(operator.or_, (Q(scientific_name__contains=keyword) for keyword in query.split())) |
                Q(category__in=category)|
                Q(classification__in=classification)
                )
        else:
            object_list = Animal.objects.all()
        return object_list


class Rule(TemplateView):
    template_name = 'red_list/rule.html'