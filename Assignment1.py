#Below is a function in python that for each position in the list, sums up all numbers other than the number at that position. For example, given [1,2,3,4], it will return [9,8,7,6].Optimize this function so that it runs faster.
    
def special_sum():
    lst=[1,2,3,4]
    total=sum(lst)
    total_li=[total-x for x in lst]
    print total_li
    
special_sum()
