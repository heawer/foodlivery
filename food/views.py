from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Food, FoodCategory
from .forms import FoodForm, RegisterForm, FoodCategoryForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')

        form = RegisterForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )

@login_required
def create_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.cook = request.user
            food.save()
            return redirect('my_listings')
    else:
        initial_data = {}
        category_id = request.GET.get('category')
        if category_id:
            initial_data['category'] = category_id
        form = FoodForm(initial=initial_data)
    return render(request, 'menu/food_form.html', {'form': form})

@login_required
def my_listings(request):
    foods = Food.objects.filter(cook=request.user)  # Fetch food items created by the user
    categories = FoodCategory.objects.filter(cook=request.user).distinct()  # Fetch categories with food created by the user
    return render(request, 'menu/my_listings.html', {
        'foods': foods,
        'categories': categories
    })

@login_required
def update_food(request, pk):
    food = get_object_or_404(Food, pk=pk, cook=request.user)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('my_listings')
    else:
        form = FoodForm(instance=food)
    return render(request, 'menu/food_form.html', {'form': form})

@login_required
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk, cook=request.user)
    if request.method == 'POST':
        food.delete()
        return redirect('my_listings')
    return render(request, 'menu/confirm_delete_food.html', {'food': food})

def category_detail(request, pk):
    category = get_object_or_404(FoodCategory, pk=pk)
    foods = Food.objects.filter(category=category)
    return render(request, 'menu/category_detail.html', {
        'category': category,
        'foods': foods
    })
    
    
def home(request):
    categories = FoodCategory.objects.all()[:4] 
    foods = Food.objects.all()[:8]
    return render(request, 'menu/home.html', {
        'categories': categories,
        'foods': foods
    })


def all_categories(request):
    categories = FoodCategory.objects.all()  
    return render(request, 'menu/all_categories.html', {
        'categories': categories
    })


def all_food(request):
    foods = Food.objects.all()  
    return render(request, 'menu/all_food.html', {
        'foods': foods
    })

@login_required
def create_category(request):
    if request.method == 'POST':
        form = FoodCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.cook = request.user
            category.save()
            return redirect('home')
    else:
        form = FoodCategoryForm()
    return render(request, 'menu/category_form.html', {'form': form})


@login_required
def update_category(request, pk):
    category = get_object_or_404(FoodCategory, pk=pk)
    if request.method == 'POST':
        form = FoodCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=category.id)
    else:
        form = FoodCategoryForm(instance=category)
    return render(request, 'menu/category_form.html', {'form': form})

@login_required
def delete_category(request, pk):
    category = get_object_or_404(FoodCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('home')
    return render(request, 'menu/confirm_delete_category.html', {'category': category})