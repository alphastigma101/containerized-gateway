from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('', TemplateView.as_view(template_name='bug_report.html'), name='bug_report'),
    #path('', TemplateView.as_view(template_name='upload_data.html'), name='upload_data'), 
    #path('', TemplateView.as_view(template_name='about_us.html'), name='about_us'), 
    path('gateway/', include('gateway.urls')), # You have user sites they can visit
    path('admin/', admin.site.urls) # You have the admin sites that only admins can visit
]

