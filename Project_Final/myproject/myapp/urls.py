from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('form/',views.form, name='form.html'),
    path('search/', views.search, name='search'),  # หน้าแสดงผลการค้นหา
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),  # เพิ่ม URL สำหรับการลบข้อมูล
]