from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .forms import MovieReviewForm
from .models import MovieReview,Like,Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models import Count


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('review_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login_user')


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def add_review(request):
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.save()
            return redirect('review_list')
    else:
        form = MovieReviewForm()
    return render(request, 'add_review.html', {'form': form})


@login_required
def all_reviews(request):
    reviews = MovieReview.objects.all().annotate(
        like_count=Count('like'),
        comment_count=Count('comment')
    )  # Here count is an aggregate function, add new fields to each object.
    return render(request, 'review_list.html', {'reviews': reviews})

@login_required
def detail(request,id):
    movie_review = MovieReview.objects.get(id=id)
    if request.method == 'POST':
        if 'like' in request.POST:
            like, created = Like.objects.get_or_create(user=request.user, review=movie_review)
            if not created:
                like.delete()  # Toggle like functionality
            return redirect('review_detail', id=id)
        if 'comment' in request.POST:
            content = request.POST.get('content')
            if content:
                Comment.objects.create(user=request.user, review=movie_review, content=content)
            return redirect('review_detail', id=id)
    comments = Comment.objects.filter(review=movie_review).order_by('-created_at')
    likes = Like.objects.filter(review=movie_review).count()
    context = {
        'movie_review': movie_review,
        'comments': comments,
        'likes': likes,
    }
    return render(request,'review_details.html',context)


@login_required
def dashboard(request):
    if request.user.is_authenticated:
        reviews = MovieReview.objects.filter(user = request.user)
    else:
        reviews = []
    return render(request,'dashboard.html',{'reviews':reviews})

@login_required
def edit_review(request, id):
    review = get_object_or_404(MovieReview, id=id, user=request.user)  
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
    else:
        form = MovieReviewForm(instance=review)  
    return render(request, 'edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, id):
    review = get_object_or_404(MovieReview, id=id, user=request.user)  
    review.delete()
    return redirect('dashboard') 

def search_reviews(request):
    query = request.GET.get('query','')
    if query:
        reviews = MovieReview.objects.filter(
            Q(movie_name__icontains = query)|Q(review__icontains = query)|Q(rating__icontains = query)
        )
        # Q is an alternate function for filter, used to combine multiple queries
        #icontains = perform case sensitive search
    else:
        reviews = MovieReview.objects.all()
    return render(request,'review_list.html',{'reviews':reviews,'query':query})

