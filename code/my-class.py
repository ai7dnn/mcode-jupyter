# %% 1) 클래스 형식 정의
class Person:
    # 초기화 메소드
    def __init__(self):
        # 인스턴스 멤버변수
        self.name = '홍길동'
    def print(self):
        print('My name is {}'.format(self.name))

# %% #2) 인스턴스 생성
p1 = Person()
p2 = Person()

# %% #3) 메소드 호촐
p1.name = '전우치'
p1.print()
p2.print()

# %% 
Person.title = 'new title'
print(p1.title)
print(p2.title)
print(Person.title)

# %% 
p1.job = 'student'
print(p1.job)

# %%
a, b = 10, 25
print(a + b)
# %%
print('a + b =', a + b)
# %%
print(f'{a} + {b} = {a+b}')

# %%
print('{} + {} = {}'.format(a, b, a+b))

# %%
