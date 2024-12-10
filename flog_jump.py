h = [2,9,4,5,1,6,10]
print(f"足場の高さ: {h}")
n = len(h)
h_2 = [0 for _ in range(n)]

def ch_min(i, i_1, i_2):
    # 後ろの足場の高さからコストを計算する
    h_1_abs = abs(h[i] - h[i-1])
    h_2_abs = abs(h[i] - h[i-2])

    h_1_result = i_1 + h_1_abs
    h_2_result = i_2 + h_2_abs

    if h_1_result < h_2_result:
        return h_1_result
    else:
        return h_2_result

for i in range(1, n):
    if i == 1:
        h_2[i] = abs(h[i] - h[i-1])
    else:
        h_2[i] = ch_min(i, h_2[i-1], h_2[i-2]) 

print(f"探索結果は: {h_2}")
print(f"最小コストは: {h_2[n-1]}")
