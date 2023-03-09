from django.shortcuts import render,redirect
from .models import Card
from django.contrib.sessions.models import Session
from Account.models import Account
from django.contrib import messages
from Shop.models import Shop_categories


# Create your views here.

def Add_Graded_card(request):
    if 'Userid' in request.session:
        if request.method == "POST":
            user_id=request.session['Userid']
            C_name=request.POST['c_name']
            nfc_no=request.POST['NFC_No']
            card_no=request.POST['Card_no']
            rareity=request.POST['reaety']
            year=request.POST['year']
            series=request.POST['series']
            game=request.POST['Game']
            overall_grade=request.POST['overal_grade']
            certering=request.POST['centering']
            surface=request.POST['surface']
            edges=request.POST['edges']
            corner=request.POST['corner']
            note=request.POST['Note']
            if 'Shop' in request.POST.keys() and request.POST['Shop']:
                Shop=True
            else:
                Shop=False
            id=request.session['Userid']
            user=Account.objects.get(id=id)
            try: 
                    if len(request.FILES) !=0:
                        Card_img=request.FILES['Card_img']
                    if 'Card_img' in request.FILES.keys() and request.FILES['Card_img']:
                        card=Card.objects.create(NFC_No=nfc_no,Card_Name=C_name,Card_No=card_no,Rarity=rareity,Year=year,Series=series,Game=game,Overall_Grade=overall_grade,Centering=certering,Surface=surface,Edges=edges,Corners=corner,Notes=note,Image=Card_img,shop=Shop,add_by=user)
                        card.save();
                    else:
                        card=Card.objects.create(NFC_No=nfc_no,Card_Name=C_name,Card_No=card_no,Rarity=rareity,Year=year,Series=series,Game=game,Overall_Grade=overall_grade,Centering=certering,Surface=surface,Edges=edges,Corners=corner,Notes=note,shop=Shop,add_by=user)
                        card.save();
                    all_cards=Card.objects.all()
                    obj_fil=Account.objects.filter(id=user_id).values()
                    username=obj_fil[0]["First_name"]
                    if obj_fil[0]['is_admin']==True:
                        modrater_type="Admin"
                    else:
                        modrater_type="Staff"
                    messages.success(request,C_name + " " +"Card add successfully")
                    Category=Shop_categories.objects.all()
                    # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
                    return redirect('staff')
            except Exception as e:
                    return render(request,"grading_template/staffhome.html",{'suss':'xyz','error':e})
        return redirect('/')
    return redirect('/')


def delete_card(request,id):
    if 'Userid' in request.session:
        user_id=request.session['Userid']
        dele_card=Card.objects.get(id=id)
        all_cards=Card.objects.all()
        obj_fil=Account.objects.filter(id=user_id).values()
        username=obj_fil[0]["First_name"]
        if obj_fil[0]['is_admin']==True:
            modrater_type="Admin"
        else:
            modrater_type="Staff"
        dele_card.delete()
        C_name=dele_card.Card_Name
        messages.success(request,C_name + " " +"Card Deleted successfully")
        Category=Shop_categories.objects.all()
        # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
        return redirect('staff')
    return redirect('/')


def Edit_Card(request):
    if 'Userid' in request.session:
        if request.method =='POST':
            user_id=request.session['Userid']
            id=request.POST['id']
            Ed_card=Card.objects.get(id=id)
            Ed_card.Card_Name=request.POST['c_name']
            Ed_card.NFC_No=request.POST['NFC_No']
            Ed_card.Card_No=request.POST['Card_no']
            Ed_card.Rarity=request.POST['reaety']
            Ed_card.Year=request.POST['year']
            Ed_card.Series=request.POST['series']
            Ed_card.Game=request.POST['Game']
            Ed_card.Overall_Grade=request.POST['overal_grade']
            Ed_card.Centering=request.POST['centering']
            Ed_card.Surface=request.POST['surface']
            Ed_card.Edges=request.POST['edges']
            Ed_card.Corners=request.POST['corner']
            Ed_card.Notes=request.POST['Note']
            if 'Shop' in request.POST.keys() and request.POST['Shop']:
                Shop=True
            else:
                Shop=False
            Ed_card.shop=Shop
            if len(request.FILES) !=0:
                Ed_card.Image=request.FILES['Card_img']
            Ed_card.save();
            all_cards=Card.objects.all()
            obj_fil=Account.objects.filter(id=user_id).values()
            username=obj_fil[0]["First_name"]
            if obj_fil[0]['is_admin']==True:
                modrater_type="Admin"
            else:
                modrater_type="Staff"
            messages.success(request,request.POST['c_name'] + " " +"Card Update successfully")
            Category=Shop_categories.objects.all()
            # return render(request,"grading_template/staffhome.html",{'suss':'xyz',"Cards":all_cards,'loginName':username,'moderTy':modrater_type,'cate':Category})
            return redirect('staff')
        return redirect('/')
    return redirect('/')






