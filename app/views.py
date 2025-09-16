from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, Product, Customer
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm

# LANDING AFTER LOGIN
'''
def landing_view(request):
    return render(request, 'landingpage.html')
'''
# LOGIN AND LOGOUT
def loginview(request):
     return render(request, 'loginpage.html')

# Login action
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')


# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

# Product view´s
def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render (request,"productlist.html",context)

def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)

def edit_product_get(request, id):
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"edit_product.html",context)


def edit_product_post(request, id):
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.packagesize = request.POST['packagesize']
        item.productname = request.POST['productname']
        item.save()
        return redirect(productlistview)

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"productlist.html",context)

# Supplier view´s
def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"supplierlist.html",context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsupp.html",context)


def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)

def edit_supplier_get(request, id):
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request,"edit_supplier.html",context)

def edit_supplier_post(request, id):
        item = Supplier.objects.get(id = id)
        item.contactname = request.POST['contactname']
        item.address = request.POST['address']
        item.phone = request.POST['phone']
        item.email = request.POST['email']
        item.save()
        return redirect(supplierlistview)

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered}
    return render (request,"supplierlist.html",context)

# Customer view's and Order view's will be added later
def customerlistview(request):
    customerlist = Customer.objects.all()
    context = {'customers': customerlist}
    return render(request, 'customerlist.html', context)

def addcustomer(request):
    # Используем .get() для избежания KeyError. '' - значение по умолчанию.
    a = request.POST.get('companyname', '')
    b = request.POST.get('contactname', '')
    c = request.POST.get('email', '')
    d = request.POST.get('phone', '')  # Теперь, если поля нет, будет пустая строка
    e = request.POST.get('address', '')

    # Создаем и сохраняем объект Customer
    Customer(companyname=a, contactname=b, contactemail=c, phone=d, address=e).save()
    return redirect(request.META['HTTP_REFERER'])

def edit_customer(request, id):
    # Получаем клиента или возвращаем 404 если не найден
    customer = get_object_or_404(Customer, id=id)
    
    if request.method == 'POST':
        # Обработка отправленной формы
        customer.companyname = request.POST.get('companyname', customer.companyname)
        customer.contactname = request.POST.get('contactname', customer.contactname)
        customer.contactemail = request.POST.get('email', customer.contactemail)
        customer.phone = request.POST.get('phone', customer.phone)
        customer.address = request.POST.get('address', customer.address)
        customer.save()
        
        # Перенаправляем на список клиентов после успешного редактирования
        return redirect('customer_list')
    
    else:
        # Показываем форму с предзаполненными данными
        context = {'customer': customer}
        return render(request, 'edit_customer.html', context)

def confirmdeletecustomer(request, id):
    # get_object_or_404 автоматически вернет страницу 404, если объект не найден
    customer = get_object_or_404(Customer, id=id)
    context = {'customer': customer}
    return render(request, "confirm_delete_customer.html", context)

def deletecustomer(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect(customerlistview) # Или лучше использовать именованный URL: redirect('customer_list')

def searchcustomers(request):
    # 1. Проверяем, что запрос пришел методом POST
    if request.method == 'POST':
        # 2. Безопасно получаем значение поиска
        search_query = request.POST.get('search', '').strip()
        # 3. Ищем только если строка не пустая
        if search_query:
            filtered_customers = Customer.objects.filter(companyname__icontains=search_query)
        else:
            # Если поиск пустой, показываем всех клиентов
            filtered_customers = Customer.objects.all()
    else:
        # Если запрос не POST, тоже показываем всех
        filtered_customers = Customer.objects.all()

    context = {'customers': filtered_customers}
    return render(request, "customerlist.html", context)