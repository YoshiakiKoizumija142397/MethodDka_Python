from decimal import Decimal, getcontext
import math

# 精度設定（JS の precision: 50 に相当）
getcontext().prec = 50

def method_dka(coeffs, max_iter=10000):
    """
    coeffs: 最高次から定数項までの係数リスト（Decimal）
    例: 3x^2 + 2x + 1 → [3, 2, 1]
    max_iter: 最大反復回数（セーフティロック: デフォルト1万回）
    """

    n = len(coeffs) - 1
    if n == 0:
        raise ValueError("次数が 0 の多項式は解けません")

    # 係数を正規化（sa[i] = sa[i] / sa[0]）
    sa = [c / coeffs[0] for c in coeffs]

    # 初期値の準備
    sr = [Decimal(0)] * (n + 1)
    si = [Decimal(0)] * (n + 1)

    # 収束判定の閾値
    eps = Decimal("1e-50")

    # π
    pi = Decimal(str(math.acos(-1)))

    # 初期半径 sw を求める
    sw = Decimal(0)
    for i in range(2, n + 1):
        sq = Decimal(n) * (abs(sa[i]) ** (Decimal(1) / Decimal(i)))
        if sw < sq:
            sw = sq

    sb = pi * 2 / n
    sc = pi / (2 * n)

    # 初期値（複素数の極座標）
    for j in range(1, n + 1):
        t = sb * (j - 1) + sc
        sr[j] = sw * Decimal(math.cos(float(t)))
        si[j] = sw * Decimal(math.sin(float(t)))

    # 反復開始
    for _ in range(max_iter):
        converged = True

        for i in range(1, n + 1):
            s1 = Decimal(1)
            s2 = Decimal(0)
            s3 = Decimal(1)
            s4 = Decimal(0)

            a = sr[i]
            b = si[i]

            # 多項式評価
            for j in range(1, n + 1):
                t1 = s1 * a - s2 * b
                t2 = s1 * b + s2 * a
                s1 = t1 + sa[j]
                s2 = t2

                if j != i:
                    dx = a - sr[j]
                    dy = b - si[j]
                    t3 = s3 * dx - s4 * dy
                    t4 = s3 * dy + s4 * dx
                    s3 = t3
                    s4 = t4

            denom = s3 * s3 + s4 * s4

            dx = (s1 * s3 + s2 * s4) / denom
            dy = (s2 * s3 - s1 * s4) / denom

            sr[i] -= dx
            si[i] -= dy

            if abs(dx) > eps or abs(dy) > eps:
                converged = False

        if converged:
            return [(sr[i], si[i]) for i in range(1, n + 1)]

    return None  # 収束しなかった場合は None を返す
