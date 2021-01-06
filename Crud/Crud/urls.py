"""Crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Crudapp import views
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='EDI API Documentation')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.insert_view, name='insert'),
    path('api_documentation/',schema_view),
    path('show/',views.show_view, name='show'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    path('update/<int:id>', views.update_view, name='update'),
    path('salary/', views.salary_view, name='salary'),
    path('search/', views.search_view, name='search'),
    # Schema view
    path('show/', schema_view),
    path('delete/<int:id>', schema_view),
    path('update/<int:id>', schema_view),
    path('salary/', schema_view),
    path('search/', schema_view),

]

