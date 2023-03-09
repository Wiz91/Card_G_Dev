from django.shortcuts import render,redirect
from .models import Shop_categories,Shop
from Account.models import Account
from Grading.models import Card
from django.contrib import messages

# Create your views here.

def add_product(request):
    if 'Userid' in request.session:
      if request.method == "POST":  
            user_id=request.session['Userid']
            product_name=request.POST['pro_name']
            discounted_Amt=request.POST['D_amt']
            actual_Amt=request.POST['A_amt']
            carte=request.POST['cate']
            key1=request.POST['Key1']
            quantity=request.POST['card_quantity']
            Value1=request.POST['Value1']
            user=Account.objects.get(id=user_id)
            cartegory=Shop_categories.objects.get(id=carte)
            all_cards=Card.objects.all()
            obj_fil=Account.objects.filter(id=user_id).values()
            username=obj_fil[0]["First_name"]
            Category=Shop_categories.objects.all()
            if obj_fil[0]['is_admin']==True:
                  modrater_type="Admin"
            else:
                  modrater_type="Staff"
            try:
                  if len(request.FILES) !=0:
                        Product_img=request.FILES['P_img']
                  if 'Key8' in request.POST.keys() and request.POST['Key8']:
                        return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category,"error":"Only 7 filed of details are allowed"})
                  elif 'Key7' in request.POST.keys() and request.POST['Key7']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        key4=request.POST['Key4']
                        Value4=request.POST['Value4']
                        key5=request.POST['Key5']
                        Value5=request.POST['Value5']
                        key6=request.POST['Key6']
                        Value6=request.POST['Value6']
                        key7=request.POST['Key7']
                        Value7=request.POST['Value7']
                        product_det={key1:Value1,key2:Value2,key3:Value3,key4:Value4,key5:Value5,key6:Value6,key7:Value7}
                        add_pro=Shop.objects.create(Product_name=product_name,Discount_price=discounted_Amt,quantity=quantity,Actual_price=actual_Amt,product_details=product_det,category=cartegory,image=Product_img,add_by=user)
                        add_pro.save();
                        messages.success(request,request.POST['pro_name'] + " " +"Product add successfully")
                        # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
                        return redirect('staff')
                  elif 'Key6' in request.POST.keys() and request.POST['Key6']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        key4=request.POST['Key4']
                        Value4=request.POST['Value4']
                        key5=request.POST['Key5']
                        Value5=request.POST['Value5']
                        key6=request.POST['Key6']
                        Value6=request.POST['Value6']
                        product_det={key1:Value1,key2:Value2,key3:Value3,key4:Value4,key5:Value5,key6:Value6}
                        add_pro=Shop.objects.create(Product_name=product_name,Discount_price=discounted_Amt,quantity=quantity,Actual_price=actual_Amt,product_details=product_det,category=cartegory,image=Product_img,add_by=user)
                        add_pro.save();
                        messages.success(request,request.POST['pro_name'] + " " +"Product add successfully")
                        # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
                        return redirect('staff')
                  elif 'Key5' in request.POST.keys() and request.POST['Key5']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        key4=request.POST['Key4']
                        Value4=request.POST['Value4']
                        key5=request.POST['Key5']
                        Value5=request.POST['Value5']
                        product_det={key1:Value1,key2:Value2,key3:Value3,key4:Value4,key5:Value5}
                        add_pro=Shop.objects.create(Product_name=product_name,Discount_price=discounted_Amt,quantity=quantity,Actual_price=actual_Amt,product_details=product_det,category=cartegory,image=Product_img,add_by=user)
                        add_pro.save();
                        messages.success(request,request.POST['pro_name'] + " " +"Product add successfully")
                        # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
                        return redirect('staff') 
                  elif 'Key4' in request.POST.keys() and request.POST['Key4']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        key4=request.POST['Key4']
                        Value4=request.POST['Value4']
                        product_det={key1:Value1,key2:Value2,key3:Value3,key4:Value4}
                        add_pro=Shop.objects.create(Product_name=product_name,Discount_price=discounted_Amt,quantity=quantity,Actual_price=actual_Amt,product_details=product_det,category=cartegory,image=Product_img,add_by=user)
                        add_pro.save();
                        messages.success(request,request.POST['pro_name'] + " " +"Product add successfully")
                        # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
                        return redirect('staff') 
                  elif 'Key3' in request.POST.keys() and request.POST['Key3']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        product_det={key1:Value1,key2:Value2,key3:Value3}
                        add_pro=Shop.objects.create(Product_name=product_name,Discount_price=discounted_Amt,quantity=quantity,Actual_price=actual_Amt,product_details=product_det,category=cartegory,image=Product_img,add_by=user)
                        add_pro.save();
                        messages.success(request,request.POST['pro_name'] + " " +"Product add successfully")
                        # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
                        return redirect('staff') 
                  elif 'Key2' in request.POST.keys() and request.POST['Key2']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        product_det={key1:Value1,key2:Value2}
                        add_pro=Shop.objects.create(Product_name=product_name,Discount_price=discounted_Amt,quantity=quantity,Actual_price=actual_Amt,product_details=product_det,category=cartegory,image=Product_img,add_by=user)
                        add_pro.save();
                        messages.success(request,request.POST['pro_name'] + " " +"Product add successfully")
                        # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
                        return redirect('staff') 
                  else:
                        product_det={key1:Value1}
                        add_pro=Shop.objects.create(Product_name=product_name,Discount_price=discounted_Amt,quantity=quantity,Actual_price=actual_Amt,product_details=product_det,category=cartegory,image=Product_img,add_by=user)
                        add_pro.save();
                        messages.success(request,request.POST['pro_name'] + " " +"Product add successfully")
                        # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
                        return redirect('staff') 
            except Exception as e:
                  return render(request,"grading_template/staffhome.html",{'error':e})
      return redirect('/')
    return redirect('/')


