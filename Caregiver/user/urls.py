from django.urls import path
from Administrator import views
from Parent import *
 
app_name="Administrator"
 
urlpatterns = [
    #DISTRICT
    path('District/',views.district,name="District"),
    path('deldis/<int:did>',views.deldis,name="deldis"),
    path('editdis/<int:eid>',views.editdis,name="editdis"),
 
    #CATEGORY
    path('Category/',views.category,name="Category"),
    path('delcate/<int:cid>',views.delcat,name="delcat"),
    path('editcat/<int:eid>',views.editcat,name="editcat"),
 
    #PLACE
    path('Place/',views.place,name="Place"),
    path('delplc/<int:pid>',views.delplc,name="delplc"),
    path('editplc/<int:eid>',views.editplc,name="editplc"),
 
   
    #SUBCATEGORY
    path('subcat/',views.subcat,name="subcat"),
    path('delsubcat/<int:dsub>',views.delsubcat,name="delsubcat"),
    path('editsubcat/<int:esub>',views.editsubcat,name="editsubcat"),


 #ADMINREG
    path('AdminRegistration/',views.adminreg,name="AdminRegistration"),
 
    path('Homepage/',views.homepage,name="homepage"),
   
    path('adprofile/',views.adprofile,name='adprofile'),
    path('viewusers/',views.viewusers,name='viewusers'),
    path('accpetuser/<int:accid>',views.accpetuser,name='accpetuser'),
    path('rejectuser/<int:rejid>',views.rejectuser,name='rejectuser'),
    

    #PARENTVIEW

    path('viewparents/',views.viewparents,name='viewparents'),
    path('accpetparent/<int:accid>',views.accpetparent,name='accpetparent'),
    path('rejectparent/<int:rejid>',views.rejectparent,name='rejectparent'),


    #CAREGIVERVIEW

     path('viewcaregivers/',views.viewcaregivers,name='viewcaregivers'),
    path('accpetcaregiver/<int:accid>',views.accpetcaregiver,name='accpetcaregiver'),
    path('rejectcaregiver/<int:rejid>',views.rejectcaregiver,name='rejectcaregiver'),
]
 