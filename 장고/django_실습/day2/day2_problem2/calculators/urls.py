from django.urls import path
from . import views


urlpatterns = [

    path('calculators/<int:calculators_id>', views.cal, name='cal')


]