def delete_product(request,id):
    if 'Userid' in request.session:
        dele_product=Shop.objects.get(id=id)
        dele_product.delete()
        Product_name=dele_product. Product_name
        messages.success(request, Product_name+ " " +"Product Deleted successfully")
        return redirect('staff')
    return redirect('/')

def edit_product(request):
      if 'Userid' in request.session:
           if request.method == "POST":
                update_shop=Shop.objects.get(id=request.POST['id'])
                update_shop.Product_name=request.POST['Product_name']
                update_shop.Discount_price=request.POST['Discout_amt']
                update_shop.Actual_price=request.POST['Actual_amt']
                update_shop.quantity=request.POST['Product_quantity']
                key1=request.POST['Key1']
                Value1=request.POST['Value1']
                instace_of_category=Shop_categories.objects.get(id=request.POST['Category'])
                update_shop.category=instace_of_category
                try:
                  if len(request.FILES) !=0:
                        Product_img=request.FILES['Pro_img']
                        update_shop.image=Product_img
                  if 'Key7' in request.POST.keys() and request.POST['Key7']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        key4=request.POST['Key4']
                        Value4=request.POST['Value4']
                        key5=request.POST['Key5']
                        Value5=request.POST['Value5']
                        key6=request.POST['Key6']
                        Value6=request.POST['Value6']
                        key7=request.POST['Key7']
                        Value7=request.POST['Value7']
                        update_shop.product_details={key1:Value1,key2:Value2,key3:Value3,key4:Value4,key5:Value5,key6:Value6,key7:Value7}
                        update_shop.save();
                        messages.success(request,request.POST['Product_name'] + " " +"Product Updated successfully")
                        return redirect('staff')
                  elif 'Key6' in request.POST.keys() and request.POST['Key6']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        key4=request.POST['Key4']
                        Value4=request.POST['Value4']
                        key5=request.POST['Key5']
                        Value5=request.POST['Value5']
                        key6=request.POST['Key6']
                        Value6=request.POST['Value6']
                        update_shop.product_details={key1:Value1,key2:Value2,key3:Value3,key4:Value4,key5:Value5,key6:Value6}
                        update_shop.save();
                        messages.success(request,request.POST['Product_name'] + " " +"Product Updated successfully")
                        return redirect('staff')
                  elif 'Key5' in request.POST.keys() and request.POST['Key5']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        key4=request.POST['Key4']
                        Value4=request.POST['Value4']
                        key5=request.POST['Key5']
                        Value5=request.POST['Value5']
                        update_shop.product_details={key1:Value1,key2:Value2,key3:Value3,key4:Value4,key5:Value5}
                        update_shop.save();
                        messages.success(request,request.POST['Product_name'] + " " +"Product Updated successfully")
                        return redirect('staff')
                  elif 'Key4' in request.POST.keys() and request.POST['Key4']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        key4=request.POST['Key4']
                        Value4=request.POST['Value4']
                        update_shop.product_details={key1:Value1,key2:Value2,key3:Value3,key4:Value4}
                        update_shop.save();
                        messages.success(request,request.POST['Product_name'] + " " +"Product Updated successfully")
                        return redirect('staff')
                  elif 'Key3' in request.POST.keys() and request.POST['Key3']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        key3=request.POST['Key3']
                        Value3=request.POST['Value3']
                        update_shop.product_details={key1:Value1,key2:Value2,key3:Value3}
                        update_shop.save();
                        messages.success(request,request.POST['Product_name'] + " " +"Product Updated successfully")
                        return redirect('staff')
                  elif 'Key2' in request.POST.keys() and request.POST['Key2']:
                        key2=request.POST['Key2']
                        Value2=request.POST['Value2']
                        update_shop.product_details={key1:Value1,key2:Value2}
                        update_shop.save();
                        messages.success(request,request.POST['Product_name'] + " " +"Product Updated successfully")
                        return redirect('staff')
                  else:
                        update_shop.product_details={key1:Value1}
                        update_shop.save();
                        messages.success(request,request.POST['Product_name'] + " " +"Product Updated successfully")
                        return redirect('staff')
                except:
                  return redirect('/')
      return redirect('/')


