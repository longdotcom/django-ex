from django.conf import settings
from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin



urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    path('admin/', admin.site.urls),
    path('', include('matchingapp.urls')),
]
