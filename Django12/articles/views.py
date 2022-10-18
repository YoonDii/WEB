from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from articles.forms import ReviewForm, CommetForm
from .models import Review, Comment

# from django.core.paginator import Paginator

# Create your views here.


def index(request):
    k = Review.objects.order_by("id")

    context = {
        "v": k,
    }

    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        ppap_form = ReviewForm(request.POST)
        if ppap_form.is_valid():
            article = ppap_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect(
                "articles:index",
            )
        messages.add_message(request, messages.INFO, "정보를 나타냅니다.")
    else:
        ppap_form = ReviewForm()
    context = {
        "ppap_form": ppap_form,
    }
    return render(request, "articles/create.html", context)


def detail(request, pk):
    k = Review.objects.get(pk=pk)
    comment_form = CommetForm()
    comments = k.comment_set.all()
    context = {
        "i": k,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "articles/detail.html", context)


def delete(request, pk):
    article = get_object_or_404(Review, pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect("articles:index")
    return redirect("articles:detail", article.pk)


def update(request, pk):
    k = get_object_or_404(Review, pk=pk)
    # k = Review.objects.get(pk=pk)
    if request.user == k.user:
        if request.method == "POST":
            ppap_form = ReviewForm(request.POST, instance=k)
            if ppap_form.is_valid():
                ppap_form.save()
                return redirect("/", k.pk)
        else:
            ppap_form = ReviewForm(instance=k)
        context = {
            "ppap_form": ppap_form,
            "ppap": k,
        }
        return render(request, "articles/update.html", context)


def comment_create(request, pk):
    article = Review.objects.get(pk=pk)
    comment_form = CommetForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect("articles:detail", article.pk)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("articles:detail", article_pk)


def comments_update(request, article_pk, comment_pk):
    article = Comment.objects.get(pk=article_pk)
    com_form = CommetForm(instance=article)
    if request.method == "POST":
        update_form = CommetForm(request.POST, instance=article)
        if update_form.is_valid():
            update_form.save()
            return redirect("detail", comment_pk)
    return render(request, "articles/update.html", {"com_form": com_form})
