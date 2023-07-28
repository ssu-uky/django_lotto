from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
# 서비스 내의 기능들을 자동으로 체크해주는 곳


class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name="Test numbers", text="selected numbers")
        g.generate()

        print(g.update_date)
        print(g.lottos)

        # testcase 는 마음대로 구성되어야 함.
        # self 인 이유는 상단에 def 에 self라고 작성했기 때문

        # assert~~~ 로 testcase를 생성

        # g.lottos 가 20글자가 넘는다면
        # 여기서는 true 가 되어야 함 (그래서 assertTrue로 확인)
        self.assertTrue(len(g.lottos) > 20)

        # python manage.py test
