from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	url(r'^subir_receta/', 'Recetas.views.subir_receta'),
	url(r'^subir_receta/', TemplateView.as_view(template_name="recetas/subir_receta.html")),
	url(r'^registrate/', 'Usuarios.views.Registro_Usuario'),
	url(r'^registrate/', TemplateView.as_view(template_name="usuarios/registrate.html")),
)
