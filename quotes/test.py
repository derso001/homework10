import os
import django
import pprint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')

django.setup()

from quoteapp.models import Quote, Author

quote = Quote.objects.all()[0]
print(quote.author)