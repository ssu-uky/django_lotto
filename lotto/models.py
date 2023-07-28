from django.db import models
from django.utils import timezone
import random

# Create your models here.


class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)  # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255)  # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(  # generate 함수를 통해 생성되는 로또 번호 리스트 (str)
        max_length=255,
        default="[1,2,3,4,5,6]",
    )
    num_lotto = models.IntegerField(default=5)  # 로또 번호 6개 set의 갯수
    update_date = models.DateTimeField()  # 로또 번호 리스트 생성 일시

    # generate 라는 함수를 어디서든 사용 가능. (views.py 에서 사용 가능) => new_row.generate() 이렇게 실행 가능
    def generate(self):  # 로또 번호를 자동으로 생성
        self.lottos = ""  # 초기값 생성
        origin = list(range(1, 46))  # 1-45까지의 숫자 리스트

        # 6개 번호 set 갯수 만큼 1-45를 뒤섞은 후 앞의 6개를 골라내어 오름차순으로 보내줌
        for _ in range(0, self.num_lotto):  # num_lotto의 갯수만큼 셋트 수가 문자형태로 나옴
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + "\n"  # 로또번호 str에 6개번호 set 추가

        self.update_date = timezone.now()
        self.save()  # GuessNumbers object를 DB에 저장

    def __str__(self):  # Admin page에서 보여지는 텍스트 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)
    
    class Meta:
        verbose_name_plural = "Guess Numbers"
