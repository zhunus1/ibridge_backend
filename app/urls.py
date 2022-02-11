from django.urls import path
from .views import (
    LogoListView,
    FormView,
    CalculatorFormView,
    SeoTextListView
)
urlpatterns = [
    path('logos/', LogoListView.as_view(), name='logos'),
    path('form/', FormView.as_view(), name='form'),
    path('calculator/', CalculatorFormView.as_view(), name='calculator'),
    path('seo/', SeoTextListView.as_view(), name='seo'),
]
