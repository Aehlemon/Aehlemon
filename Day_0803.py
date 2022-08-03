# Two Pointer (투 포인터) 알고리즘

# 리스트에 순차적으로 접근해야할 때 2개의 점의 위치를 기록하면서 처리하는 방법
# 학생 1번~8번이 있을 때, 2번부터 7번까지 학생을 부르자!
# 이처럼 '시작점'과 '끝점을 활용하여 데이터의 범위를 표현 가능/ 리스트 원소가 음수 일 수 없다.

# 특정한 합을 가지는 부분 연속 수열 찾기

n = 5  # 데이터 개수
m = 5  # 찾고자 하는 부분 합
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

# start를 차례로 증가시키면서 반복
for start in range(n):
    # end를 가능한 만큼 이동
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1

    interval_sum -= data[start]

print(count) # 3


# '정렬되어 있는 리스트의 합집합' 알고리즘 -> Merge Sort 에서도 활용됨

# 1. 이미 정렬되어 있는 2개의 리스트가 주어짐
# 2. 2개 리스트 원소 값을 합쳐서 정렬한 결과를 보여줘야 함

# 작동원리
# 1. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 함
# 2. 리스트 B에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 함
# 3. A[i], B[j] 중에서 더 작은 원소를 결과 리스트에 담는다
# 4. 리스트 A, B에서 처리하지 않은 원소가 없을 때까지 위 내용 반복

# 리스트 A, B 데이터 개수 각각 N, M이라고 할 때 시간 복잡도 O(N+M) : 단순하게 모든 원소 1번씩 순회

n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 담을 리스트 초기화
result = [0]*(n+m)
i = 0
j = 0
k = 0

# 반복하면서 정렬

while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]): # b의 모든 원소가 처리되었거나 리스트 A원소가 더 작거나 같을 때
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    
    k += 1

for i in result:
    print(i, end=" ")

# 1 2 3 4 5 6 8 





