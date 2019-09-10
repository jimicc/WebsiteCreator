from django.contrib import admin
from .models import Cards, Website,  Cv, Cv_headline, Cv_list_element
# Register your models here.
admin.site.register(Cards),
admin.site.register(Website),
admin.site.register(Cv),
admin.site.register(Cv_headline),
admin.site.register(Cv_list_element),
