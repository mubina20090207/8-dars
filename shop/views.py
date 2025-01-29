from django.views.generic import ListView
from .models import Product
from random import sample

class HomePageView(ListView):
    model = Product
    template_name = 'shop/home.html'  
    context_object_name = 'products'
    paginate_by = 10  

    def get_queryset(self):
        all_products = list(Product.objects.all())
        return sample(all_products, min(10, len(all_products)))