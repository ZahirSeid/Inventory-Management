from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProductForm, OrderForm
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
from datetime import date

@login_required(login_url='user-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    employee = User.objects.filter(groups=2)
    employee_count = employee.count()

    if request.method == 'POST':
        form = OrderForm(request.POST, user=request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.employee = request.user
            obj.borrowed_date = date.today()  # Automatically set the borrowed date to today
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm(user=request.user)
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'employee_count': employee_count,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    employee = User.objects.filter(groups=2)
    employee_count = employee.count()
    order = Order.objects.all()
    order_count = order.count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/products.html', context)


@login_required(login_url='user-login')
def product_detail(request, pk):
    context = {}
    return render(request, 'dashboard/products_detail.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def employees(request):
    employee = User.objects.filter(groups=2)
    employee_count = employee.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'employee': employee,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/employees.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def employee_detail(request, pk):
    employee = User.objects.filter(groups=2)
    employee_count = employee.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    employees = User.objects.get(id=pk)
    context = {
        'employees': employees,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/employees_detail.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    context = {
        'order': orders,
    }
    return render(request, 'dashboard/order.html', context)

@login_required(login_url='user-login')
def order_action(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            order.status = 'Accepted'
            messages.success(request, 'Order accepted successfully.')
        elif action == 'deny':
            order.status = 'Denied'
            messages.success(request, 'Order denied successfully.')
        order.save()
    return redirect('dashboard-order')