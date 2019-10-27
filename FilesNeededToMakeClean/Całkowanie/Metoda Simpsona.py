import math as mat
def f(x):
    return (mat.sqrt(1.3 * x + 0.2)) / (mat.log(x + 1.1))
def main():
    wt = 0.0
    wx = 0.0
    gp = 0.2
    gk = 0.8

    n = 5

    h = (gk - gp) / n

    for i in range(1,n+1):
        x = gp + (i * h)
        wt += f(x - h /2)
        if i < n:
            wx += f(x)
    wx=h/6*(f(gp)+f(gk) +(2*wx)+(4*wt))
    print("Wynik Metodą Simpsona wynosi: ",wx)
main()
