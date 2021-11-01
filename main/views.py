from django.shortcuts import render

from .models import Contacts

# Страницы
from .models import PageHome
from .models import PageContacts
from .models import PageAboutСompany
from .models import PagePhotoGallery
from .models import PageDocument

def home(request):

    contacts = Contacts.objects.all().first()
    companys = PageAboutСompany.objects.all().first()

    pageHome = PageHome.objects.all().first()


    context = {
        'contacts': contacts,
        'companys': companys,

        'pageHome': pageHome,
    }

    return render(request, 'home/home.html', context)

def contacts(request):

    contacts = Contacts.objects.all().first()
    companys = PageAboutСompany.objects.all().first()

    pageContacts = PageContacts.objects.all().first()


    context = {
        'contacts': contacts,
        'companys': companys,

        'pageContacts': pageContacts,
    }

    return render(request, 'contacts/contacts.html', context)

def aboutCompany(request):

    contacts = Contacts.objects.all().first()
    companys = PageAboutСompany.objects.all().first()

    pageAboutСompany = PageAboutСompany.objects.all().first()

    context = {
        'contacts': contacts,
        'companys': companys,

        'pageAboutСompany': pageAboutСompany,
    }

    return render(request, 'about-company/about-company.html', context)

def photoGallery(request):

    contacts = Contacts.objects.all().first()
    companys = PageAboutСompany.objects.all().first()

    pagePhotoGallery = PagePhotoGallery.objects.all().first()

    context = {
        'contacts': contacts,
        'companys': companys,

        'pagePhotoGallery': pagePhotoGallery,
    }

    return render(request, 'photo-gallery/photo-gallery.html', context)

def documents(request):
    contacts = Contacts.objects.all().first()
    companys = PageAboutСompany.objects.all().first()

    documents = PageDocument.objects.all()

    context = {
        'contacts': contacts,
        'companys': companys,

        'documents': documents,
    }

    return render(request, 'documents/documents.html', context)

def documentDetail(request, id):
    contacts = Contacts.objects.all().first()
    companys = PageAboutСompany.objects.all().first()

    document = PageDocument.objects.get(pk=id)

    context = {
        'contacts': contacts,
        'companys': companys,

        'document': document,
    }

    return render(request, 'document-detail/document-detail.html', context)
