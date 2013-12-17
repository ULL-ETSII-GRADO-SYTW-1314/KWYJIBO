from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name="kwyjibo/index.html"), name="index"), 
	url(r'^admin/', include(admin.site.urls)),
	url(r'^subir_receta/', 'Recetas.views.subir_receta'),
	url(r'^subir_receta/', TemplateView.as_view(template_name="recetas/subir_receta.html"), name="subir_receta"),
	url(r'^registrate/', 'Usuarios.views.Registro_Usuario'),
	url(r'^registrate/', TemplateView.as_view(template_name="usuarios/registrate.html"), name="registrate"),
	url(r'^login/', 'Usuarios.views.LogIn'),
	url(r'^about/', TemplateView.as_view(template_name="kwyjibo/about.html"), name="about"),
	url(r'^contact/', TemplateView.as_view(template_name="kwyjibo/contact.html"), name="contact"),
	url(r'^logout/', 'Usuarios.views.LogOut'),
	url(r'^recetas/', 'Recetas.views.buscar_receta'),
	url(r'^recetas/', TemplateView.as_view(template_name="recetas/recetas.html"), name="recetas"),	
	)