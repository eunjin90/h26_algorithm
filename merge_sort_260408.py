A = [5, 7, 23, 14, 9]   # 정렬할 원본 배열
new_list = [0] * len(A) # 병합 결과를 임시로 저장할 배열 (같은 크기로 생성)

def merge(A, left, mid, right):
    pL = pNew = left    # pL: 왼쪽 배열 시작 인덱스 / pNew: new_list에 넣을 위치
    pR = mid + 1        # pR: 오른쪽 배열 시작 인덱스

    # 왼쪽과 오른쪽 배열을 비교하면서 작은 값부터 new_list에 넣음
    while pL <= mid and pR <= right:        
        if A[pL] < A[pR]:           # 왼쪽 값이 더 작으면
            new_list[pNew] = A[pL]  # 왼쪽 값을 new_list에 넣고
            pNew += 1               # new_list 다음 위치로 이동
            pL += 1                 # 왼쪽 포인터 이동
            # pNew, pL = pNew +1, pL + 1
        else:                           # 오른쪽 값이 더 작거나 같으면
            new_list[pNew] = A[pR]      # 오른쪽 값을 new_list에 넣고
            pNew, pR = pNew +1, pR + 1  # 둘 다 한 칸 이동

    # 왼쪽 배열에 남은 값이 있으면 한 번에 복사
    if pL <= mid : # 왼쪽 영역에 남아 있는 경우
        new_list[pNew:pNew + mid - pL + 1 ] = A[pL:mid+1]

    if pR <= right : # 오른쪽 영역에 남아 있는 경우
        new_list[pNew:pNew + right - pR + 1] = A[pR:right+1]

    # new_list에 정렬된 내용을 다시 A에 덮어씀 (이게 핵심!!)
    A[left:right+1] = new_list[left:right+1]

def merge_sort(A, left, right):
    if left < right:                # 더 이상 나눌 수 없을 때까지 반복
        mid =(left + right) // 2    # 가운데 인덱스 계산
        merge_sort(A, left, mid)    # 왼쪽 부분 배열 정렬
        merge_sort(A, mid+1, right) # 오른쪽 부분 배열 정렬
        merge(A, left, mid, right)  # 정렬된 두 배열을 합침

merge_sort(A, 0, len(A)-1)  # 전체 배열을 merge sort 실행
print(A)                    # 최종 정렬 결과 출력