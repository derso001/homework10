from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quote, Tag, Author
from .forms import QuoteForm, AuthorForm

def main(request):
    quotes =  Quote.objects.all()[0:2]
    context = {"quotes":quotes}

    return render(request, 'quoteapp/index.html', context)

@login_required
def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, "authors":authors, 'form': QuoteForm()})


