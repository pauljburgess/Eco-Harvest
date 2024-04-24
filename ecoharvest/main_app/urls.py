from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.ProductList.as_view(), name='product_index'),
    path('products/<int:product_id>/', views.products_detail, name='detail'),
    path('orders/', views.order, name="order"),
    path('orders/index/', views.order_index, name="order_index"),
    path('orders/create/', views.OrderCreate.as_view(), name="create_order"),
    path('orders/<int:pk>/update/', views.OrderUpdate.as_view(), name="order_update"),
    path('orders/<int:pk>/delete/', views.OrderDelete.as_view(), name="order_delete"),
    path('orders/<int:order_id>/', views.order_detail, name="order_detail"),
    path('orders/<int:order_id>/add_order_line/', views.add_order_line, name='add_order_line'),
    path('products/<int:product_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
    path('pickups/index/', views.pickup_index, name="pickup_index"),
    path('pickups/create/', views.OrderCreate.as_view(), name="create_opickup"),
    
]