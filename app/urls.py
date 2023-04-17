from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.erp,name='erp'),
    path('home/',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('subproducts/<str:type>',views.subproducts,name='subproducts'),
    path('productdescription/<int:id>',views.productdescription,name='productdescription'),
    path('projects/',views.project,name='projects'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),

] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)