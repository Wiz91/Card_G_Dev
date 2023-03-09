from django.contrib import admin
from django.urls import path
from Account import views
from Grading import views as grading
from Shop import views as shop
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.masterpage,name="masterpage"),
    path('',views.Landing_page,name="Landing_page"),
    path('db',views.Database_page,name="db"),
    path('Sup',views.Sinup_page,name="Sin_Up"),
    path('homepage',views.homepage,name="homepage"),
    path('Login',views.Login,name="login"),
    path('contact',views.Contect_page,name="contact"),
    path('sub',views.Submission_page,name='sub'),
    path('Shop_new',views.Shop_new,name="shop"),
    path('reg',views.registration,name="reg"),
    path('PLogin',views.Perform_Login,name="plogin"),
    path('Logout',views.Logout,name="logout"),
    path('Login_shop',views.Shop_after_login,name="login_shop"),
    path('Login_Database',views.Database_after_login,name="login_db"),
    path('Login_submission',views.submission_after_login,name="login_sub"),
    path('Login_contacts',views.contacts_after_login,name="login_contact"),
    path('Home_after_login',views.After_login_home,name="login_home"),
    path('add_graded_card',grading.Add_Graded_card,name="add_graded_card"),
    path('del/<int:id>',grading.delete_card,name="del_card"),
    path('del/add_graded_card',grading.Add_Graded_card),
    path('Edit_Card',grading.Edit_Card),
    path('del/Edit_Card',grading.Edit_Card),
    path('Padd',shop.add_product),
    path('dele/<int:id>',shop.delete_product),
    path('staff',views.redict_staff,name='staff'),
    path('edit_pro',shop.edit_product),
    path('shop_detail/<int:id>',shop.shop_detail,name="shop_detail"),
    path('cart',shop.shop_cart_after_login,name="cart"),  
    path('google_oauth/redirect/',views.RedirectOauthView,name="google_login"),
    path('google_oauth/callback/',views.CallbackView),
]



urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)