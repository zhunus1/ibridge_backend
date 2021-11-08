from django.urls import path
from .views import (
    LogoListView,
    CounterListView,
    CountryListView,
    FormView,
    CalculatorFormView,
    UniversityListView,
)
urlpatterns = [
    path('logos/', LogoListView.as_view(), name='logos'),
    path('counters/', CounterListView.as_view(), name='counters'),
    path('countries/', CountryListView.as_view(), name='countries'),
    path('universities/', UniversityListView.as_view(), name='universities'),
    path('form/', FormView.as_view(), name='form'),
    path('calculator/', CalculatorFormView.as_view(), name='calculator'),
]
