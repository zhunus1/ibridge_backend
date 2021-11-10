from django.urls import path
from .views import (
    LogoListView,
    FormView,
    CalculatorFormView,
)
urlpatterns = [
    path('logos/', LogoListView.as_view(), name='logos'),
    path('form/', FormView.as_view(), name='form'),
    path('calculator/', CalculatorFormView.as_view(), name='calculator'),
]
