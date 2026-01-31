from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CommentForm, DiscussionPostForm
from .models import Comment, DiscussionPost


class DiscussionListView(ListView):
    model = DiscussionPost
    template_name = 'discussions/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = DiscussionPost.Category.choices
        context['active_category'] = self.request.GET.get('category', '')
        return context


class DiscussionDetailView(DetailView):
    model = DiscussionPost
    template_name = 'discussions/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to comment.')
            return redirect('accounts:login')
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=self.object,
                author=request.user,
                content=form.cleaned_data['content'],
            )
            messages.success(request, 'Comment added.')
            return redirect('discussions:detail', pk=self.object.pk)
        context = self.get_context_data(object=self.object)
        context['comment_form'] = form
        return self.render_to_response(context)


class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class DiscussionCreateView(LoginRequiredMixin, CreateView):
    model = DiscussionPost
    form_class = DiscussionPostForm
    template_name = 'discussions/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Discussion created.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('discussions:detail', kwargs={'pk': self.object.pk})


class DiscussionUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = DiscussionPost
    form_class = DiscussionPostForm
    template_name = 'discussions/post_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Discussion updated.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('discussions:detail', kwargs={'pk': self.object.pk})


class DiscussionDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = DiscussionPost
    template_name = 'discussions/post_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Discussion deleted.')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('discussions:list')

# Create your views here.
