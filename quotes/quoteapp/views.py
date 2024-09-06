from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quote, Tag, Author
from .forms import QuoteForm, AuthorForm, TagForm

def main(request):
    quotes =  Quote.objects.all()[0:6]
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
            # new_quote.user = request.user
            new_quote.save()

            choice_author = Author.objects.filter(fullname__in=request.POST.getlist('author'))
            for author in choice_author.iterator():
                new_quote.author = author

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            new_quote.save()


            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags,"authors":authors, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, "authors":authors, 'form': QuoteForm()})


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})
