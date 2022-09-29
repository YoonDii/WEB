from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):
    todo = Todo.objects.all()
    context = {
        "todos": todo,
    }
    return render(request, "todos/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    context = {
        "content": content,
        "priority": priority,
        "deadline": deadline,
    }
    return redirect("todos:index")


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")


def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        "todo": todo,
    }
    return render(request, "todos/detail.html", context)


def edit(request, todo_pk):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    todo = Todo.objects.get(pk=todo_pk)

    context = {
        "todo": todo,
    }

    return render(request, "todos/edit.html", context)


# read + create + 알파
# read : 수정페이지에 데이터를 출력
def update(request, todo_pk):
    # update할 특정 데이터를 불러온다. -> todo_pk 를 사용해서
    todo = Todo.objects.get(pk=todo_pk)

    content_ = request.GET.get("content")
    priority_ = request.GET.get("priority")
    deadline_ = request.GET.get("deadline")
    completed_ = request.GET.get("completed")

    # 데이터를 수정
    todo.content = content_
    todo.priority = priority_
    todo.deadline = deadline_
    todo.completed = completed_

    # 데이터를 수정한 것을 반영(save)
    todo.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect("todos:detail", todo.pk)


# 이걸해냄버튼 누르면 진행상태 바뀜
def completed(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True

    todo.save()
    print(todo.completed)
    return redirect("todos:index")
