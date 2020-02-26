# Partner 1 Name: Maxine Matheson-Lieber
# Partner 2 Name: Amanda Tracy
###########################
#Assignmnent Name: GitHub Practice - 2/26/20 - 10 points


def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    list=[]
    for i in range (n):
       list.append(random.randint(0,11))
    return list

def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    product = 1
    for n in numbers:
        product = product*n
    return product

def main():
    print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
    main()
