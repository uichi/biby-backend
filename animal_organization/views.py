from django.views.generic import ListView, TemplateView
from .models import Hospital
from django.db.models import Q
from functools import reduce
import operator


class Top(ListView):
    template_name = 'animal_organization/top.html'
    model = Hospital
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            # object_list = Hospital.objects.filter(Q(name__contains=keyword) | Q(address__contains=keyword))
            object_list = Hospital.objects.filter(
                reduce(operator.or_, (Q(name__contains=keyword) for keyword in query.split())) |
                reduce(operator.or_, (Q(address__contains=keyword) for keyword in query.split()))
                )
        else:
            object_list = Hospital.objects.all()
        return object_list