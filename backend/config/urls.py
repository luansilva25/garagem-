"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from garagem import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from uploader.router import router as uploader_router
from django.conf import settings 
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register(r'marcas', views.MarcaViewSet)
router.register(r'cores', views.CorViewSet)
router.register(r'acessorios', views.AcessorioViewSet)
router.register(r'veiculos', views.VeiculoViewSet)
router.register(r'categorias',views.CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("refresh/", TokenRefreshView.as_view(), name=""),
    path('', include(router.urls)),
    path('image/', include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root = settings.MEDIA_ROOT)
