from django.urls import path, include  
from . import views
urlpatterns = [
    path('', views.home, name="home") ,
    path('products/', views.products, name="products"),  
    path('products/newform/', views.new_product_form, name="new_product_form"),      
    path('products/create_product', views.create_product, name = "create_product"),
    path('products/view/<int:id>', views.view_product, name = "view_product"),
    path('suppliers/', views.suppliers, name="suppliers"),
    path('suppliers/newform/', views.new_supplier_form, name = "new_supplier_form"),
    path('suppliers/create_supplier', views.create_supplier, name = "create_supplier"),
    path('test/', views.test, name="test") #para pruebas en desarrollo
]