from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    
    path('Dashboard',views.Dashboard,name='Dashboard'),

    path('EditPermanentCustomer',views.EditPermanentCustomer,name='EditPermanentCustomer'),

    path('EditTemporaryCustomer',views.EditTemporaryCustomer,name='EditTemporaryCustomer'),

    path('ExistingCustomer',views.ExistingCustomer,name='ExistingCustomer'),

    path('NormalBill',views.NormalBill,name='NormalBill'),

    path('EvaluateNormalBill',views.EvaluateNormalBill,name='EvaluateNormalBill'),
    
    path('DcBill',views.DcBill,name='DcBill'),

    path('EvaluateDcBill',views.EvaluateDcBill,name='EvaluateDcBill'),
    
    path('GstBill',views.GstBill,name='GstBill'),

    path('EvaluateGstBill',views.EvaluateGstBill,name='EvaluateGstBill'),

    path('AddCustomer',views.AddCustomer,name='AddCustomer'),

    path('DeleteAccount',views.DeleteAccount,name='DeleteAccount'),

    path('SearchByBillno',views.SearchByBillno,name='SearchByBillno'),

    path('SearchByCylinderno',views.SearchByCylinderno,name='SearchByCylinderno'),

    path('SearchByDate',views.SearchByDate,name='SearchByDate'),

    path('SearchByCustomer',views.SearchByCustomer,name='SearchByCustomer'),

]