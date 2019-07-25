from django.shortcuts import render
from .forms import MemeForm
from .models import Meme

# Create your views here.

#view with meme form
def add_meme_view(request):
    added = False
    if request.method == 'POST':
        print(request.POST)
        meme_form = MemeForm(request.POST, request.FILES)
        if meme_form.is_valid():
            meme_form.save()
            added = True
        else:
            print(meme_form.errors)
    else:
        meme_form = MemeForm()
    return render(request, 'add_meme.html',
                  {'meme_form': meme_form,
                   'added': added,
                   'errors': meme_form.errors})

# display memes from category given - view
def memes_view(request, category):
    memes = Meme.objects.filter(category=category)
    context = {
        'memes': memes,
    }

    return render(request, 'memes.html', context)

# meme detailed view
def meme_detail_view(request, id):
    meme = Meme.objects.get(id=id)
    context = {
        'meme': meme,
    }
    return render(request, 'meme_detail.html', context)

def upvote(request, id):
    meme = Meme.objects.get(id=id)
    meme.upvoters.add(request.user)
    meme.downvoters.remove(request.user)
    memes = Meme.objects.filter(category=meme.category)
    meme.rank = meme.upvoters.all().count() - meme.downvoters.all().count()
    meme.save()
    context = {
        'memes': memes,
    }
    return render(request, 'memes.html', context)

def downvote(request, id):
    meme = Meme.objects.get(id=id)
    meme.downvoters.add(request.user)
    meme.upvoters.remove(request.user)
    memes = Meme.objects.filter(category=meme.category)
    meme.rank = meme.upvoters.all().count() - meme.downvoters.all().count()
    meme.save()
    context = {
        'memes': memes,
    }
    return render(request, 'memes.html', context)

def unvote(request, id):
    meme = Meme.objects.get(id=id)
    meme.downvoters.remove(request.user)
    meme.upvoters.remove(request.user)
    meme.rank = meme.upvoters.all().count() - meme.downvoters.all().count()
    meme.save()
    memes = Meme.objects.filter(category=meme.category)
    context = {
        'memes': memes,
    }
    return render(request, 'memes.html', context)


