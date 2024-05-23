def print_items(myList):
    for item in myList:
        print(item)


from time import sleep
def print_items2(myList):
    for item in myList:
        sleep(1)
        print(item)

print_items([1,2,5,7,0,7,19,12])
print_items2([1,2,5,7,0,7,19,12])
