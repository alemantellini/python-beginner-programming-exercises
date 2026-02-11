# EJERCICIO 19 - bottles of milk
def number_of_bottles():
    for bottles in range(99,2,-1):
        print(str(bottles) + " bottles of milk on the wall, " + str(bottles) + " bottles of milk. Take one down and pass it around, " + str(bottles-1)+ " bottles of milk on the wall.")
    print("2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.")
    print("1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.")
    print("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
    return None
number_of_bottles()
