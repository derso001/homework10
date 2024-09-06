import os
import django
import pprint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')

django.setup()

from quoteapp.models import Quote, Author

# for quote in Quote.objects.all()[0:3]:
#     print(quote.quote)

#     for tag in quote.tags.all():
#         print(tag)

quotes =  Quote.objects.all()[0:5]
context = {"quotes":quotes}
for quote in quotes:
    tags = quote.tags.all()
    context[quote.quote] = tags

pprint.pprint(context)