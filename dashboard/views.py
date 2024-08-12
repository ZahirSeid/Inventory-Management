from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
from django.contrib.auth.models import Group



@login_required(login_url='user-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    employee = User.objects.filter(groups=2)
    employee_count = employee.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.employee = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
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
    product_quantity = Product.objects.filter(name='')
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
    context = {

    }
    return render(request, 'dashboard/products_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def employees(request):
    # Retrieve the group by name
    try:
        employee_group = Group.objects.get(name='employees')
    except Group.DoesNotExist:
        employee_group = None

    if employee_group:
        # Filter users who belong to the 'employees' group
        employee = User.objects.filter(groups=employee_group)
    else:
        employee = User.objects.none()  # No users if the group doesn't exist

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
    # Retrieve the group by name
    try:
        employee_group = Group.objects.get(name='employees')
    except Group.DoesNotExist:
        employee_group = None

    if employee_group:
        # Filter users who belong to the 'employees' group
        employee = User.objects.filter(groups=employee_group)
    else:
        employee = User.objects.none()  # No users if the group doesn't exist

    try:
        # Fetch the specific employee by primary key (pk)
        employees = employee.get(id=pk)
    except User.DoesNotExist:
        employees = None

    employee_count = employee.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    
    context = {
        'employees': employees,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/employees_detail.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def employee_order_history(request, pk):
    # Fetch the specific employee using the primary key
    employee = get_object_or_404(User, pk=pk)

    # Filter orders for this specific employee
    orders = Order.objects.filter(employee=employee)

    # Context to be passed to the template
    context = {
        'employee': employee,
        'orders': orders,
    }

    return render(request, 'dashboard/employee_order_history.html', context)

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
def view_product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'dashboard/product_detail_view.html', context)


@login_required(login_url='user-login')
def order(request):
    order = Order.objects.all()
    order_count = order.count()
    employee = User.objects.filter(groups=2)
    employee_count = employee.count()
    product = Product.objects.all()
    product_count = product.count()

    context = {
        'order': order,
        'employee_count': employee_count,
        'product_count': product_count,
        'order_count': order_count,
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

@login_required
def order_accept(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'accepted'
    order.save()
    return redirect('dashboard-order')

@login_required
def order_deny(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.status = 'denied'
    order.save()
    return redirect('dashboard-order')