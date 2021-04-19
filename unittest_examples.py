import unittest
'''
파이썬 표준 라이브러리) 유닛테스트
https://docs.python.org/ko/3/library/unittest.html#module-unittest

assertEqual : 기대 결과를 확인
assertTrue : 조건 검증
assertFalse : 조건 검증
assertRaises : 특정 예외 발생 검증

단위 테스트 기본 구성 블록 : TestCase
- 하나의 시나리오
- 완전히 독립적
- test_ 로 시작하는 테스트 메서드 구현
- 텍스터 픽스쳐: 테스트를 위한 실행 환경
    - setUp 으로 사전 설정
    - tearDown 으로 테스트 메서드 실행 후 성공여부와 상관없이 실행, 정리 목적
    - setUp, tearDown, __init__() 은 테스트당 1번씩 실행

unittest.main() : 모듈의 모든 테스트 케이스를 수집해 실행
테스트 묶음을 정의해 실행 : TestSuite & TextTestRunner()

python3.7 -m unittest -v unittest_examples 로 실행가능
 
'''

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

widget_ref = {}

class Widget:
    def __init__(self):
        self.width = 50
        self.height = 50

    def size(self):
        return self.width, self.height

    def resize(self, width, height):
        self.width = width
        self.height = height

    def dispose(self):
        print('dispose '+ str(id(self)))
        pass


class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), 'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150), 'wrong size after resize')

    def tearDown(self):
        self.widget.dispose()


def widget_suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite


class NumbersTest(unittest.TestCase):

    def test_even(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

def number_suite():
    suite = unittest.TestSuite()
    suite.addTest(NumbersTest('test_even'))
    return suite


if __name__ == '__main__':
    # unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(widget_suite())
    runner.run(number_suite())