from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static
app_name='myapp'
urlpatterns = [
    path('', views.index,name='index1'),
    path('index', views.index,name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
    path('logged', views.logged, name='logged'),
    path('products/<int:pk>/',views.product_view,name='products'),
    path('profile/', views.update_student_id, name='profile'),
    path('update_student_id/', views.update_student_id, name='update_student_id'),
    path('request', views.book_request, name='request'),
    path('requests', views.book_request_list, name='requests'),
    path('approval/list/', views.book_approval_list, name='book_approval_list'),
    path('approval/<int:request_id>/', views.approve_book_request, name='approve_book_request'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
