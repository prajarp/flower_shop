"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Homea
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flowershop.views import index
from flowershop.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flower/index', showFlowersView, name='show_flowers'),
    path('flower/show/<int:f_id>/', showFlowerView, name='show_flower'),
    path('flower/create/', createFlowerView, name='create_flower'),
    path('flower/update/<int:f_id>/', updateFlowerView, name='update_flower'),
    path('flower/delete/<int:f_id>/', deleteFlowerView, name='delete_flower'),

    path('color/index', showColorsView, name='show_colors'),
    path('color/show/<int:c_id>/', showColorView, name='show_color'),
    path('color/create/', createColorView, name='create_color'),
    path('color/update/<int:c_id>/', updateColorView, name='update_color'),
    path('color/delete/<int:c_id>/', deleteColorView, name='delete_color'),

    path('flower_arrangement/index', showFlowerArrangementsView, name='show_arrangements'),
    path('flower_arrangement/show/<int:a_id>/', showFlowerArrangementView, name='show_arrangement'),
    path('flower_arrangement/create/', createFlowerArrangementView, name='create_arrangement'),
    path('flower_arrangement/update/<int:a_id>/', updateFlowerArrangementView, name='update_arrangement'),
    path('flower_arrangement/delete/<int:a_id>/', deleteFlowerArrangementView, name='delete_arrangement'),

    path('flower_arrangement/image/delete/<int:i_id>/', deleteImageView, name='delete_image'),
    path('', index),

    path('search/', searchFlowersView, name='search_flowers'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
