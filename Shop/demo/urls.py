app_name = 'demo'
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path,re_path
from demo import views

urlpatterns = [
	
	path('', views.demo, name='index'),
    path('form/',views.form),
    path('create/',views.create_data)
	 
]