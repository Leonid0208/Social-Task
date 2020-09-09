from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ImageCreateForm, CommentForm
from .models import Image
# from .utils import ObjectCreate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


@login_required
def image_create(request):
    if request.method == "POST":
        form = ImageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            return redirect('image_list')
    else:
        form = ImageCreateForm()
    return render(request, 'image/create.html', {'form': form})


def image_detail(request, slug):
    image = get_object_or_404(Image, slug=slug)
    comments = image.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            cd = comment_form.cleaned_data
            new_comment = comment_form.save(commit=False)
            new_comment.post = image
            new_comment.user = request.user
            new_comment.save()
            redirect('image.get_absolute_url')
    else:
        comment_form = CommentForm()

    return render(request, 'image/detail.html', {'section': 'images', 'image': image, 'comments': comments,
                                                 'comment_form': comment_form})


def image_list(request):
    images = Image.objects.all()
    return render(request, 'image/image_list.html', {'list': images})
