"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    n1 = 0
    n2 = 1
    count = 0
    while(count < x):
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count+=1

def longest_run(mylist, key):
    c = 0
    for i in range(len(mylist)):
        if key == mylist[i]:
            c+=1
        else:
            break
    return c


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    l = Result(mylist[:len(mylist)//2], mylist[len(mylist)//2:], 0, True)
    if len(mylist) == 0:
        return 0
    for i in range(len(mylist)):
        if mylist[i - 1] !=key
        l.is_entire_range = False
    if l.is_entire_range = True:
        print(len(mylist))
        return(len(mylist))
    elif len(mylist) == 1 and list_result.is_entire_range == False:
        return 0
 
    left = longest_run_recursive(l.left_size, key)
    
    right = longest_run_recursive(l.right_size, key)
 
    if left != 0: 
        if right != 0:
            l.longest_size = left + right
        elif left > list_result.longest_size:
            l.longest_size = left
    elif longest_size_2 > list_result.longest_size and longest_size == 0:
            l.longest_size = right
    
    return l.longest_size
        

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


