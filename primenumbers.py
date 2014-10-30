#Samantha Holloway 10/2014
#OOD
#Program will output all prime numbers up to a given input


#-----Function Definitions----

#Function finds out if a number is prime and prints it
def prime(number):
        i=1
        #any factors must be less than the square root
        #of the number, +1 for python not including upper limit
        upper=int((number ** 0.5))+1
        for i in range(2,upper):
            if number % i == 0: #composite -- do nothing
                break
        else:
            print(number) #prime


#Function loops through all numbers between 1 and the given number
#Calls prime() on each number
def primeloop(number):
    if number > 1:
        for j in range(2, number+1):
            prime(j)
    else:
        print("1 is not a prime number, and has no primes before it")


#----------Program Start--------------

#number is user input
number = int(input("Enter a number: "))
primeloop(number)




