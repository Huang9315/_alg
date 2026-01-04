import random
import math
def riemann_integration_ndim(func, bounds, divisions=10):
    """
    使用中點法則 (Midpoint Rule) 計算 n 維積分。
    
    Args:
        func: 被積函數 f(x1, x2, ..., xn) -> float
        bounds: 積分範圍列表，例如 [(0, 1), (0, 1)] 代表二維的 0~1
        divisions: 每個維度要切分成幾塊 (精度)
    
    Returns:
        積分近似值
    """
    ndim = len(bounds)
    
    # 1. 計算每個維度的步長 (delta)
    # deltas 是一個 list，存著每個維度的 dx, dy, dz...
    deltas = [(b - a) / divisions for a, b in bounds]
    
    # 2. 計算微小體積元素 dV = dx * dy * dz ...
    # 這是最後要乘上的總體積因子
    dv = 1.0
    for d in deltas:
        dv *= d

    # 3. 定義遞迴函數來模擬 n 層迴圈
    def recursive_sum(current_dim, current_point):
        """
        current_dim: 當前正在處理第幾個維度 (0 到 n-1)
        current_point: 目前累積的座標點列表 [x1, x2, ...]
        """
        # 基底情況 (Base Case)：如果座標都收集齊全了 (到達最深層)
        if current_dim == ndim:
            # 計算函數在該點的值
            return func(*current_point)
        
        # 遞迴步驟：遍歷當前維度的所有區段
        start, _ = bounds[current_dim]
        step = deltas[current_dim]
        dim_sum = 0.0
        
        for i in range(divisions):
            # 使用中點法則 (Midpoint Rule) 以提高精度
            # 座標 = 起點 + (i + 0.5) * 步長
            mid_point = start + (i + 0.5) * step
            
            # 遞迴進入下一個維度，並將座標加入列表
            # current_point + [mid_point] 會建立新的列表傳下去
            dim_sum += recursive_sum(current_dim + 1, current_point + [mid_point])
            
        return dim_sum

    # 4. 開始遞迴計算總和
    total_value_sum = recursive_sum(0, [])
    
    # 5. 積分值 = 函數值總和 * dV
    return total_value_sum * dv