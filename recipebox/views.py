from django.shortcuts import render
from recipebox.models import RecipeTitle, Author 
from recipebox.forms import RecipesForm, AuthorsForm



def index(request, *args, **kwargs):

    html = 'hello.html'
    items = RecipeTitle.objects.all()
    return render(request, html, {'recipes': items})


def recipe_info(request, id):
    html = 'recipes.html'
    items = RecipeTitle.objects.all().filter(id=id)
    instructions = items[0].instructions.split("/n")
    return render(request, html, {'recipes': items, "instructions": instructions})

   
def authordetails(request, id):
    html = 'authordetails.html'
    authors = Author.objects.all().filter(id=id)
    items = RecipeTitle.objects.all().filter(author_id=id)
    return render(request, html, {'recipes': items, "authors": authors})


def addrecipe(request):
    html = "addrecipe.html"
    form = None
    if request.method == "POST":
        form = RecipesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RecipeTitle.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                time=data["time"],
                instructions=data["instructions"],
            )
        return render(request, "added.html")
    else:
        form = RecipesForm()
    return render(request, html, {"form": form})


def addauthor(request):
    html = "addauthor.html"
    form = None
    if request.method == "POST":
        form = Author(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
            )
        return render(request, "added.html")
    else:
        form = Author()
    return render(request, html, {"form": form})
