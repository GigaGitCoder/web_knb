from django.urls import path
from knb.views import index_page, game_page, sign_in_page, sign_up_page, logout_and_redirect, send_scores, profile_page, upload_avatar
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from knb.views import upload_image

urlpatterns = [
    path('', index_page, name='index'),
    path('game/', game_page, name='game'),
    path('signin/', sign_in_page, name='signin'),
    path('signup/', sign_up_page, name='signup'),
    path('upload/', upload_image, name='upload_image'),
    path('scores/', send_scores, name='upload_image'),
    path('logout/', logout_and_redirect, name='logout'),
    path('profile/<str:username>', profile_page, name='profile'),
    path('upload-avatar/', upload_avatar, name='upload_avatar'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

