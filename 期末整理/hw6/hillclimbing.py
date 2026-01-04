def hill_climbing(X, y, iterations=1000, step_size=0.1):
    # 隨機初始化
    w = np.random.randn()
    b = np.random.randn()
    
    best_loss = compute_loss(w, b, X, y)
    
    for i in range(iterations):
        # 在周圍隨機生成一個新的點 (鄰居)
        w_new = w + np.random.uniform(-step_size, step_size)
        b_new = b + np.random.uniform(-step_size, step_size)
        
        new_loss = compute_loss(w_new, b_new, X, y)
        
        # 貪婪策略：如果鄰居比較好，就搬過去
        if new_loss < best_loss:
            w = w_new
            b = b_new
            best_loss = new_loss
            
    return w, b, best_loss

w_hc, b_hc, loss_hc = hill_climbing(X, y)
print(f"[爬山演算法] w: {w_hc:.4f}, b: {b_hc:.4f}, Loss: {loss_hc:.4f}")