from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import LostFoundItemForm
from .models import LostFoundItem


class LostFoundListView(ListView):
    model = LostFoundItem
    template_name = 'lostfound/item_list.html'
    context_object_name = 'items'
    paginate_by = 10


class LostFoundDetailView(DetailView):
    model = LostFoundItem
    template_name = 'lostfound/item_detail.html'
    context_object_name = 'item'


class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class LostFoundCreateView(LoginRequiredMixin, CreateView):
    model = LostFoundItem
    form_class = LostFoundItemForm
    template_name = 'lostfound/item_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Item created.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lostfound:detail', kwargs={'pk': self.object.pk})


class LostFoundUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = LostFoundItem
    form_class = LostFoundItemForm
    template_name = 'lostfound/item_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Item updated.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('lostfound:detail', kwargs={'pk': self.object.pk})


class LostFoundDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = LostFoundItem
    template_name = 'lostfound/item_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Item deleted.')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('lostfound:list')

# Create your views here.
