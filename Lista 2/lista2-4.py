def banner(n):
    if n>0 and n%2 == 0 :
        print("| | | | | | | | | |")
    elif n>0 and n%2 == 1  :
        print("- - - - - - - - - -")
    elif n<0 and n%2 == 0 :
        print( ". . . . . . . . . .")
    else:
        print("= = = = = = = = = =")

banner(4)