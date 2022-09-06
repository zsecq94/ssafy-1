from django.shortcuts import render

import calculators

# Create your views here.
def cal(request):
    return render(request, 'calculators.html')