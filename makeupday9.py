#duplicate item check storing in empty set
list = ['a','b','c','b','d','e','e','f']

empty_list=[]

for value in list:
  if list.count(value) > 1:
    empty_list.append(value)
    
print(empty_list)    


#single single value (seperate) print korte gele
# unique list of duplicate elements
list = ['a','b','c','b','d','e','e','f']
empty_list = []
for value in list:
  if list.count(value)>1:
    if value not in empty_list:
     empty_list.append(value)
print(empty_list) 
print(list)   
  
   
#Computer pixel
picture = [[0,0,0,1,0,0,0],
          [0,0,1,1,1,0,0], 
          [0,1,1,1,1,1,0], 
          [1,1,1,1,1,1,1], 
          [0,1,1,1,1,1,0], 
          [0,0,1,1,1,0,0],
          [0,0,0,1,0,0,0],
          
        ]

for pixel in picture:
 for image in pixel:
   if image == 0:
     print(' ', end='')
   else:
     print('*', end='')
 print('')


#While loop
i = 0
while i<31:
  print(i)
  i+=1

#while loop, break
i =0

while i < len([1,2,3,4,5,6]):
  print(i)
  i+=1

#list with while Loop
i =0
list = [1,2,3,4,5,6]
while i <len(list):
  print(list[i])
  i+=1
  

while True:
  input('what is your name:')
  break  


#What is good code:
#REAdable
#clean
#dry-do not repeat your code
#kiss- Keep it super simple
#predictable

#Function:

def my_function():
  print("My new Function")

#invoking means cslling the function
my_function()

#parameter:Kind if variable
def my_function(name,address):
  print(f"My name is {name} and i live in {address}")

#invoking means calling the function
my_function("Neeti","Azimpur")


def my_function(num1,num2):
  print(num1+num2)
my_function(5,6)

def my_function(num1,num2):
  return(num1+num2)
print(my_function(5,10))
print(my_function(10,10))
print(my_function(50,10))


#positional argument:
def my_function(name,num2):
  return(name+num2)
print(my_function(5,10))


#pass(one kind of placeholder)
for i in (1,2,3):
  pass
