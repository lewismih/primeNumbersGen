# Calculator for prime numbers

 # Beginning of the function prime_num
def prime_num (num):
 	
 	# Check for values from one and below to negative side
 	
  if (num <= 1):
    print ("Not a Prime number.")
 	
  else:
 		for b in range(2, num + 1):
 			num1 = num
 			isPrime = True
 			
 			
 			for c in range (2, b):
        			if (b % c == 0):
 				 			    isPrime = False
 		
 
 		
 		if isPrime == True:
 			print(b)
 			print("Is a prime number")
 		else:
 			print (num1)
 			print ("Not a Prime number.")
