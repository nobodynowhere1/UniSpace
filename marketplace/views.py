from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'marketplace/product_list.html'
    context_object_name = 'products'
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = 'marketplace/product_detail.html'
    context_object_name = 'product'


class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'marketplace/product_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Product created.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('marketplace:detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'marketplace/product_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Product updated.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('marketplace:detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Product
    template_name = 'marketplace/product_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Product deleted.')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('marketplace:list')

# Create your views here.
