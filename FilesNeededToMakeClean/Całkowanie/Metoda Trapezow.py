import math as mat

def funkcja(x):
    return (mat.sqrt(1.3*x + 0.2)) / (mat.log(x+1.1))


def main():
    gp = 0.2
    gk = 0.8
    n = 3
    h = (gk - gp) / n

    integration = 0

    i = 1
    for i in range (i<n):
        integration += funkcja(gp + i * h)
    integration += (funkcja(gp) + funkcja(gk)) / 2
    integration += h

    print(integration)

main()
