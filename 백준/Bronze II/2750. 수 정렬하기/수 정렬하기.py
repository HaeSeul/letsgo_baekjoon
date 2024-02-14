def merge_sort(lst):
    # [1] 종료조건
    if len(lst) <= 1:
        return lst

    # [2] 하부호출 : 중앙값 기준으로 배열 분할
    m = len(lst)//2
    left = merge_sort(lst[:m])
    right = merge_sort(lst[m:])

    # [3] 단위작업 : 분할된 left,right 간 비교 => 작은 순서대로 병합
    merge_lst = []
    leftIdx, rightIdx = 0,0
    while leftIdx < len(left) and rightIdx < len(right):
        if left[leftIdx] < right[rightIdx]:
            merge_lst.append(left[leftIdx])
            leftIdx += 1
        else:
            merge_lst.append(right[rightIdx])
            rightIdx += 1

    # 남은 리스트의 값 순차적으로 넣어주기
    return merge_lst + left[leftIdx:] + right[rightIdx:]


N=int(input())
lst = list(int(input()) for _ in range(N))
# ans = qsort(lst)
# print(*ans, sep='\n')

ans2 = merge_sort(lst)
print(*ans2, sep='\n')