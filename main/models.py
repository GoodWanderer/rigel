from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=200, unique=True, verbose_name='Название')
#     slug = models.SlugField(unique=True)
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name


class Contacts(models.Model):
    phone1 = models.CharField(max_length=30, verbose_name='Телефон-1', blank=False)
    phone2 = models.CharField(max_length=30, verbose_name='Телефон-2', blank=False)
    mail = models.EmailField(verbose_name='Почта', blank=False)
    fb = models.URLField(verbose_name='Ссылка на facebook', blank=False)
    inst = models.URLField(verbose_name='Ссылка на instagram', blank=False)
    google = models.URLField(verbose_name='Ссылка на google', blank=False)

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'

    def __str__(self):
        return 'Контактные данные'


# Страница - Главная
class PageHome(models.Model):

    mission = models.TextField(max_length=3000, verbose_name='Описание миссии', blank=False)

    class Meta:
        verbose_name = 'Страница - Главная'
        verbose_name_plural = 'Страница - Главная'

    def __str__(self):
        return 'Страница - Главная'

class PageHomeSlider(models.Model):
    img = models.ImageField(upload_to='slider/', verbose_name='Изображение слайдера')
    pageHome = models.ForeignKey('pageHome', on_delete=models.CASCADE, related_name='homeSlider')

    class Meta:
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'

    def __str__(self):
        return 'Слайдер'

class PageHomeAccordion(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название', blank=False)
    description = models.TextField(max_length=3000, verbose_name='Описание', blank=False)
    pageHome = models.ForeignKey('pageHome', on_delete=models.CASCADE, related_name='homeAccordion')

    class Meta:
        verbose_name = 'Аккордеон'
        verbose_name_plural = 'Аккордеон'

    def __str__(self):
        return 'Аккордеон'

# Страница Контакты
class PageContacts(models.Model):
    address_office = models.CharField(max_length=500, verbose_name='Адрес офиса', blank=False)
    address_legal = models.TextField(max_length=500, verbose_name='Юридический адрес', blank=False)
    fax = models.CharField(max_length=30, verbose_name='Факс', blank=False)
    class Meta:
        verbose_name = 'Страница - Контакты'
        verbose_name_plural = 'Страница - Контакты'

    def __str__(self):
        return 'Страница - Контакты'


class PageContactsPeople(models.Model):
    name = models.CharField(max_length=300, verbose_name='Имя', blank=True)
    post = models.CharField(max_length=300, verbose_name='Должность', blank=True)
    phone = models.CharField(max_length=30, verbose_name='Телефон', blank=True)
    mail1 = models.EmailField(verbose_name='Почта-1', blank=True)
    mail2 = models.EmailField(verbose_name='Почта-2', blank=True)
    pageContacts = models.ForeignKey('pageContacts', on_delete=models.CASCADE, related_name='contactsPeople')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return 'Сотрудник'

# Страница О компании
class PageAboutСompany(models.Model):
    text = models.TextField(max_length=5000, verbose_name='Текст о компании', blank=False)

    class Meta:
        verbose_name = 'Страница - О компании'
        verbose_name_plural = 'Страница - О компании'

    def __str__(self):
        return 'Страница - О компании'


class PageAboutСompanyOther(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название', blank=True)
    description = models.TextField(max_length=5000, verbose_name='Название', blank=True)

    pageAboutСompany = models.ForeignKey('pageAboutСompany', on_delete=models.CASCADE, related_name='aboutСompany')

    class Meta:
        verbose_name = 'Другая компания'
        verbose_name_plural = 'Другие компании'

    def __str__(self):
        return 'Другие компании'

# Страница фотогаллереи
class PagePhotoGallery(models.Model):

    class Meta:
        verbose_name = 'Страница - Фотогалерея'
        verbose_name_plural = 'Страница - Фотогалерея'

    def __str__(self):
        return 'Страница - Фотогалерея'


class PagePhotoGalleryAuto(models.Model):
    img1 = models.ImageField(upload_to='gallery-auto/', verbose_name='Изображене автогаллереи 1')
    img2 = models.ImageField(upload_to='gallery-auto/', verbose_name='Изображене автогаллереи 2')
    pagePhotoGalleryAuto = models.ForeignKey('pagePhotoGallery', on_delete=models.CASCADE, related_name='galleryAuto')
    class Meta:
        verbose_name = 'Изображение автотранспорта'
        verbose_name_plural = 'Изображения автотранспорта'

    def __str__(self):
        return 'Изображение автотранспорта'


class PagePhotoGalleryProject(models.Model):
    img1 = models.ImageField(upload_to='gallery-project/', default='default.jpg', verbose_name='Изображене проекта 1')
    img2 = models.ImageField(upload_to='gallery-project/', default='default.jpg', verbose_name='Изображене проекта 2')
    pagePhotoGalleryProject = models.ForeignKey('pagePhotoGallery', on_delete=models.CASCADE, related_name='galleryProject')
    class Meta:
        verbose_name = 'Изображение проекта'
        verbose_name_plural = 'Изображения проектов'

    def __str__(self):
        return 'Изображение проекта'


# Страница Документов
class PageDocument(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название', blank=True)
    company_choise = (
        ("Rigel-Z", "Rigel-Z"),
        ("ROSTERMINĀLS", "ROSTERMINĀLS"),
        ("STRAUME", "STRAUME"),
    )
    company = models.CharField(max_length=30, choices=company_choise, default="Rigel-Z", verbose_name='Компания')
    pdf = models.FileField(upload_to='pdf/', verbose_name='PDF')
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name

class PageDocumentImg(models.Model):
    img = models.ImageField(upload_to='document-img/', verbose_name='Изображение')
    pageDocumentImg = models.ForeignKey('PageDocument', on_delete=models.CASCADE, related_name='documentImg')
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return 'Изображение'

