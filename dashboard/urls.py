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
    path('employees/', views.employees, name='dashboard-employees'),
    path('employees/detial/<int:pk>/', views.employee_detail,
         name='dashboard-employee-detail'),
    path('employee/<int:pk>/order-history/', views.employee_order_history, name='employee-order-history'),
    path('order/', views.order, name='dashboard-order'),
    path('order/action/<int:order_id>/accept/', views.order_accept, name='order-accept'),
    path('order/action/<int:order_id>/deny/', views.order_deny, name='order-deny'),
    path('order/action/<int:order_id>/return/', views.order_return, name='order-return'),
    path('order/action/<int:order_id>/receive/', views.order_receive, name='order-receive'),
    path('product-details/<int:pk>/', views.view_product_details, name='product-detail-view'),
]