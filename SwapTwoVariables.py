P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
   
# To Swap the values of two variables using XOR  
P = P ^ Q  
Q = P ^ Q  
P = P ^ Q  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  


Input:
Please enter value for P:  15
Please enter value for Q:  10
  
Output:
The Value of P after swapping: 10
The Value of Q after swapping: 15
