from django.urls import path
from .views import home, contacts, aboutCompany, photoGallery
from .views import documents, documentDetail

urlpatterns = [
    path('', home, name='home'),

    path('documents/', documents, name='documents'),
    path('document-detail/<int:id>/', documentDetail, name="documentDetail"),

    path('photo-gallery/', photoGallery, name='photoGallery'),
    path('about-company/', aboutCompany, name='aboutCompany'),
    path('contacts/', contacts, name='contacts')
]


