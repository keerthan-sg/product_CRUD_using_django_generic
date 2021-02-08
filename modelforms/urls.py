from django.conf.urls import url

from modelforms import views


urlpatterns = [

    # /modelforms/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^product/entry/$',views.ProductEntry.as_view(),name='product-entry'),
    url(r'^product/(?P<pk>[0-9]+)/$',views.ProductUpdate.as_view(),name='product-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.ProductDelete.as_view(), name='product-delete'),

]
