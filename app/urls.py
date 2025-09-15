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
from app.views import customerlistview, addcustomer, confirmdeletecustomer, deletecustomer, searchcustomers

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

    # Customer and Order urls will be added later
    path('customers/', customerlistview, name='customerlistview'),
    path('add-customer/', addcustomer, name='addcustomer'),  # Placeholder for add customer view
    path('confirm-delete-customer/<int:id>/', confirmdeletecustomer, name='confirmdeletecustomer'),  # Placeholder for confirm delete customer view
    path('delete-customer/<int:id>/', deletecustomer, name='deletecustomer'),  # Placeholder for delete customer view
    path('search-customers/', searchcustomers, name='searchcustomers'),  # Placeholder for search customer view

]
