from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Contacts

from .models import PageHome, PageHomeAccordion, PageHomeSlider
from .models import PageContacts, PageContactsPeople
from .models import PageAboutСompany, PageAboutСompanyOther
from .models import PagePhotoGallery, PagePhotoGalleryAuto, PagePhotoGalleryProject
from .models import PageDocument, PageDocumentImg


@admin.register(Contacts)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

# К стрницам
class PageHomeAccordionInline(admin.TabularInline):
    fk_name = 'pageHome'
    model = PageHomeAccordion

class PageHomeSliderInline(admin.TabularInline):
    fk_name = 'pageHome'
    model = PageHomeSlider



class PageContactsPeopleInline(admin.TabularInline):
    fk_name = 'pageContacts'
    model = PageContactsPeople

class PageAboutСompanyOtherInline(admin.TabularInline):
    fk_name = 'pageAboutСompany'
    model = PageAboutСompanyOther



class PagePhotoGalleryAutoInline(admin.TabularInline):
    fk_name = 'pagePhotoGalleryAuto'
    model = PagePhotoGalleryAuto

class PagePhotoGalleryProjectInline(admin.TabularInline):
    fk_name = 'pagePhotoGalleryProject'
    model = PagePhotoGalleryProject



class PageDocumentImgInline(admin.TabularInline):
    fk_name = 'pageDocumentImg'
    model = PageDocumentImg

# Стриницы
@admin.register(PageHome)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    inlines = [PageHomeAccordionInline, PageHomeSliderInline]

@admin.register(PageContacts)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    inlines = [PageContactsPeopleInline,]

@admin.register(PageAboutСompany)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    inlines = [PageAboutСompanyOtherInline,]

@admin.register(PagePhotoGallery)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    inlines = [PagePhotoGalleryAutoInline, PagePhotoGalleryProjectInline]

@admin.register(PageDocument)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    inlines = [PageDocumentImgInline,]
