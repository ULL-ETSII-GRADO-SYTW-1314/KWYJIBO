from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'Usuarios.views.Session'),
	url(r'^$', TemplateView.as_view(template_name="kwyjibo/index.html")), 
	url(r'^admin/', include(admin.site.urls)),
	url(r'^subir_receta/', 'Recetas.views.subir_receta'),
	url(r'^subir_receta/', TemplateView.as_view(template_name="recetas/subir_receta.html")),
	url(r'^registrate/', 'Usuarios.views.Registro_Usuario'),
	url(r'^registrate/', TemplateView.as_view(template_name="usuarios/registrate.html")),
	url(r'^login/', 'Usuarios.views.LogIn'),
<<<<<<< HEAD
	url(r'^about/', TemplateView.as_view(template_name="kwyjibo/about.html")),
	url(r'^contact/', TemplateView.as_view(template_name="kwyjibo/contact.html")),
=======
>>>>>>> fbe24721fcd61daf7775c40ff97d605eb902e22f
	url(r'^logout/', 'Usuarios.views.LogOut'),
)