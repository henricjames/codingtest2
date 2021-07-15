
def print_series(count):
    def print_one_line(i):
        return_string="1"
        for x in range(2,i+1):
            return_string+="#"+str(x)
        if(i%2==0):   # if i is even number then print the reversed string
            print(return_string[::-1]) #string reverse
        else:
            print(return_string)

    #calling the function multiple times
    for count in range(1, count + 1):
        print_one_line(count)




print_series(3)






