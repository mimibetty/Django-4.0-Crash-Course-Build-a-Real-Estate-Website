
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from listings.views import (
    listing_list,
    listing_retrieve,
    listing_create,
    listing_update,
    listing_delete,
    
    listing_test,
    test_get,
    add_listing_test
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<int:pk>/', listing_retrieve),
    path('listing_create/', listing_create),
    path('listing_update/<int:pk>/', listing_update),
    path('listing_delete/<int:pk>/', listing_delete),

    path('listing_test/', listing_test, name='listing_test'),
    path('test_get/', test_get, name='test_get'),
    path('add_listing_test/', add_listing_test, name='add_listing_test'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)