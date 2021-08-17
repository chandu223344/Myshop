from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View




class Signup(View):
        def get(self,request):
                return render(request,'signup.html')

        def post(self,request):
                postData = request.POST
                first_name = postData.get('firstname')
                last_name = postData.get("lastname")
                phone = postData.get("phone")
                email = postData.get("email")
                password = postData.get("password")      

       
                # when error come previous given data stay
                value = {
                   'first_name' : first_name,
                   'last_name' : last_name,
                   'phone' : phone,
                   'email' : email  
                } 
                # create customer object   
                customer = Customer(first_name = first_name,
                        last_name =last_name,        
                        phone = phone,        
                        email = email,        
                        password = password)
        
                error_message = self.validateCustomer(customer)
        
    
                if not error_message:
            
                  # password hashing
                  customer.password = make_password(customer.password)
                  # password hashing

                  #saving the customer 
                  customer.register()
                  return redirect('homepage')  
                else:
                  data = {
                    'error':error_message,    
                    'values': value
                  }
                  return render(request,'signup.html',data)


        def validateCustomer(self,customer):
                error_message = None
                if(not customer.first_name):
                        error_message = "First Name must be required!!"
                elif len(customer.first_name)<4:
                        error_message = "First name must be 4 char long or more"
                elif (not customer.last_name):
                        error_message = "Last Name must be required!!"
                elif len(customer.last_name)<2:
                        error_message = "Last name must be 2 char long or more"
                elif (not customer.phone):
                        error_message = "Phone Number must be required!!"
                elif len(customer.phone)<10:
                        error_message = "Phone Number must be 10 char long"
                elif len(customer.phone)>10:
                        error_message = "Phone Number must be 10 char long"
                elif len(customer.email)<5:
                        error_message = "Email must be 5 char long or above"
                elif (not customer.password):
                        error_message = "Password must be required"
                elif len(customer.password)<8:
                        error_message = "Passsword Must be 8 char long or more "
                elif customer.isExist():
                        error_message ="Email already Exist"
        
                return error_message

