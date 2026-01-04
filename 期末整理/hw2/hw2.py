from datetime import datetime
import sys

# 為了防止遞迴深度不足導致錯誤 (Python 預設通常是 1000)
sys.setrecursionlimit(2000)

# 方法 1：內建運算
def power2n1(n):
    return 2**n

# 方法 2a：用遞迴 (加法邏輯)
# 缺點：極慢，因為會重複計算 (O(2^n))
def power2n2(n):
    if n == 0: return 1
    return power2n2(n-1) + power2n2(n-1)

# 方法 2b：用遞迴 (乘法邏輯)
# 優點：快，線性時間 (O(n))
def power2n3(n):
    if n == 0: return 1
    return 2 * power2n3(n-1)

# 方法 3：用遞迴 (加法邏輯) + 查表
# 優點：透過查表 (Memoization) 解決了方法 2a 重複計算的問題
def power2n4(n, m={}):
    if n == 0: return 1
    if n in m: return m[n]      # 如果算過，直接查表回傳
    
    # 下面這行原本在方法 2a 會算兩次，現在算完第一次後會存入 m
    val = power2n4(n-1, m) + power2n4(n-1, m)
    
    m[n] = val                  # 紀錄答案
    return val

# --- 執行測試 ---
n_value = 32  # 建議設 30~32 左右，再大方法 2a 會跑非常久

print(f"--- 計算 2 的 {n_value} 次方效能比較 ---")

# 測試方法 1
startTime = datetime.now()
print(f"power2n1({n_value})=", power2n1(n_value))
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
print("-" * 20)

# 測試方法 2a (最慢)
startTime = datetime.now()
print(f"power2n2({n_value})=", power2n2(n_value))
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
print("-" * 20)

# 測試方法 2b
startTime = datetime.now()
print(f"power2n3({n_value})=", power2n3(n_value))
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')
print("-" * 20)

# 測試方法 3 (查表)
startTime = datetime.now()
# 注意：為了公平測試，這裡手動清空預設參數的字典，確保重新計算
print(f"power2n4({n_value})=", power2n4(n_value, {}))
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')