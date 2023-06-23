from django.urls import path
from .views import SignUpView,MyLoginView, MyLogoutView, create_post, post_list
from . import views

urlpatterns = [
    
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('create/', create_post, name='create_post'),
    path('', post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/',views.post_update, name='post_update'),
    path('post/<int:pk>/delete/',views.post_delete, name='post_delete'),

]
