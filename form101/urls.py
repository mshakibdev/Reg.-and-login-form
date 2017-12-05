

from django.conf.urls import url
from django.contrib import admin
from userform import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/', views.get_info),
    url(r'^login/',views.login),
    url(r'^profile/',views.profile),

]
