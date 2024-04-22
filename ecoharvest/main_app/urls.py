from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.ProductList.as_view(), name='product_index'),
    path('products/<int:product_id>/', views.products_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('orders/', views.order, name="order"),
    path('orders/new/', views.new_order, name="new_order"),
    path('products/<int:product_id>/add_photo/', views.add_photo, name='add_photo'),
]