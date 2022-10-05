from django.shortcuts import render, redirect

from .forms import PpapForm
from .models import Ppap

# Create your views here.
def index(request):
    ppaps = Ppap.objects.order_by("-id")
    context = {"ppaps": ppaps}
    return render(request, "ppap/index.html", context)


def create(request):
    # get으로 받는 코드
    # if request.method == "GET":
    #     ppap = request.GET
    #     context = {"ppap": ppap}

    #     return render(request, "ppap/create.html", context)
    # else:
    #     title = request.POST.get("title")
    #     content = request.POST.get("content")
    #     Ppap.objects.create(title=title, content=content)

    #     return redirect("/")
    if request.method == "POST":
        # DB에 저장하는 로직
        ppap_form = PpapForm(request.POST)
        if ppap_form.is_valid():
            ppap_form.save()
            return redirect("ppap:index")
    else:
        ppap_form = PpapForm()
    context = {"ppap_form": ppap_form}
    return render(request, "ppap/create.html", context=context)


def detail(request, pk):
    ppap = Ppap.objects.get(pk=pk)
    context = {"ppap": ppap}
    return render(request, "ppap/detail.html", context)


def delete(request, pk):
    Ppap.objects.get(pk=pk).delete()
    return redirect("/")


def update(request, pk):
    # 폼하기전
    # return render(request, "ppap/update.html", context)
    # ppap = Ppap.objects.get(pk=pk)
    # if request.method == "POST":
    #     ppap.title = request.POST.get("title")
    #     ppap.content = request.POST.get("content")
    #     ppap.save()
    #     return redirect("/")
    # else:
    #     context = {"ppap": ppap}
    # return render(request, "ppap/update.html", context)

    # 폼하고나서
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
    context = {"ppap_form": ppap_form, "ppap": ppap}
    return render(request, "ppap/update.html", context)
