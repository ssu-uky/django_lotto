settings.py 에 있는 대문자로 되어있는 변수들은 다른 파일에서 고유명사처럼 활용 가능
BASE_DIR / SECRET_KEY 등..

python manage.py runserver 8001 > 하면 8001번 포트로 서버 실행

# TestCase를 기반으로 프로그램 하는 것 = TDD (Test-Driven Development)

TDD의 핵심은 먼저 코드를 짜는 것이 아니라 testcase를 먼저 작성한 후, testcase를 충족시키는 코드를 써내려가는 것

# Shell

1. python manage.py shell
2. from lotto.models import GuessNumbers -> 빼먹지 말기!!!
    > GuessNumbers.objects.all() => GuessNumbers 의 테이블의 모든 행들을 불러옴 == GuessNumbers 클래스의 모든 것을 불러옴
    > GuessNumbers.objects.get(name="번호 세트 1번") => GuessNumbers 의 (테이블) object(행) 안에서 (name이 "번호 세트 1번" / name의 열의 값이 "번호 세트 1번") 인 것을 꺼내옴
    > GuessNumbers.objects.get(pk=1) == GuessNumbers.objects.get(id=1)

> guess_object = GuessNumbers(name="번호 세트 2번") => 새로운 행을 추가

> guess_object.generate() => models.py에 있는 함수를 실행
> guess_object.lottos => 로또번호 생성 확인

# {% --- %} => 장고 템플릿 태그
# {{ --- }} => dict{} 안에 들어있는 파이썬 변수를 꺼내서 사용할 때 사용

return render(
    첫번째는 request,
    두번째는 user에게 돌려보내줄 html 경로를 포함한 파일 이름,
    세번째로는 예측작업을 다 한 후, 예측 된 결과값을 dict로 내보냄 / dict에 내가 생성한 python 변수를 받아내어 보여줌,
)

# return render(request, html 경로를 포함한 파일 이름, dict에 내가 생성한 python 변수)
# return render(request, "lotto/default.html", {})

장고의 linebreaksbr == <br> 역할 / str 일 때만 가능!

# form tag
method = CRUD (GET,POST,PUT,DELETE)
action = "naver.com/lottos/" 처럼 url을 넣어 주어야 함 (API endpoint 같은 느낌)
- action 을 따로 적지 않는다면 CRUD 요청이 현재 위치하고 있는 동일한 url로 요청함

<input type="text" id="fname" name="fname" value="안녕하세요"> 일 때,
user 가 전송버튼 (submit)을 누른 후 POST 요청이 url로 날라가면,
request.POST["name값"] == request.POST["fname"]

request.POST -> dict
- dict의 key == input tag의 name 값
- dict의 value == input tag의 value 값 (== user가 입력한 값)