import numpy as np

def antisym(A):
    return (A - A[:, ::-1])/2

def sym(A):
    return (A + A[:, ::-1])/2

def sub_line(X, Y, ini = 0, fin = 0):
    ini = int(ini)
    fin = int(fin)
    if fin == 0:
        fin = len(Y) - 1
    slope = (Y[fin] - Y[ini])/(X[fin] - X[ini])
    line = Y[0] + slope*(X-X[0])
    return Y - line
    
def diff(X, Y, n = 1, flag = True):
    """Pay attention to boundaries"""
    if n == 0:
        return Y
    if flag == True:
        X = np.gradient(X)
    Y = np.gradient(Y)/X
    return diff(X, Y, n-1, False)

def minus_min(A):
    return A - min(A)

def average(A, aver_times):
    assert int(len(A))%aver_times == 0, print ('A can not be divided by aver_times')
    res = np.zeros(int(len(A)/aver_times))
    for i in np.split(A, aver_times):
        res += i
    res = res/aver_times
    return res
    
def smoothing(A, n):
    B = []
    for i in range(n//2, len(A) - n//2 + 1):
        B.append(np.mean(A[i-n//2:i+n//2]))
    return np.array(B)

def smooth_2Darray1(A, k, l):
    m, n = np.shape(A)
    B = [[None] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            count = 0
            SUM = 0
            for p in range(i - k, i + k + 1):
                if p < 0:
                    continue
                for q in range(j - l, j + l + 1):
                    if q < 0:
                        continue
                    try:
                        SUM += A[p][q]
                        count += 1
                    except IndexError:
                        pass
            value = SUM/count
            B[i][j] = value
    return np.array(B)
                    
def smooth_2Darray2(A, k, l):
    m, n = np.shape(A)
    B = [[None] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            count = 0
            SUM = 0
            for p in range(i, i + k + 1):
                if p < 0:
                    continue
                for q in range(j, j + l + 1):
                    if q < 0:
                        continue
                    try:
                        SUM += A[p][q]
                        count += 1
                    except IndexError:
                        pass
            value = SUM/count
            B[i][j] = value
    return np.array(B)

def smooth_2Darray(A, k, l, Fullgrid = True):
    return smooth_2Darray1(A, k, l) if Fullgrid == True else smooth_2Darray2(A, k, l)         