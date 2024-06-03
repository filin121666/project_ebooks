from django.shortcuts import render
from django.views.generic.base import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='netlibrary/home.html')