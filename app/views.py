from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import BernieCalcForm

# Create your views here.

class HomePageView(TemplateView):

  template_name = 'pages/home.html'

  def get_context_data(self, **kwargs):

    context = super().get_context_data(**kwargs)

    context['form'] = BernieCalcForm

    return context
