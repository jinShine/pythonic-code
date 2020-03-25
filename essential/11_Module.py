# 파이썬 모듈과 패키지

# .. : 부모 디렉토리
# .  : 현재 디렉토리


# pkg라는 패키지 폴더를 생성 했다.

# 클래스 가져오기
from pkg.show import Show

s = Show()
s.p()
s.d()
s.t()


# 클래스가 없고 메서드를 가져오고 싶을때
from pkg.calc import add
from pkg.calc import div

# alias를 사용 할 수 있다.
from pkg.calc import mul as m

print(add(3, 5))
print(div(5, 8))

print(m(3, 2))


