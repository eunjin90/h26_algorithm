# 정수형 스택 연산 실습(용량 5)

MAX = 5 # 스택의 최대 크기(용량)을 5로 정함
stack = []  # 빈 리스트 : 사용할 스택공간

# 스택이 비었는지 검사  True,false
def isEmpty():
    return len(stack) == 0  # len(stack) : 현재 데이터 개수, ==0 : 하나도없으면

# 스택이 꽉찼는지 검사  True,false
def isFull():
    return len(stack) == MAX    # 최대 5

# 데이터 넣기
def push(value):    # value 넣을 값
    if isFull():    # 일단 꽉 찼는지 확인, 추가x
        print("스택이 차 있어서 더이상 추가할수없습니다")
    else:
        stack.append(value) # 안찼으면 리스트에 값 추가

# 데이터 빼기
def pop():
    if isEmpty():   # 일단 비었는지 확인, 비었으면 못뺌
        print("스택이 비어있습니다")
    else:
        print("가져온 데이터 :", stack.pop())    # 맨 위값 꺼내면서 삭제
                                        #  스택은 맨 위(LIFO)만 꺼냄

# 맨 위 보기
def peek():
    if isEmpty():   # 비었는지 확인
        print("스택이 비어있습니다")
    else:
        print("top 값:", stack[-1]) # stack[-1] :리스트의 마지막 값(맨 위)
                                    # 삭제 없이 확인만 함


# 선택지 보여주기
while True:
    print("=============================")
    print("1.push  2.pop  3.peek  0.exit")
    print("=============================")

    # 숫자로 입력받기
    menu = int(input("메뉴선택 : "))

    if menu == 1:
        value = int(input("데이터입력 : "))
        push(value)

    elif menu == 2:
        pop()

    elif menu == 3:
        peek()

    elif menu == 0:
        print("프로그램 종료")
        break

    else:
        print("잘못된 입력입니다")  # 1,2,3,0 아니면 오류

    print("현재스택상태", stack)    # 스택안에 뭐 있는지 보여줌