def shop_detail(request,id):
    if 'Userid' in request.session:
        user_id=request.session['Userid']
        User=Account.objects.filter(id=user_id).values()
        username=User[0]["First_name"]
        print(user_id)
        product=Shop.objects.get(id=id)
        pro_det=Shop.objects.filter(id=id).values()
        # print(id)
        # print(pro_det[0])
        added_pro=Shop.objects.select_related().all()
        Category=Shop_categories.objects.all()
        return render(request,"shop_detail.html",{"addedpro":added_pro,"product":product,"pro_det":pro_det,'loginName':username,'Login_Database_url':'Login_Database','Login_shop_url':'Login_shop','Login_submission_url':'Login_submission','Login_contacts_url':'Login_contacts','home_login_url':"Home_after_login",'Login_shop_cart_url':'Login_cart'})
    else:
        product=Shop.objects.get(id=id)
        pro_det=Shop.objects.filter(id=id).values()
        # print(id)
        print(pro_det[0])
        added_pro=Shop.objects.select_related().all()
        Category=Shop_categories.objects.all()
        return render(request,"shop_detail.html",{"addedpro":added_pro,"product":product,"pro_det":pro_det})
    
      
def shop_cart_after_login(request):
    if 'Userid' in request.session:
        userid=request.session['Userid']
        User=Account.objects.filter(id=userid).values()
        username=User[0]["First_name"]
        print(username)
        print(userid)
        return render(request,'shop_cart.html',{'loginName':username,'Login_Database_url':'Login_Database','Login_shop_url':'Login_shop','Login_submission_url':'Login_submission','Login_contacts_url':'Login_contacts','home_login_url':"Home_after_login",'Login_shop_cart_url':'Login_cart'})
    else:
         messages.success(request,'Please Login Here....')
         return redirect('login')
    