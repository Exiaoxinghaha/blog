from django.shortcuts import render
from django.views import View
from .models import ArticleModel,Category

class IndexView(View):
    def get(self,request):
        article_list = ArticleModel.objects.filter().order_by('-id').all()
        return render(request,'index.html',locals())

class BasicsView(View):
    def get(self,request,cid):
        article_list = ArticleModel.objects.filter(category_id=cid).all()
        category = Category.objects.filter(pk=cid).first()
        return render(request,'basics.html',locals())

class ArticleDetailView(View):
    def get(self,request,aid):
        article = ArticleModel.objects.filter(pk=aid).first()
        return render(request, 'article_detail.html', locals())