from django.shortcuts import render
# handles a http request
# Create your views here.
from .forms import ProductuploadForm

def upload_product(request):
    form = ProductuploadForm()
    
    return render(request, "inventory/product_upload.html", {"form": form})
