"""
URL configuration for suppliers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from app.views import loginview, login_action, logout_action
from app.views import productlistview, addproduct, deleteproduct, confirmdeleteproduct, \
    edit_product_get, edit_product_post, products_filtered
from app.views import supplierlistview, addsupplier, deletesupplier, confirmdeletesupplier, \
    edit_supplier_get, edit_supplier_post, searchsuppliers
from app.views import customerlistview, addcustomer, confirmdeletecustomer, deletecustomer, searchcustomers, edit_customer
from app.views import order_list_view, add_order, confirm_delete_order, delete_order, orders_by_customer, update_order_status

urlpatterns = [
    
    # Loginview and authentication methods
    path('', loginview, name='loginview'),
    path('login/', login_action, name='login_action'),
    path('logout/', logout_action, name='logout_action'),
    
    # Product urls
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get, name='edit_product_get'),
    path('edit-product-post/<int:id>/', edit_product_post, name='edit_product_post'),
    path('products-by-supplier/<int:id>/', products_filtered, name='products_filtered'),

    # Supplier urls
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get, name='edit_supplier'),
    path('edit-supplier-post/<int:id>/', edit_supplier_post, name='edit_supplier_post'),
    path('search-suppliers/', searchsuppliers),

    # Customer URLs
    path('customers/', customerlistview, name='customer_list'),
    path('customers/add/', addcustomer, name='customer_add'),
    path('customers/search/', searchcustomers, name='customer_search'),
    path('customers/<int:id>/edit/', edit_customer, name='customer_edit'),
    path('customers/<int:id>/delete/confirm/', confirmdeletecustomer, name='customer_confirm_delete'),
    path('customers/<int:id>/delete/', deletecustomer, name='customer_delete'),
    
    # Order URLs
    path('orders/', order_list_view, name='order_list'),
    path('orders/add/', add_order, name='order_add'),
    path('orders/<int:id>/delete/confirm/', confirm_delete_order, name='order_confirm_delete'),
    path('orders/<int:id>/delete/', delete_order, name='order_delete'),
    path('customers/<int:id>/orders/', orders_by_customer, name='orders_by_customer'),
    path('orders/<int:id>/update-status/', update_order_status, name='order_update_status'),

]
