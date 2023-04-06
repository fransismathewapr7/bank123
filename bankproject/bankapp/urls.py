from . import views
from django.urls import path
app_name="bankapp"
urlpatterns = [

    path('',views.demo,name='demo'),
    path('student-form/', views.student_form, name='student_form'),
    path('odercom/', views.odercom, name='odercom'),

]