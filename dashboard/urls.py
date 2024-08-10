from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('products/', views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/', views.product_delete,
         name='dashboard-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail,
         name='dashboard-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit,
         name='dashboard-products-edit'),
    path('customers/', views.customers, name='dashboard-customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='dashboard-customer-detail'),
    path('order/', views.order, name='dashboard-order'),
    path('order/action/<int:order_id>/accept/', views.order_accept, name='order-accept'),
    path('order/action/<int:order_id>/deny/', views.order_deny, name='order-deny'),
    path('product-details/<int:pk>/', views.view_product_details, name='product-detail-view'),
]
