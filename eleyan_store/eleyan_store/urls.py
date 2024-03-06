# eleyan_store/urls.py

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

app_name = 'products'

urlpatterns = [
    # Use a unique name like 'admin'
    path('admin/', admin.site.urls, name='admin'),
    path('', include('products.urls')),
]

urlpatterns += i18n_patterns(
    path('products/', include('products.urls')),
)
