from django.conf.urls import url

from article import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^documents/$', views.documents, name='documents'),
    url(r'^info/$', views.info, name='info'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^lich_cab/$', views.lich_cab, name='lich_cab'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^zab_parol/$', views.zab_parol, name='zab_parol'),
    url(r'^zayavka/$', views.zayavka, name='zayavka'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
]