
from django.contrib import admin
from django.urls import path,include
from quiz_app import views as quiz_app_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz_app.urls')),
    path('account/', include('userapp.urls')),
    path('contact', quiz_app_views.contact, name='contact'),
    path('about-us', quiz_app_views.about, name='about'),

]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
