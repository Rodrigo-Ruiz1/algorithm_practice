candies = [2,3,5,1,3]
max_candies = max(candies)
extra_candies = 3

def extra(self):
    count = 0
    while count < len(candies):
        candies[count] += extra_candies
        if candies[count] >= max_candies:
            print("True")
        else:
            print("False")
        count += 1

extra(candies)