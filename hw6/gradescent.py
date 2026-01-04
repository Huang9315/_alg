def gradient_descent(X, y, learning_rate=0.1, iterations=1000):
    w = np.random.randn()
    b = np.random.randn()
    n = len(X)
    
    for i in range(iterations):
        y_pred = w * X + b
        
        # 計算梯度 (偏微分)
        dw = -(2/n) * np.sum(X * (y - y_pred))
        db = -(2/n) * np.sum(y - y_pred)
        
        # 更新權重
        w = w - learning_rate * dw
        b = b - learning_rate * db
        
    return w, b, compute_loss(w, b, X, y)

w_gd, b_gd, loss_gd = gradient_descent(X, y)
print(f"[梯度下降法] w: {w_gd:.4f}, b: {b_gd:.4f}, Loss: {loss_gd:.4f}")