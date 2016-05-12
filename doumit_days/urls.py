from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'survey.views.home', name='home'),
	url(r'^submit', 'survey.views.submit', name='submit'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^results/$', 'survey.views.results', name='results'),
    url(r'^results/(\d+)/$', 'survey.views.results', name='results_wThanks'),
)
