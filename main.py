import random
import math
from math import perm, comb

def block1():
    print("=== БЛОК 1: Парадокс днів народження ===")
    N = 365
    k_vals = [5, 10, 15, 20, 23, 30, 40, 50, 60, 80]
    for k in k_vals:
        cols = sum(1 for _ in range(10000) if len(set(random.choices(range(N), k=k))) < k)
        W = cols / 10000
        log_p = sum(math.log(N - i) for i in range(k)) - k * math.log(N)
        P = 1 - math.exp(log_p)
        print(f"k={k}: Стат={W:.4f}, Точна={P:.4f}, Похибка={abs(W-P):.4f}")

def block2():
    print("\n=== БЛОК 2: Інспекція мікросервісів ===")
    cA = cB = cAB = cAUB = cNotA = 0
    M = 100000
    for _ in range(M):
        sample = random.sample([1]*4 + [0]*11, 5) 
        s = sum(sample)
        if s == 2: cA += 1
        if s == 0: cB += 1
        if s == 2 or s == 0: cAUB += 1
        if s != 2: cNotA += 1

    PA_ex = (comb(4, 2) * comb(11, 3)) / comb(15, 5)
    PB_ex = comb(11, 5) / comb(15, 5)
    print(f"P(A) = {cA/M:.4f} (Точна: {PA_ex:.4f})")
    print(f"P(B) = {cB/M:.4f} (Точна: {PB_ex:.4f})")

def block3():
    print("\n=== БЛОК 3: Монте-Карло ===")
    for N in [100, 1000, 10000, 100000, 1000000]:
        M = sum(1 for _ in range(N) if (y := random.random()) <= (x := random.random())**2 and y >= 1-x)
        print(f"N={N}: Оцінка={M/N:.4f}, Похибка={abs(M/N - 0.181695):.4f}")

def block4():
    print("\n=== БЛОК 4: Хеш-таблиця ===")
    c1 = c3 = 0
    for _ in range(100000):
        cells = [1]*3 + [0]*7
        random.shuffle(cells)
        if cells.index(0) + 1 == 1: c1 += 1
        if cells.index(0) + 1 == 3: c3 += 1
    print(f"1 спроба: {c1/100000:.4f} (Точна: 0.7000)")
    print(f"3 спроби: {c3/100000:.4f} (Точна: 0.0583)")

block1(); block2(); block3(); block4()
