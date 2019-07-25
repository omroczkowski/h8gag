"""h8gag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pages.views import home_view
from pages.views import login_view
from pages.views import logout_view
from pages.views import cancel_view
from pages.views import signup_view
from meme.views import add_meme_view
from meme.views import memes_view
from meme.views import meme_detail_view
from meme.views import upvote, downvote, unvote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cancel/', cancel_view, name='cancel'),
    path('signup/', signup_view, name='signup'),
    path('add_meme/', add_meme_view, name='add_meme'),
    path('memes/<category>', memes_view, name='memes'),
    path('meme/<id>/', meme_detail_view, name='meme_detail'),
    path('upvote/<id>/', upvote, name='upvote'),
    path('downvote/<id>/', downvote, name='downvote'),
    path('unnvote/<id>/', unvote, name='unvote'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)