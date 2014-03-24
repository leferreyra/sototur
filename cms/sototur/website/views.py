from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, View
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
from website.models import Package, Category, HomeBlock, HomeSlide
from website.forms import ContactForm


class HomeBlockList(ListView):

	model = HomeBlock
	template_name = 'home.html'

	def get_context_data(self, **kwargs):

		context = super(HomeBlockList, self).get_context_data(**kwargs)

		# Add category list for menu rendering
		context['categories'] = Category.objects.all()
		context['slides'] = HomeSlide.objects.all()

		return context



class CategoryPackagesList(ListView):

	template_name = 'category.html'

	def get_queryset(self):

		self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
		return Package.objects.filter(category=self.category)

	def get_context_data(self, **kwargs):

		context = super(CategoryPackagesList, self).get_context_data(**kwargs)

		# Add category list for menu rendering
		context['category'] = self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
		context['categories'] = Category.objects.all()
		context['slides'] = HomeSlide.objects.all()

		return context



class PackageDetail(DetailView):

	template_name = 'package.html'
	model = Package

	def get_context_data(self, **kwargs):

		context = super(PackageDetail, self).get_context_data(**kwargs)

		# Add category list for menu rendering
		context['categories'] = Category.objects.all()

		return context



class ContactView(View):

	template_name = 'contact.html'

	def get(self, request):

		return render(request, "contact.html", context_instance=RequestContext(request));



	def post(self, request):


		mailbody = 'Nombre: %s\Telefono: %s\E-mail: %s\nTexto:%s' % (request.POST['nombre'],request.POST['telefono'],request.POST['email'],request.POST['texto'])

		# Enviar una notificacion al correo
		send_mail('Mensaje del sitio web', mailbody, 'noreply@sototur.tur.ar' , ['leferreyra@gmail.com']);

		return render(request, "contact.html", {"msj": "Mensaje enviado correctamente"}, context_instance=RequestContext(request));



	def get_context_data(self, **kwargs):

		context = super(ContactView, self).get_context_data(**kwargs)

		# Add category list for menu rendering
		context['categories'] = Category.objects.all()

		return context



