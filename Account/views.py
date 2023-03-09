from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Account
from django.contrib.auth import authenticate,logout
from .import models
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from Grading import views as grading
from django.contrib import messages
from Grading.models import Card
from Shop.models import Shop_categories,Shop
from django.utils import timezone
import google_apis_oauth
from CardG.settings import JSON_FILEPATH,SCOPES,REDIRECT_URI
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
import google_apis_oauth
from googleapiclient.discovery import build

def masterpage(request):
    return render(request,"masterpage.html")

def Landing_page(request):
    return render(request,"Landing.html")

def Database_page(request):
    return render (request, "Database.html")

def Sinup_page(request):
   return render (request, "Sinup.html")

def homepage(request):
    return render (request,'homepage.html')

def Login(request):
    return render(request,'Login.html')

def Contect_page(request):
    return render(request,'contacts.html')

def Submission_page(request):
    return render(request,'submission.html')

def Shop_new(request):
    added_pro=Shop.objects.select_related().all()
    return render(request,"Shop_new.html",{"addedpro":added_pro}) 
    
def registration(request):
    if request.method=="POST":
        eml=request.POST['email']
        Fname=request.POST['First_N']
        Lname=request.POST['Last_N']
        Contect=request.POST['contact']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        Location=request.POST['Location']
        pin=request.POST['pin']
        try:
            if pass1!=pass2:
                raise Exception("Password doesn't match!")
            user=Account.objects.create_user(email=eml,First_name=Fname,Last_name=Lname,contact=Contect,password=pass1,password2=pass2,tc=True,pin=pin,Location=Location)
            user.save();
            messages.success(request,'Registered Succesfully, Now you can Login Here....')
            return render( request,"Landing.html")
        except Exception as e:
            return render(request,"Sinup.html",{'error':e})
    return redirect('/')

def Perform_Login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass']
        user=authenticate(email=email,password=password)
        if user==None:
            return render (request,"Login.html",{'error':'Please check your email Id or password'})
        user.last_login=timezone.now()
        print(user.last_login)
        user.save();
        obj_fil=Account.objects.filter(email=email).values()
        username=obj_fil[0]["First_name"]
        request.session['Userid']=obj_fil[0]['id'] 
        if obj_fil[0]['Is_staff']==True or obj_fil[0]["is_admin"]==True:  
            return redirect('staff')
        return render(request,'masterpage.html',{'loginName':username,'Login_shop_url':'Login_shop','Login_Database_url':'Login_Database','Login_submission_url':'Login_submission','Login_contacts_url':'Login_contacts','home_login_url':"Home_after_login",'Login_shop_cart_url':'Login_cart'})
    return redirect('/')

def After_login_home(request):
    if 'Userid' in request.session:
        userid=request.session['Userid']
        User=Account.objects.filter(id=userid).values()
        username=User[0]["First_name"]
        return render(request,'masterpage.html',{'loginName':username,'Login_shop_url':'Login_shop','Login_Database_url':'Login_Database','Login_submission_url':'Login_submission','Login_contacts_url':'Login_contacts','home_login_url':"Home_after_login",'Login_shop_cart_url':'Login_cart'})


def RedirectOauthView(request):
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    
    return HttpResponseRedirect(oauth_url)

def CallbackView(request):
    try:

        # Get user credentials
        credentials = google_apis_oauth.get_crendentials_from_callback(
            request,
            JSON_FILEPATH,
            SCOPES,
            REDIRECT_URI
        )
        
        user_info_service = build('oauth2', 'v2', credentials=credentials)
        user_info = user_info_service.userinfo().get().execute()
        print(user_info['email'])
        print('name: ',user_info['name'])
        name=user_info['name']
        email=user_info['email']
        l_name=name.split()
        user=Account.objects.create(email=email,First_name=l_name[0],Last_name=l_name[1],contact="",password="",tc=True,pin="",Location="")
        user.save();
        obj_fil=Account.objects.filter(email=email).values()
        request.session['Userid']=obj_fil[0]['id'] 
        messages.success(request,"Wellcome" + " " + l_name[0]+" "+"enjoye our card garding servise")
        return redirect('login_home')
    except Exception as e:
        print(e)
        return redirect("/") 
    



def Shop_after_login(request):
    if 'Userid' in request.session:
        userid=request.session['Userid']
        User=Account.objects.filter(id=userid).values()
        username=User[0]["First_name"]
        added_pro=Shop.objects.select_related().all()
        return render(request,'Shop_new.html',{"addedpro":added_pro,'loginName':username,'Login_shop_url':'Login_shop','Login_Database_url':'Login_Database','Login_submission_url':'Login_submission','Login_contacts_url':'Login_contacts','home_login_url':"Home_after_login",'Login_shop_cart_url':'Login_cart'})
    return redirect('/')

def Database_after_login(request):
    if 'Userid' in request.session:
        userid=request.session['Userid']
        User=Account.objects.filter(id=userid).values()
        username=User[0]["First_name"]
        return render(request,'Database.html',{'loginName':username,'Login_Database_url':'Login_Database','Login_shop_url':'Login_shop','Login_submission_url':'Login_submission','Login_contacts_url':'Login_contacts','home_login_url':"Home_after_login",'Login_shop_cart_url':'Login_cart'})
    return redirect('/')

def submission_after_login(request):
    if 'Userid' in request.session:
        userid=request.session['Userid']
        User=Account.objects.filter(id=userid).values()
        username=User[0]["First_name"]
        return render(request,'submission.html',{'loginName':username,'Login_Database_url':'Login_Database','Login_shop_url':'Login_shop','Login_submission_url':'Login_submission','Login_contacts_url':'Login_contacts','home_login_url':"Home_after_login",'Login_shop_cart_url':'Login_cart'})
    return redirect('/')

def contacts_after_login(request):
    if 'Userid' in request.session:
        userid=request.session['Userid']
        User=Account.objects.filter(id=userid).values()
        username=User[0]["First_name"]
        print(userid)
        return render(request,'contacts.html',{'loginName':username,'Login_Database_url':'Login_Database','Login_shop_url':'Login_shop','Login_submission_url':'Login_submission','Login_contacts_url':'Login_contacts','home_login_url':"Home_after_login",'Login_shop_cart_url':'Login_cart'})
    

def Logout(request):
    # auth.logout(request)
    if "Userid" in request.session.keys():
        del request.session["Userid"]
        auth.logout(request)
        return redirect('/')


def redict_staff(request):
    user_id=request.session['Userid']
    all_cards=Card.objects.all()
    obj_fil=Account.objects.filter(id=user_id).values()
    username=obj_fil[0]["First_name"]
    if obj_fil[0]['is_admin']==True:
        modrater_type="Admin"
    else:
        modrater_type="Staff"
    Category=Shop_categories.objects.all()
    added_pro=Shop.objects.select_related().all()
    return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,"addedpro":added_pro,'loginName':username,'moderTy':modrater_type,'cate':Category})


