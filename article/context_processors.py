from .models import Category

def category(request):
    categorys = Category.objects.filter().all()
    return {'categorys':categorys}
