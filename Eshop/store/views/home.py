from django.http import request
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from store.templatetags.cart import is_in_cart

# Create your views here.
class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                       cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else :
                cart[product]= 1   

        else:
            cart={}
            cart[product]= 1
        request.session['cart'] = cart 
        # print( request.session['cart']) 
        return redirect('homepage')



    def get(self,request):
         cart = request.session.get('cart')
         if not cart:
             request.session['cart'] = {}
         products = None
          
         cart = request.session.get('cart')
         if not cart:
             request.session.cart = {}
         
         categories = Category.get_all_catagories()
         categoryID=request.GET.get('category')
         if categoryID:
             products = Product.get_all_products_by_categoryid(categoryID)
         else:
             products = Product.get_all_products()
         data = {}
         data['products'] = products
         data['categories'] = categories
         print(request.session.get('email'))
    
         return render(request,'index.html', data)
     

   




