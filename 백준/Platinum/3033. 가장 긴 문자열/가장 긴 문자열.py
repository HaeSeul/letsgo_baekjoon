def makeSuffix(s):
    n = len(s)
    suffix_array = list(range(n))
    rank = [ord(c) for c in s]  # 문자별 초기 랭크
    temp_rank = [0] * n
    k = 1

    while k < n:
        # 두 키로 정렬: (현재 랭크, 다음 랭크)
        key = [(rank[i], rank[i + k] if i + k < n else -1) for i in range(n)]
        suffix_array.sort(key=lambda i: key[i])

        # 새로운 랭크 계산
        temp_rank[suffix_array[0]] = 0
        for i in range(1, n):
            temp_rank[suffix_array[i]] = temp_rank[suffix_array[i - 1]]
            if key[suffix_array[i]] != key[suffix_array[i - 1]]:
                temp_rank[suffix_array[i]] += 1

        rank = temp_rank[:]
        k *= 2

    return suffix_array


def makeLcp(s, suffix_array):
    n = len(s)
    rank = [0] * n   # 접미사 인덱스 순서
    lcp = [0] * n   # 인접한 두 접미사의 공통 접두사 길이

    # 접미사의 인덱스 저장
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i

    # 다음 문자 비교하며 공통 접두사 길이 계산
    h = 0   # 공통 접두사 길이
    for i in range(n):
        if rank[i] > 0:     # 첫번째 접미사는 비교할 이전 접미사 없음
            j = suffix_array[rank[i] - 1]   # 이전 접미사의 시작 인덱스
            while i+h < n and j+h < n and s[i+h] == s[j+h]:
                h += 1
            lcp[rank[i]] = h

            if h > 0:
                h -= 1
    return lcp


def findLongest(s):
    if len(s) <= 1: return 0
    suffix = makeSuffix(s)
    lcp = makeLcp(s, suffix)
    return max(lcp)

L = int(input())
S = input()
res = findLongest(S)

print(res)