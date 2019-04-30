from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Festival, Tag, Region
from django.db.models import Count
from .forms import FestivalForm, CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json


def festival_list(request, region, tag=None):
    tag_all = Tag.objects.annotate(num_festival=Count('festival')).order_by('-num_festival')
    festival_li = Festival.objects.filter(region__name=region)

    # if tag:
    #     festival_li = Festival.objects.filter(tag_set__name__iexact=tag, region=region)
    # else:
    #     festival_li = Festival.objects.filter(region__name=region)
    #
    # comment_form = CommentForm()

    # paginator = Paginator(festival_li, 3)
    # page_num = request.POST.get('page')
    #
    # try:
    #     festivals = paginator.page(page_num)
    # except PageNotAnInteger:
    #     festivals = paginator.page(1)
    # except EmptyPage:
    #     festivals = paginator.page(paginator.num_pages)

    # if request.is_ajax():  # Ajax request 여부 확인
    #     return render(request, 'post/post_list_ajax.html', {
    #         'festivals': festivals,
    #         'comment_form': comment_form,
    #     })
    #
    # if request.method == 'POST':
    #     tag = request.POST.get('tag')
    #     tag_clean = ''.join(e for e in tag if e.isalnum())  # 특수문자 삭제
    #     return redirect('post:post_search', tag_clean)

    return render(request, 'festival/festival_list.html', {
        'festival_list': festival_li,
        # 'festivals': festivals,
        # 'comment_form': comment_form,
        'tag_all': tag_all,
        'region': region
    })


def festival_detail(request, region, pk):
    festival = get_object_or_404(Festival, region__name=region, pk=pk)
    return render(request, 'festival/festival_detail.html', {
        'festival': festival
    })


def festival_new(request):
    if request.method == 'POST':
        form = FestivalForm(request.POST, request.FILES)
        if form.is_valid():
            festival = form.save(commit=False)
            festival.save()
            festival.tag_save()

            return redirect('travel:complete')
    else:
        form = FestivalForm()
    return render(request, 'festival/festival_new.html', {
        'form': form,
    })


def festival_complete(request):
    return render(request, 'festival/festival_complete.html')



# 좋아요 기능
@login_required
@require_POST  # 해당 뷰는 POST method 만 받는다.
def post_like(request):
    pk = request.POST.get('pk', None)
    festival = get_object_or_404(Festival, pk=pk)
    festival_like, festival_like_created = festival.like_set.get_or_create(user=request.user)

    if not festival_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': festival.like_count,
               'message': message,
               'nickname': request.user.profile.nickname}

    return HttpResponse(json.dumps(context), content_type="application/json")


from django.views.generic.edit import FormView
from .forms import FileFieldForm

class FileFieldView(FormView):
    form_class = FileFieldForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')
        if form.is_valid():
            for f in files:
                with open(Path(settings.MEDIA_ROOT + "/" + f.name).resolve(), 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

            return JsonResponse({'form': True})
        else:
            return JsonResponse({'form': False})


