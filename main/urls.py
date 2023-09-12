from unicodedata import category, name
from django.urls import path
from  . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    url(r'^details/(?P<id>\d+)/$',views.details,name="details"),
    url(r'^category/(?P<id>\d+)/$',views.category,name="category"),
    path('addtocart/<int:id>',views.add_to_cart,name="add_to_cart"),
    path('remove/<int:id>',views.remove_from_cart,name="remove_from_cart"),
    path('viewcart/',views.view_cart,name="view_cart"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)