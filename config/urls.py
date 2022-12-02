
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from config import views


urlpatterns = [
    path('superadmin_010123/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('myspace/', views.MySpaceViews.as_view(), name='dashboard'),
    path('', include('frontend.urls')),
    path('', include('client.urls')),
    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'config.views.page_not_found_view'
handler500 = 'config.views.error_view'
handler403 = 'config.views.permission_denied_view'
handler400 = 'config.views.bad_request_view'

admin.site.site_header = "SuperAdmin projectX"
admin.site.site_title = "ProjectX"
admin.site.index_title = "Admin"
