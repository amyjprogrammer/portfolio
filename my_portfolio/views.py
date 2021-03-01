from django.shortcuts import render

"""Portfolio page"""
def index(request):
    return render(request, 'my_portfolio/index.html', {})
