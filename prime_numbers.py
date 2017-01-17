# calculator for prime numbers

 # begining of the functiion prime_num
def prime_num (num):
 	
 	#check for values from one and below to negative side
 	
  if (num <= 1):
    print ("Not a Prime number.")
 	
  else:
 		for b in range(2, num + 1):
 			isPrime = True
 			
 			for c in range (2, b):
        			if (b % c == 0):
 				 			    isPrime = False
 		
 		if isPrime:
 			print(b)
