#  given a string of rights and lefts find the number of combinations that lead up to a number


num = 6
the_str = "rrlrlr"
start = 1
end = 4

rights = the_str.count("r")
lefts = the_str.count("l")


pairs = min(lefts,rights)
excess = 
