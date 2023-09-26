from django.contrib import admin
from django.urls import path,re_path,include
# import views
from Shop import views as v1
from demo import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include("demo.urls" ,namespace="demo")),
    
    
]
