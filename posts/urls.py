from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('new/', views.new_post, name='new_post'),
    path("<int:post_id>/", views.post_view, name="post"),
    path("<int:post_id>/edit/", views.post_edit, name="post_edit"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
