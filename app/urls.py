from django.urls import include, path
from app.views import HomePageView, CalculatorResultsView


urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path("results/", CalculatorResultsView.as_view(), name='calculator_results'),
]