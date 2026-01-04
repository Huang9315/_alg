import numpy as np
from scipy.optimize import minimize

# 1. 定義目標 P 分佈 (固定不變)
p = np.array([1/2, 1/4, 1/4])

# 定義初始猜測的 Q 分佈 (題目給的範例)
q_init = np.array([1/3, 1/3, 1/3])

# 2. 定義 Cross Entropy 函數 (這是我們要優化的目標函數 Loss Function)
def cross_entropy_loss(q):
    # 為了防止 log(0) 導致錯誤，加上一個極小值 epsilon
    epsilon = 1e-15 
    # 圖片中的公式： sum(p * log2(1/q)) 等同於 -sum(p * log2(q))
    return -np.sum(p * np.log2(q + epsilon))

# 3. 設定限制條件 (Constraints)
# 限制：q 的總和必須為 1
def constraint_sum_to_one(q):
    return np.sum(q) - 1

constraints = ({'type': 'eq', 'fun': constraint_sum_to_one})

# 4. 設定邊界 (Bounds)
# 每個 q 的元素必須在 0 到 1 之間 (機率的定義)
bounds = tuple((1e-5, 1) for _ in range(len(p)))

# 5. 執行優化算法
# 使用 SLSQP (Sequential Least SQuares Programming) 算法，適合處理有限制條件的優化
result = minimize(cross_entropy_loss, q_init, method='SLSQP', bounds=bounds, constraints=constraints)

# 6. 顯示結果
print("--- 優化結果 ---")
print(f"目標 P 分佈: {p}")
print(f"初始 Q 分佈: {q_init}")
print(f"優化後的 Q : {np.round(result.x, 4)}")  # 四捨五入方便閱讀
print("-" * 20)

# 7. 驗證是否相等
if np.allclose(p, result.x, atol=1e-3):
    print(">> 驗證成功！優化後的 Q 非常接近 P。")
    print(f"最小 Cross Entropy 值: {result.fun:.4f}")
    
    # 計算原本 P 的 Entropy (熵) 來對比
    entropy_p = -np.sum(p * np.log2(p))
    print(f"P 的 Entropy (理論最小值): {entropy_p:.4f}")
else:
    print(">> 驗證失敗。")