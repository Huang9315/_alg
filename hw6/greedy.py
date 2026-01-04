def coordinate_descent(X, y, iterations=100):
    w = 0.0
    b = 0.0
    n = len(X)
    
    # 預先計算一些固定的值以加速
    sum_x = np.sum(X)
    sum_x2 = np.sum(X**2)
    sum_y = np.sum(y)
    sum_xy = np.sum(X * y)
    
    for i in range(iterations):
        # 1. 固定 w，更新 b
        # 對 b 微分等於 0 的解: b = mean(y) - w * mean(x)
        b = (sum_y - w * sum_x) / n
        
        # 2. 固定 b，更新 w
        # 對 w 微分等於 0 的解: w = (sum(xy) - b * sum(x)) / sum(x^2)
        w = (sum_xy - b * sum_x) / sum_x2
        
    return w, b, compute_loss(w, b, X, y)

w_cd, b_cd, loss_cd = coordinate_descent(X, y)
print(f"[座標下降法] w: {w_cd:.4f}, b: {b_cd:.4f}, Loss: {loss_cd:.4f}")