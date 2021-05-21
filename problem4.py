list = [2,3,5,7,11]

def prime(self):
    count = 0
    while len(list) > count:
        if list[count] %1 == 0:
            if list[count] % list[count] == 0:
                print(list[count])
                count + 1
        else: return False
        count + 1
            
prime(list)   