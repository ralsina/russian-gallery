from django.conf.urls.defaults import *

urlpatterns = patterns('',

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')), 
    (r'^edit/.*$','russian.gallery.views.edit_page'),
    (r'^.*$','russian.gallery.views.view_page'),
)
