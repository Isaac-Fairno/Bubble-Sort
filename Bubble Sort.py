# 1 enter a list of data items
import random,time



y = int(input("Enter a length of an array"))
items = [random.randint(0,100) for x in range (y)]


print(f"Original List of {y} numbers: {items}")

start = time.time() #Starts the timeer now to only capture how long the actual sort takes, not all the other code before it

n = len(items)-1

swap = True

while (swap) and n>0: # While loop to only iterate through the array ONLY if swaps are made (swap = True)
    swap = False # Swap is False to break the loop
    
    for x in range(0,n): # For loop to iterate through the array
        
        if items[x]>items[x+1]: # If the current value is greater than the next value the swap the two values

            temp = items[x]
            items[x] = items[x+1]
            items[x+1] = temp
     
            swap = True # Sets swap to True so it loops round again
    n = n-1 #Shortens the list by 1 each pass
end = time.time()
speed = round(end - start, 6) #Makes the time precise

print(items)
print(f"Time Taken: {speed}")


 
        

