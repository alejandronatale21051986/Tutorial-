"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import TemplateView
#from  . import views
from rest_framework.schemas import get_schema_view
 
urlpatterns = [
    path('admin/', admin.site.urls),
    #path ('',views.index,name ='index'),
    # ...
    # Route TemplateView to serve the ReDoc template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),# si pongo 'openapi-schema' y ejecuto se queda cargando eternamente. 
    
   

]
"""
ERROR 
|openapi-schema no es una funcion validad de views o |
Reverse for 'openapi-schema' not found. 'openapi-schema' 
is not a valid view function or pattern name.
--------------------------------------------------
(from rest_framework.schemas import get_schema_view )->

"""