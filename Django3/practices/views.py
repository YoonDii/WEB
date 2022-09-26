from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.


def index(request):

    return render(request, "index.html")


def ping(request):

    return render(request, "ping.html")


def pong(request):

    return render(request, "pong.html", {"name": request.GET.get("ball")})


def isoddeven(requset, _num):
    num = _num

    if num == 0:
        check = 0

    elif num % 2 == 0:
        check = "짝수"
    else:
        check = "홀수"
    context = {"num": num, "check": check}

    return render(requset, "isoddeven.html", context)


def number(requset, num1, num2):
    numm1 = num1
    numm2 = num2
    context = {
        "numm1": num1,
        "numm2": num2,
        "a": num1 + num2,
        "b": num1 - num2,
        "c": num1 * num2,
        "d": num1 // num2,
    }
    return render(requset, "number.html", context)


def pastlife(request):

    return render(request, "pastlife.html")


def pastlife2(request):
    name_ = request.GET.get("name_")
    past_life = [
        "궁녀",
        "밥은 안굶는 노예",
        "왕한테 사랑받는 후궁",
        "딸 2명 낳은 황후",
        "조선절세미녀 옆에 시녀",
        "짚신장인",
        "사냥꾼",
        "양반댁 개똥이",
        "금순이",
    ]
    past = random.choice(past_life)
    context = {"name_": name_, "past": past}
    return render(request, "pastlife2.html", context)


def lipsum(request):
    return render(request, "lipsum.html")


def lipsum2(request):
    sten = int(request.GET.get("sten"))  # 문단수
    word = int(request.GET.get("word"))  # 단어수

    words = [
        "재현",
        "태용",
        "쟈니",
        "도영",
        "해찬",
        "유타",
        "정우",
        "마크",
        "태일",
        "지성",
        "재민",
        "천러",
        "런쥔",
        "제노",
        "쿤",
        "양양",
        "헨드리",
        "샤오쥔",
        "텐",
        "윈윈",
        "성찬",
        "쇼타로",
    ]

    listt = []
    for _ in range(sten):
        l = []
        for _ in range(word):
            w = random.choice(words)
            l.append(w)
        listt.append(l)
        # print(listt)

    context = {
        "sten": sten,
        "word": word,
        "words": listt,
    }
    return render(request, "lipsum2.html", context)
