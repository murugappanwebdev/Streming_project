from django.contrib import admin
from netflixapp.models import Movies,Home,payment
class MovieAdmin(admin.ModelAdmin):
    list_display=('title','cast','genre','description')
admin.site.register(Movies,MovieAdmin)
#movies
class HomeAdmin(admin.ModelAdmin):
    list_display=('title','cast','genre')
admin.site.register(Home,MovieAdmin)
#payment
class paymentAdmin(admin.ModelAdmin):
    list_display=('title','cast','genre','description')
admin.site.register(payment,MovieAdmin)
