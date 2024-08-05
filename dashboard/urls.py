from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('products/', views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/', views.product_delete, name='dashboard-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail, name='dashboard-products-detail'),
    path('products/edit/<int:pk>/', views.product_edit, name='dashboard-products-edit'),
    path('employees/', views.employees, name='dashboard-employees'),
    path('employees/detail/<int:pk>/', views.employee_detail, name='dashboard-employee-detail'),
    path('order/', views.order, name='dashboard-order'),
    path('order/action/<int:order_id>/', views.order_action, name='order-action'),
]
