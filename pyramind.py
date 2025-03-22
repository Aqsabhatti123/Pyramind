n = 5  # Number of rows in the pyramid
for i in range(n):     # i = 0, 1, 2, 3, 4
    spaces = ' ' * (n - 1 - i)   #i = 0  ( n - 1 - i = 5 - 1 - 0 = 4)
    # This calculates how many stars to print for each row
    stars = '*' * (2 * i + 1)    #2*0 + 1 = 1 = *     or so on  2*1 + 1 = 3
    print(spaces + stars)    #Row 0: ' ' + '*'  





