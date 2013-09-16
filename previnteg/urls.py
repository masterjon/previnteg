from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.generic_view', {'template':'home.html'},name='home'),
    url(r'^vida/', 'website.views.generic_view', {'template': 'vida.html'},name='vida'),
    url(r'^danios/', 'website.views.generic_view', {'template': 'danios.html'},name='danios'),
    url(r'^gastos-medicos-mayores/', 'website.views.generic_view', {'template': 'gmm.html'},name='gmm'),
    url(r'^autos/', 'website.views.generic_view', {'template': 'autos.html'},name='autos'),
    url(r'^servicios/', 'website.views.generic_view', {'template': 'servicios.html'},name='servicios'),
    url(r'^contact/','website.views.contact', name='contact'),
    (r'^tinymce/', include('tinymce.urls')),    
    # url(r'^previnteg/', include('previnteg.foo.urls')),
    url(r'^example/','website.views.exa'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
