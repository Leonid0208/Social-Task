from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import ImageCreateForm
from .models import *
from django.contrib import messages


# class ObjectCreate:
#
#     def get(self, request):
#         form = ImageCreateForm(data=request.GET)
#         return render(request, 'image/create.html', {'section': 'images', 'form': form})
#
#     def post(self, request):
#         self.user = request.user
#             new_item.save()
#         messages.success(request, 'Image added successfully')
#         return redirect('image_list')
