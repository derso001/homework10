from django.shortcuts import render
from .models import Quote

def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quoteapp/index.html', {"quotes": quotes})
