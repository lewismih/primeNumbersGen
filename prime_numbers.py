# Calculator for prime numbers

 # Beginning of the function prime_num
def prime_num (num):
 	
 	# Check for values from one and below to negative side
 	
  if (num <= 1):
    print ("Not a Prime number.")
 	
  else:
 		num1 = num
 		for b in range(2, num + 1):
 			isPrime = True
 			 			
 			for c in range (2, b):
        			if (b % c == 0):
        				isPrime = False
  		
 		if isPrime == True:
 			print("%s is a prime number" % b)
 			
 		else:
 			print ("%s is NOT a Prime number" % num1)
 			
