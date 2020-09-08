from time import sleep
def cont(a,b,c):
    for i in range(a,b,c):
        sleep(0.5)
        print(i)

cont(20,0,-2)