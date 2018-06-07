from django.shortcuts import render
from django.views import View
from .models import ArticleModel,Category,TagsModel

class IndexView(View):
    def get(self,request):
        article_list = ArticleModel.objects.filter().order_by('-id').all()
        return render(request,'index.html',locals())

class BasicsView(View):
    def get(self,request,cid):
        tid = request.GET.get('tid')
        article_list = ArticleModel.objects.filter(category_id=cid).order_by('-create_time').all()
        if tid:
            article_list = ArticleModel.objects.filter(category_id=cid,tags_id=tid).order_by('-create_time').all()
        category = Category.objects.filter(pk=cid).first()
        tags = TagsModel.objects.filter(category=category).all()
        return render(request,'basics.html',locals())


class ArticleDetailView(View):
    def get(self,request,aid):
        article = ArticleModel.objects.filter(pk=aid).first()
        return render(request, 'article_detail.html', locals())