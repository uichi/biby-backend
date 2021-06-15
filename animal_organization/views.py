from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Hospital
from django.db.models import Q, query


class Top(ListView):
    template_name = 'animal_organization/top.html'
    model = Hospital
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            object_list = Hospital.objects.filter(
                Q(name__contains=query) | Q(address_name__contains=query))
        else:
            object_list = Hospital.objects.all()
        return object_list