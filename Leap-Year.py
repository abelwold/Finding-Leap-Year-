def problem1(end):
    #initial point
    start = 1600
    #empty list to store and count numbers
    count = [] 
    #if input (end) is less than the given initial dont process otherwise perform the calculation  
    if start > end:  
        print("Out of range.")
    else:
        while(start < end):  
            if start % 100 == 0 and start % 400 == 0:
                count.append(start)
                start += 1
            if start % 4 == 0 and start % 100 != 0:
                count.append(start)
                start += 1
            else:
                start += 1
        return ("The number of leap years from 1600 until " + str(end)  + " is: "+ str(len(count)))