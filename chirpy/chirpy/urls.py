from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'chirpy_app.views.index'), # url for root view
    url(r'^login$', 'chirpy_app.views.login_view'),  # url for login view
    url(r'^logout$', 'chirpy_app.views.logout_view'),  # url for logout view
    url(r'^signup$', 'chirpy_app.views.signup'),  # url for signup view
    url(r'^chirpy$', 'chirpy_app.views.public'),  # url for posting view
    url(r'^submit$', 'chirpy_app.views.submit'),  # url for submitting chirp/post view
    url(r'^users/$', 'chirpy_app.views.users'),  # url for viewing users/profiles
    url(r'^users/(?P<username>\w{0,30})/$', 'chirpy_app.views.users'),  # url for a particular user
    url(r'^follow$', 'chirpy_app.views.follow'), # url for following other users
  

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
