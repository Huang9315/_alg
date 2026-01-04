def newtons_method(X, y):
    # 為了進行矩陣運算，我們需要由 [1, x] 組成的矩陣
    # 增加一列全是 1 的項，用來處理截距 b
    X_b = np.c_[np.ones((len(X), 1)), X] 
    
    # 正規方程公式：theta = (X.T * X)^-1 * X.T * y
    # 這是利用 Hessian 矩陣特性的解析解
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    b = theta_best[0][0]
    w = theta_best[1][0]
    
    return w, b, compute_loss(w, b, X, y)

w_nm, b_nm, loss_nm = newtons_method(X, y)
print(f"[牛頓改良法] w: {w_nm:.4f}, b: {b_nm:.4f}, Loss: {loss_nm:.4f}")