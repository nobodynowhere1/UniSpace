from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from discussions.models import DiscussionPost
from lostfound.models import LostFoundItem
from marketplace.models import Product

from .forms import AvatarUploadForm, RegistrationForm
from .models import Profile


def register(request):
    if request.user.is_authenticated:
        return redirect('discussions:list')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome to UniSpace!')
            return redirect('discussions:list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    profile_obj, _ = Profile.objects.get_or_create(user=request.user)
    avatar_form = AvatarUploadForm(instance=profile_obj)
    context = {
        'user_posts': DiscussionPost.objects.filter(author=request.user),
        'user_products': Product.objects.filter(author=request.user),
        'user_items': LostFoundItem.objects.filter(author=request.user),
        'avatar_form': avatar_form,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def update_avatar(request):
    if request.method != 'POST':
        return redirect('accounts:profile')
    profile_obj, _ = Profile.objects.get_or_create(user=request.user)
    form = AvatarUploadForm(request.POST, request.FILES, instance=profile_obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Avatar updated.')
    else:
        messages.error(request, 'Please upload a valid image.')
    return redirect('accounts:profile')

# Create your views here.
