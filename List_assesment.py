# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 10:37:17 2019

@author:     
"""

##Statements Assessment Test

#1. Use for, .split(), and if to create a Statement that will print out words that start with 's':
            
st = 'Print only the words that start with s in this sentence'
st.split(" ")
for letter in st.split(" "):
    if letter[0]=="s":
        print(letter)
        
        
        
#2. Use range() to print all the even numbers from 0 to 10.
#Method 1
list(range(0,11,2))

#Method 2
print("The even numbers from 0 to 10 are as")
for num in range(0,11):
    if num%2==0:
        if num>0:
            print(num)
            
            

#3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
#Method 1
[x for x in range(1,51) if x%3==0]            

#Method 2
numlist=[x if x%3==0 else 0 for x in range(0,50)]
for num in numlist:
    if num!=0:
        print(num)  
        
        
        
#4. Go through the string below and if the length of a word is even print "even!"
        
st = 'Print every word in this sentence that has an even number of letters'
st.split(" ")
for word in st.split(" "):
    if len(word)%2==0:
        print("even!")
    else:
        print(word)


"""5. Write a program that prints the integers from 1 to 100.
 But for multiples of three print "Fizz" instead of the number, 
 and for the multiples of five print "Buzz".
 For numbers which are multiples of both three and five print "FizzBuzz"."""
 
for num in range (1,100):
    if num%3==0 and num%5==0:
        print(num," FizzBuzz")
    elif num%3==0:
        print(num," Fizz")
    elif num%5==0:
        print(num," Buzz")
    else:
       print(num)
            

          

#6. Use List Comprehension to create a list of the first letters of every word in the string below:
            
st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split(" ")]        
     
        