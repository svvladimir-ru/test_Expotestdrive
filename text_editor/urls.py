from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
        # раздел администратора
        path("admin/", admin.site.urls),
        # импорт из приложения posts
        path("", include("posts.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



