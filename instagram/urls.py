from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^new/post$', views.new_post, name='new_post'),
    url(r'^profile/edit/$', views.edit, name='edit'),
    url(r'^like/(?P<post_id>\d+)$', views.like, name='like'),
    url(r'^save/(?P<post_id>\d+)$', views.save, name='save'),
    url(r'^follow_or_not/(?P<user_id>\d+)$', views.togglefollow, name='follow_or_not'),
    url(r'^unlike/(?P<post_id>\d+)$', views.unlike, name='unlike'),
    url(r'^user/(?P<user_id>\d+)$', views.user, name='aboutuser'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
