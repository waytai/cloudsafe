from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudsafe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

#    url(r'^$','handleui.views.index'),
    url(r'^infaq/$','handleui.views.faq'),
    url(r'^inabout/$','handleui.views.about'),
    url(r'^chart/$','handleui.views.chart'),

    url(r'^callback/$','handleui.views.callback'),
    url(r'^$','webui.views.index'),
    url(r'^faq/$','webui.views.faq'),
    url(r'^about/$','webui.views.about'),

    url(r'^syndatabase/$','handleui.views.syndatabase'),
    url(r'^advanced/$','handleui.views.advanced'),

    url(r'^results/$','handleui.views.results'),
    url(r'^queue/$','handleui.views.queue'),

)
