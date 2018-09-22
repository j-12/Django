from django.urls import include, path, re_path
from . import views


# app_name='personal'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^products/$', views.products, name='product'),
    re_path(r'^cart/$', views.add_to_cart, name='added'),
    re_path(r'^viewcart/$', views.viewcart, name='added'),
    re_path(r'^login/$',views.login,name='login'),


]
# path('contact/',views.contact,name='contact'),
# /123/-saves an id from the url into id
# re_path(r'^info/$',views.information,name='info'),
# re_path(r'^update/$',views.update_name,name='update'),
