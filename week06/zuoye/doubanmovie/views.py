from django.shortcuts import render,HttpResponse
from django.db.models import Avg
from .models import MovieInfo

# Create your views here.
def movieinfo(request):
    #短评总数
    shorts = MovieInfo.objects.all()

    counter = MovieInfo.objects.all().count()

    #star_value = movieinfo.objects.values('n_star')

    star_avg = f"{MovieInfo.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "

    sent_avg = f" {MovieInfo.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"

    # 正向数量
    queryset = MovieInfo.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = MovieInfo.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())

