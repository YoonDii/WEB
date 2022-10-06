from django.shortcuts import render, redirect
from .form import InfoForm
from .models import Info
from django.db.models import Q

# Create your views here.


def movies(request):
    infos = Info.objects.order_by("-id")
    context = {"infos": infos}
    return render(request, "info/movies.html", context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        info_form = InfoForm(request.POST)
        if info_form.is_valid():
            info_form.save()
            return redirect("info:movies")
    else:
        info_form = InfoForm()
    context = {"info_form": info_form}
    return render(request, "info/create.html", context=context)


def detail(request, pk):
    info = Info.objects.get(pk=pk)
    context = {"info": info}
    return render(request, "info/detail.html", context)


def delete(request, pk):
    Info.objects.get(pk=pk).delete()
    return redirect("info:movies")


def update(request, pk):
    # 폼하기전
    # return render(request, "info/update.html", context)
    # info = info.objects.get(pk=pk)
    # if request.method == "POST":
    #     info.title = request.POST.get("title")
    #     info.content = request.POST.get("content")
    #     info.save()
    #     return redirect("/")
    # else:
    #     context = {"info": info}
    # return render(request, "info/update.html", context)

    # 폼하고나서
    info = Info.objects.get(pk=pk)

    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        info_form = InfoForm(request.POST, instance=info)
        if info_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            info_form.save()
            return redirect("info:detail", info.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 info_form을 랜더링
    else:
        # GET : Form을 제공
        info_form = InfoForm(instance=info)
    context = {"info_form": info_form, "info": info}
    return render(request, "info/update.html", context)


# def search(request):
#     all_date = Info.objects.all()
#     search = request.GET.get("search", "")

#     if search:
#         aa = all_date.filter(title__icontains=search)

#     bb = {"aa": aa}

#     return render(request, "info/search.html", bb)
def search(request):
    if request.method == "GET":
        search = request.GET.get("search", "")
        reviews = Info.objects.filter(title__icontains=search)
        context = {"aa": reviews}

    return render(request, "info/search.html", context)
