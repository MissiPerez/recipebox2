from django.shortcuts import render, reverse, HttpResponseRedirect
from recipebox.models import RecipeTitle, Author, User
from recipebox.forms import RecipesForm, AuthorsForm, LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


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

 
@login_required()
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


@login_required()
@staff_member_required()
def addauthor(request):
    html = "addauthor.html"
    form = None
    if request.method == "POST":
        form = AuthorsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
            )
        return render(request, "added.html")
    else:
        form = AuthorsForm()
    return render(request, html, {"form": form})


def signup(request):
    html = 'signup.html'
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data["username"], data["password"])
            login(request, user)
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
                user=user
            )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})


def login_view(request):
    html = 'login.html'
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
