from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('', views.home, name='home'),
    path('add-review/', views.add_review, name='add_review'),
    path('review_list/', views.all_reviews, name='review_list'),
<<<<<<< HEAD
    # In your `urls.py`
    path('reviews/<str:name>/', views.detail, name='review_detail'),

=======
    path('reviews/<int:id>/',views.detail,name = 'review_detail'),
>>>>>>> b0f25a95475018487945e2e5370fe479f7e2e6aa
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('edit_review/<int:id>/',views.edit_review,name = "edit_review"),
    path('delete_review/<int:id>/',views.delete_review,name = "delete_review"),
    path('search_reviews/',views.search_reviews,name = 'search_reviews'),
    path('logout/', views.logout_user, name='logout_user'),
]
