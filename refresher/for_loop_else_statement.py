#this demonstrates the use of an else statement at the end of a for loop,
#basicly whats inside the else statement gets run only, and ONLY If the for loop doesnt get interrupted,
#interruption can be an error, a return, a break or exit


for i in range(1,10):
    print(i)
    if i % 5 == 0:
        print("Multiple of 5 found!")
        break #comment this and the else statement reachs execution point
else:
    print("No Multiple of 5 found")
