from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from website.models import Package, Category, HomeBlock, HomeSlide



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
