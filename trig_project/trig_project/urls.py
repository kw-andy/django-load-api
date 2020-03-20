"""trig_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# need to import views before creating the URL


from django.contrib import admin
from django.urls import path
from trig_app.views import profile_upload
from trig_app.views import denom_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-file/',profile_upload,name='profile_upload'),
    path('home/',denom_list,name='denom_list'),
]
