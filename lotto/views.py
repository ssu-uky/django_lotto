from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from django.utils import timezone
import random

from .models import GuessNumbers
from .forms import PostForm


# request 파라미터는 views.py 에 통째로 넘겨줌
# request 는 유저가 제출한 데이터


def index(request):
    
    lottos = GuessNumbers.objects.all()  # 전체 행을 가져옴

    # return render(request, html 경로를 포함한 파일 이름, dict에 내가 생성한 python 변수)
    return render(request, "lotto/default.html", {"lottos": lottos})  # context-dict # key값은 lottos 로 설정하고 value 값은(파이썬 변수) 상단에 있는 lottos를 받음


def post(request):
    
    form = PostForm()
    
    return render(request, "lotto/form.html", {"form":form})



def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


# def index(request):

# index.html
# <input type = "text", name = "name"> </input>  <- "Win the Prize!"
# <input type = "text", name = "text"> </input>
# USER가 값을 입력하고, 전송 버튼을 클릭 -> USER가 입력한 값을 가지고 HTTP POST request

# user_input_name = request.POST["name"] # HTML 에서 name 이 "name"인 input tag에 대해 user가 입력한 값 // <로또 번호 리스트의 이름>
# user_input_text = request.POST["text"] # HTML 에서 name 이 "text"인 input tag에 대해 user가 입력한 값 // <로또 번호 리스트에 대한 설명>

# # 하나의 행을 생성
# new_row = GuessNumbers(name=user_input_name, text=user_input_text)

# print(new_row.num_lotto) # 5
# print(new_row.name) # "Win the Prize!"

# new_row.name = new_row.name.upper() # "WIN THE PRIZE!"

# new_row.generate() # 하단과 같음 (models.py 에 정의되어있음.)

# --------------------------------------------------------------------

# new_row.lottos = ""
# origin = list(range(1,46))

# for _ in range(0, new_row.num_lotto):
#     random.shuffle(origin)
#     guess = origin[:6]
#     guess.sort()
#     new_row.lottos += str(guess) + "\n"

# new_row.update_date = timezone.now()

# # new_row.num_lotto = [ np.randint(1,45) for i in range(6) ] # [결과물(np.randint(1,45) , 출처(for i in range(6))]

# new_row.save()

# return HttpResponse("<h1>Hello, world!</h1>")
