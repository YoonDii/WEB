from multiprocessing import context
from random import random
from django.shortcuts import render
import random
# Create your views here.


def index(request):
    # 메인 페이지를 보여준다.
    menus = [['부대찌개', 'http://www.newstap.co.kr/news/photo/202009/118343_196725_1049.jpg'],
             ['파스타', 'https://m.convenii.com/web/product/big/202011/e23b9620b097a4011615ad41a673a353.jpg'],
             ['짜장면', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQC1MMkDKfjpnZpSAiOHNcGO8cezeyGPYK6oQ&usqp=CAU'],
             ['마라탕', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLLXrcJRkm9CTyvSU50bf0VEil9Tt6n44Znw&usqp=CAU'],
             ['삼겹살', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSad5bluCAOEmt_fPj39tUZN8mzCD9d0xURPw&usqp=CAU'],
             ['타코', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNmBJG2SgInUfmbIUL1yisWG8v3FCx4KBIsA&usqp=CAU'],
             ['칼국수', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLusksHLOlyr-CMywhcU34cXxDMK-WRbF5jw&usqp=CAU'],
             ['라멘', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqIf0Zhy202nsfN2F6DuHERKifJUf5RgHKLA&usqp=CAU']
             ]
    menu = random.choice(menus)

    context = {
        'menu': menu[0],
        'images': menu[1],
    }
    return render(request, 'today-dinner.html', context)


def lotto(request):
    lotto_list = []

    for i in range(5):
        lotto = random.sample(range(1, 46), 6)
        lotto.sort

        lotto_list.append(lotto)

    context = {
        'lotto_list': lotto_list
    }
    return render(request, 'lotto.html', context)
