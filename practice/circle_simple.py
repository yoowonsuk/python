from circle import ar_circle as ac
from circle import ci_circle as cc

def ar_circle(rad):
    print("area:", rad * rad * 3.14)
def ci_circle(rad):
    print("circumference:", rad * 2 * 3.14)

def main():
    #print(ar_circle(2))
    #print(ci_circle(3))

    ar_circle(2)
    ci_circle(3)

    print(ac(2))
    print(cc(3))

main()


