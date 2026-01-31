from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcements/announcement_list.html'
    context_object_name = 'announcements'
    paginate_by = 10


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcement_detail.html'
    context_object_name = 'announcement'

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class AnnouncementCreateView(StaffRequiredMixin, CreateView):
    model = Announcement
    fields = ['title', 'content', 'cover']
    template_name = 'announcements/announcement_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Announcement created.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('announcements:detail', kwargs={'pk': self.object.pk})


class AnnouncementUpdateView(StaffRequiredMixin, UpdateView):
    model = Announcement
    fields = ['title', 'content', 'cover']
    template_name = 'announcements/announcement_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Announcement updated.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('announcements:detail', kwargs={'pk': self.object.pk})


class AnnouncementDeleteView(StaffRequiredMixin, DeleteView):
    model = Announcement
    template_name = 'announcements/announcement_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Announcement deleted.')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('announcements:list')
