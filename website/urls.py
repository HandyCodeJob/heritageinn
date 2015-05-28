from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

#id = '(?P<id>[0-9a-fA-F]{8}[-]?[0-9a-fA-F]{4}[-]?[0-9a-fA-F]{4}[-]?[0-9a-fA-F]{4}[-]?[0-9a-fA-F]{12})'

urlpatterns = (
    url(r'^/?$', 'website.views.home', name='home'),
    url(r'^geothermal/?$',
        TemplateView.as_view(template_name='website/geothermal.html'),
        name='geothermal'
    ),
)
