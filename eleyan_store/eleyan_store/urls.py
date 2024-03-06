from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
)
