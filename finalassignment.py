largest = None
smallest = None
while True:
    num = raw_input("Enter a number")
    if num == 'done' : break
    try:
        int(num)
    except ValueError :
        print "Invalid input"
        continue
    if largest is None or num > largest :
        largest = num
    elif smallest is None or num < smallest :
        smallest = num
print "Maximum is",largest
print "Minimum is",smallest                        
            
