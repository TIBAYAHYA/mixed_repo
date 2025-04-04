#demonstrating the use of an else statement on a while loop,
#basicly whats inside the else statement gets run only, and ONLY If the while loop doesnt get interrupted,
#interruption can be an error, a return, a break or exit

a = 1
b = 5
while a < 10:
    try:
        print("try statement: ___________________________")   
        print(a/b)   


        
    except ZeroDivisionError:
        print(f"except statement: result of {a}/{b} is a zero devision error")
        continue #replace with break and the else statement doesnt get executed
    finally:  #the finnaly statement always executes after try, regardless of there being an axception or not
    

        print("finnaly statement: operation done")
        b -= 1
        a += 1 

else:  # else statement after a while loop will only executes If the loop doesnt get a break
    print("reached the break point!")





    