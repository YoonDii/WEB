from django.shortcuts import render, redirect
from .models import Ppap
from .forms import PpapForm

# Create your views here.


# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    ppaps = Ppap.objects.order_by("-pk")
    # Template에 전달한다.
    context = {"ppaps": ppaps}
    return render(request, "ppap/index.html", context)


# def new(request):
#     ppap_form = PpapForm()
#     context = {
#         'ppap_form': ppap_form
#     }
#     return render(request, 'ppap/new.html', context=context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        ppap_form = PpapForm(request.POST)
        if ppap_form.is_valid():
            ppap_form.save()
            return redirect("ppap:index")
    else:
        ppap_form = PpapForm()
    context = {"ppap_form": ppap_form}
    return render(request, "ppap/new.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    ppap = Ppap.objects.get(pk=pk)
    # template에 객체 전달
    context = {"ppap": ppap}
    return render(request, "ppap/detail.html", context)


def update(request, pk):
    ppap = Ppap.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        ppap_form = PpapForm(request.POST, instance=ppap)
        if ppap_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            ppap_form.save()
            return redirect("ppap:detail", ppap.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 ppap_form을 랜더링
    else:
        # GET : Form을 제공
        ppap_form = PpapForm(instance=ppap)
    context = {"ppap_form": ppap_form}
    return render(request, "ppap/update.html", context)
