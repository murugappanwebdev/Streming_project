from netflix import settings
from netflixapp import views
from django.urls import path
from django.conf.urls.static import static
urlpatterns = [
    path('reg',views.registerpage),
    path('plans/', views.plans_view, name='plans'),
    path('payment/<str:plan_id>/<int:amount>/', views.payment_view, name='payment'),
    path('palyback/<int:id>/', views.watchvideo, name='watchvideo'),
    path('watch/<int:id>/', views.watchmovie, name='homevideo'),
    path('log',views.loginpage),
    path('header',views.header),
    path('',views.frontpage),
    path('out',views.signout),
    path('movie',views.movie),
    path('home',views.tv),
    path('movie/<int:id>/',views.about_detail, name='about_detail'),
    path('series/<int:id>/',views.series_detail, name='series_detail'),   
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)