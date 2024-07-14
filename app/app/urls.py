from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('gateway.urls')), # You have user sites they can visit
    path('admin/', admin.site.urls) # You have the admin sites that only admins can visit
]

