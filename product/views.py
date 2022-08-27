from django.shortcuts import render, redirect
import json
# Create your views here.
from product.forms import AddCategory
from product.models import *
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# def main(request):
#     product = Product.objects.all()
#     category = Category.objects.all()
#     con = {
#         'products': product,
#         'categories': category
#     }
#     return render(request, "index.html", con)
from product.serializer import SubCategorySerializer


def category(request):
    category = Category.objects.all()
    if request.method == 'POST':
        form = AddCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'category.html')
    form = AddCategory()

    return render(request, 'category.html', {'cat': category, 'form': form})


def home(request):
    return render(request, "home.html")


def sub_category(request, sub_id):
    sub_cat = SubCategory.objects.filter(category=sub_id)
    context = {
        'sub': sub_cat
    }
    return render(request, 'sub_category.html', context)


def product(request, pro_id):
    product = Product.objects.filter(sub_category=pro_id)
    return render(request, 'product.html', {'products': product})


# def sub(request):
#     sub = SubCategory.objects.all().values('id', 'title', 'category', 'is_active')
#     result = list(sub)
#     return HttpResponse(json.dumps(result), content_type='application/json')


# def product1(request, cat_id):
#     pro = Product.objects.all().filter(category_id=cat_id).values('id', 'title',
#                                                                   'category',
#                                                                   'sub_category',
#                                                                   'old_price',
#                                                                   'amount',
#                                                                   'article',
#                                                                   'gender').order_by(
#         '-id')
#     result = list(pro)
#     return HttpResponse(json.dumps(result), content_type='application/json')

def detail(request, det_id):
    product = Product.objects.get(pk=det_id)
    context = {
        'product': product
    }
    if request.method == 'POST':
        text = request.POST['text']
        comment = Comment(
            text=text,
            product=product,
            owner=request.user
        )
        comment.save()
        return redirect('detail', det_id=det_id)
    return render(request, 'detail.html', context)


@api_view(['GET'])
def sub_list_api(request):
    sub = SubCategory.objects.all()
    sub_s = SubCategorySerializer(sub, many=True)
    return Response(sub_s.data, status=200)


@api_view(['GET'])
def sub_get_api(request, id):
    sub = SubCategory.objects.get(id=id)
    sub_s = SubCategorySerializer(sub)
    return Response(sub_s.data, status=200)
