def recursion(x):
    if x>0:
        print(x)
        recursion(x-1)
    

if __name__=="__main__":
    recursion(5)
    print('BOOOOOOM!!!')