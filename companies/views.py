#from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Company


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Company
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Company.objects.filter(
            Q(name__icontains=query) | Q(score__icontains=query) | Q(graph_image__icontains=query) | Q(words_frequency_image__icontains=query)
        )
        return object_list
