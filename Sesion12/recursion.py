
def recursion(x):
    if x>0:
        recursion(x-1)
        print(x)
    print(f'finalizó iteracion x = {x}')


if __name__=="__main__":
    recursion(5)