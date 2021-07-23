# import timeit module
# only import the function required - speed up your code
from timeit import default_timer as timer

# defining a function called mytimer
def mytimer():

    start= timer()
	
    for i in range(1000000):
            print(i)
        
            end = timer()
		    print(end)
            
            print(end - start)


# calling or invoking the function mytimer hutIIZ	
mytimer()
