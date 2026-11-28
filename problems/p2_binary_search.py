n = int(input())
arr = list(map(int, input().split()))
target = int(input())
lo, hi, ans = 0, n - 1, -1
while lo <= hi:
    mid = (lo + hi) // 2
    if arr[mid] == target:
        ans = mid
        break
    elif arr[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)
