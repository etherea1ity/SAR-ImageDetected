from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.copy, name='copy'),
    path('detect_change/', views.detect_change, name='detect_change'),
    path('project/', views.project_view, name='project'),
    path('group/', views.group_view, name='group'),
    path('detect/', views.detect, name='detect'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)