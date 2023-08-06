from django.contrib import admin 
from django.urls import path, include 
from django.conf.urls.static import static 
from src.settings import MEDIA_ROOT, MEDIA_URL 
from django.conf.urls.i18n import i18n_patterns
from app.views import set_language
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('api/', include('app.urls')), 
]
 
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", set_language, name="set-language"),
]