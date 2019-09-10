from django.db import models

# Create your models here.
class Cards(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    text = models.TextField()
    image = models.FileField(default='hills.png', blank=True)


    def __str__(self):
        return self.title



class Website(models.Model):
    title = models.CharField(max_length=20, default='Set_Title')
    slug = models.SlugField(default='set-title')
    link_1 = models.CharField(max_length=20, default='link_1')
    link_2 = models.CharField(max_length=20, default='link_2')
    link_3 = models.CharField(max_length=20, default='link_3')
    background_image = models.FileField(default='hills.png', blank=True)
    image_service_1 = models.FileField(default='hills.png', blank=True)
    title_service_1 = models.CharField(max_length=20, default='title_service_1')
    text_service_1 = models.CharField(max_length=1000, default='text_service_1')
    image_service_2 = models.FileField(default='hills.png', blank=True)
    title_service_2 = models.CharField(max_length=20, default='title_service_2')
    text_service_2 = models.CharField(max_length=1000, default='text_service_2')
    parallax_image = models.FileField(default='hills.png', blank=True)
    link_2_title = models.CharField(max_length=1000, default='Title')
    link_2_content = models.CharField(max_length=1000, default='text_link_2')
    link_2_tab_opt_1 = models.CharField(max_length=20, default='title_tab_1')
    link_2_tab_opt_2 = models.CharField(max_length=20, default='title_tab_2')
    link_2_tab_content_1 = models.CharField(max_length=1000, default='link_2_tab_content_1')
    link_2_tab_content_2 = models.CharField(max_length=1000, default='link_2_tab_content_2')
    email = models.CharField(max_length=20, default='your@email.com')
    phone = models.CharField(max_length=10, default='Your phone number')


    def __str__(self):
        return self.title


class Cv(models.Model):
    full_name = models.CharField(max_length=50, default='Full_Name')
    slug = models.CharField(max_length=50, default='full-name')
    position = models.CharField(max_length=200, default='Subtitle')
    preamble = models.CharField(max_length=200, default='This_is_the_Preamble')
    avaliable = models.CharField(max_length=200, default='Currently Avaliable')
    relocate = models.CharField(max_length=200, default='Willing to relocate to: ')
    cv_image = models.FileField(default='cv-face.jpg', blank=True)
    email = models.CharField(max_length=50, default='email')
    phone = models.CharField(max_length=20, default='phone')


    def __str__(self):
        return self.full_name


class Cv_headline(models.Model):
    headline_id = models.ForeignKey(Cv, on_delete=models.CASCADE)
    headline = models.CharField(max_length=50, default='headline')
    date = models.CharField(max_length=50, default='headline')
    title = models.CharField(max_length=50, default='title')


    def __str__(self):
        return self.headline


class Cv_list_element(models.Model):
    list_element = models.CharField(max_length=50, default='list_element')
    list_id = models.ForeignKey(Cv_headline, on_delete=models.CASCADE)


    def __str__(self):
        return self.list_element
