"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from recipebox.views import index, recipe_info, authordetails, addrecipe, addauthor, login_view, logout_view, signup
from recipebox.models import RecipeTitle, Author

admin.site.register(RecipeTitle)
admin.site.register(Author)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("recipes/<int:id>", recipe_info),
    path("author/<int:id>", authordetails),
    path("addrecipe/", addrecipe),
    path("addauthor/", addauthor),
    path("signup/", signup),
    path("login/", login_view),
    path("logout/", logout_view),
]
