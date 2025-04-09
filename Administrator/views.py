
from django.shortcuts import render,redirect
import Administrator
from Administrator.models import *
from Guest.models import *
from Parent.models import*
from Caregiver.models import*

# Create your views here.
def district(request):
    disdata=tbl_district.objects.all().order_by('district_name')
    if request.method=='POST':
        districtname=request.POST.get('txtdist')
        tbl_district.objects.create(district_name=districtname)
        return render(request,'Administrator/District.html',{'msg':"Inserted"})
    else:
        return render(request,'Administrator/District.html',{'dis':disdata})
 
def editdis(request,eid):
    disdata=tbl_district.objects.all()
    data=tbl_district.objects.get(id=eid)
    if request.method=='POST':
        districtname=request.POST.get('txtdist')
        data.district_name=districtname
        data.save()
        return render(request,'Administrator/District.html',{'msg':"Updated"})
    return render(request,'Administrator/District.html',{'dis':disdata,'data':data})
 
def deldis(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Administrator/District.html',{'msg':"Deleted"})
    # return redirect('Administrator:District')
 
 
def category(request):
    catdata=tbl_category.objects.all()
    if request.method=='POST':
        categoryname=request.POST.get('txtcategory')
        tbl_category.objects.create(category_name=categoryname,category_salary=request.POST.get("txtcatsal"))
        return render(request,'Administrator/Category.html',{'msg':"Inserted"})
    else:
        return render(request,'Administrator/Category.html',{'cat':catdata})
 
from django.shortcuts import render, redirect, get_object_or_404
from Administrator.models import tbl_category

def editcat(request, eid):
    catdata = tbl_category.objects.all()
    data = get_object_or_404(tbl_category, id=eid)  

    if request.method == 'POST':
        categoryname = request.POST.get('txtcategory')
        categorysalary = request.POST.get('txtcatsal')

        if categoryname and categorysalary: 
            data.category_name = categoryname
            try:
                data.category_salary = float(categorysalary) 
                data.save()
                return redirect("Administrator:Category") 
            except ValueError:
                return render(request, 'Administrator/Category.html', {
                    'msg': "Invalid salary value!", 'cat': catdata, 'data': data
                })

    return render(request, 'Administrator/Category.html', {'cat': catdata, 'data': data})

 
def delcat(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return render(request,'Administrator/Category.html',{'msg':"Deleted"})
    # return redirect('Administrator:Category')
 
 
def place(request):
    disdata=tbl_district.objects.all()
    data=tbl_place.objects.all().order_by('district__district_name')
    if request.method=='POST':
        placename=request.POST.get('txtplace')
        pin=request.POST.get('txtpin')
        districtid=tbl_district.objects.get(id=request.POST.get('ddlDist'))

        placedata=tbl_place.objects.filter(district=districtid)

        tbl_place.objects.create(place_name=placename,place_pincode=pin,district=districtid)
        return render(request,'Administrator/Place.html',{'plc':placedata,'dis':disdata})
    else:
        return render(request,'Administrator/Place.html',{'dis':disdata,'plc':data})
 
def delplc(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return render(request,'Administrator/Place.html',{'msg':"Deleted"})
 
 
def editplc(request,eid):
    disdata=tbl_district.objects.all()#dropdown
    data=tbl_place.objects.get(id=eid)
    if request.method=='POST':
        district=tbl_district.objects.get(id=request.POST.get('ddlDist'))
        place=request.POST.get('txtplace')
        pin=request.POST.get('txtpin')
        data.place_name=place
        data.district=district
        data.place_pincode=pin
        data.save()
        return render(request,'Administrator/Place.html',{'msg':"Updated"})
    else:
        return render(request,'Administrator/Place.html',{'data':data,'dis':disdata})
 
 
    

def adminreg(request):
    admindata= tbl_adminreg.objects.all()
    if request.method=='POST':
        name=request.POST.get('txtname')
        contact=request.POST.get('txtnum')
        email=request.POST.get('txtemail')
        password=request.POST.get('txtpwd')
        tbl_adminreg.objects.create(name=name,contactNumber=contact,email=email,password=password)
        return render(request,'Administrator/AdminRegistration.html',{'msg':"Inserted"})
    else:
        return render(request,'Administrator/AdminRegistration.html',{'admin':admindata}) 
 
def subcat(request):
    subcatdata=tbl_subcategory.objects.all()
    catdata=tbl_category.objects.all()
    if request.method=='POST':
        subcatename=request.POST.get('txtsubcate')
        catid=tbl_category.objects.get(id=request.POST.get('ddlcategory'))
        tbl_subcategory.objects.create(subcat_name=subcatename,category=catid)
        return render(request,'Administrator/Subcategory.html',{'msg':"Inserted"})
    else:
        return render(request,'Administrator/Subcategory.html',{'subcat':subcatdata,'cat':catdata})        
    


def editsubcat(request,esub):
    
    catdata=tbl_category.objects.all()
    data=tbl_subcategory.objects.get(id=esub)
    if request.method=='POST':
       categoryname=tbl_category.objects.get(id=request.POST.get('ddlcategory'))
       subcategoryname=request.POST.get('txtsubcate')
       data.subcat_name=subcategoryname
       data.category=categoryname
       data.save()
       return render(request,'Administrator/SubCategory.html',{'msg':"Updated"})
    else:
       return render(request,'Administrator/SubCategory.html',{'data':data,'cat':catdata})

def homepage(request):
    return render(request,"Administrator/Homepage.html")



 
def delsubcat(request,dsub):
    tbl_subcategory.objects.get(id=dsub).delete()
    return render(request,'Administrator/Subcategory.html',{'msg':"Deleted"})



def adprofile(request):
    admin_id = request.session['aid']
    admin_data = tbl_adminreg.objects.get(id=admin_id)
    return render(request, 'Administrator/AdminProfile.html', {'data': admin_data})

def viewusers(request):
    newdata = tbl_user.objects.filter(user_status=0)
    accdata = tbl_user.objects.filter(user_status=1)
    rejdata = tbl_user.objects.filter(user_status=2)
    return render(request, 'Administrator/ViewUsers.html', {'data1': newdata,'data2':accdata,'data3':rejdata})

def accpetuser(request,accid):
    data=tbl_user.objects.get(id=accid)
    data.user_status=1
    data.save()
    return redirect('Administrator:viewusers')


def rejectuser(request,rejid):
    data=tbl_user.objects.get(id=rejid)
    data.user_status=2
    data.save()
    return redirect('Administrator:viewusers')


def viewparents(request):
    newdata = tbl_parent.objects.filter(parent_status=0)
    accdata = tbl_parent.objects.filter(parent_status=1)
    rejdata = tbl_parent.objects.filter(parent_status=2)
    return render(request, 'Administrator/ViewParents.html', {'data1': newdata,'data2':accdata,'data3':rejdata})

def accpetparent(request,accid):
    data=tbl_parent.objects.get(id=accid)
    data.parent_status=1
    data.save()
    return redirect('Administrator:viewparents')


def rejectparent(request,rejid):
    data=tbl_parent.objects.get(id=rejid)
    data.parent_status=2
    data.save()
    return redirect('Administrator:viewparents')



def viewcaregivers(request):
    newdata = tbl_caregiver.objects.filter(caregiver_status=0).select_related('category')
    accdata = tbl_caregiver.objects.filter(caregiver_status=1).select_related('category')
    rejdata = tbl_caregiver.objects.filter(caregiver_status=2).select_related('category')

    for caregiver in rejdata:
        caregiver.salary = caregiver.category.category_salary  # Assign category salary

    return render(request, 'Administrator/ViewCaregivers.html', {
        'data1': newdata,  # Pending caregivers
        'data2': accdata,  # Accepted caregivers
        'data3': rejdata   # Rejected caregivers
    })


def accpetcaregiver(request,accid):
    data=tbl_caregiver.objects.get(id=accid)
    data.caregiver_status=1
    data.save()
    return redirect('Administrator:viewcaregivers')


def rejectcaregiver(request,rejid):
    data=tbl_caregiver.objects.get(id=rejid)
    data.caregiver_status=2
    data.save()
    return redirect('Administrator:viewcaregivers')