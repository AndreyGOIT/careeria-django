from django.shortcuts import render

# Create your views here.
def landing_view(request):
    return render(request, 'landingpage.html')

def supplier_list_view(request):
    return render(request, 'supplierlist.html')

def product_list_view(request):
    return render(request, 'productlist.html')