#05
#Datatype:- A datatype defines the type of value a variable can hold.
#           It indicates variable value is int or str or float etc..
#Types of datatype:-
#                 1. Numeric type
#                 2. Text type
#                 3. Boolen type 
#                 4. Sequence type
#                 5. Set type
#                 6. Mapping type
#                 7. Binary type
#                 8. None type
#1. Numeric type:-
#int - integer (Ex: 5,2,1,6,)
#float - decimal numbers  (Ex: 3.5, 5.6, 8.6)
#complex - complex number (Ex: 3+4j, 4+3j)

#2. Text type:-
# str - string (Ex: "Ironman", "Jarvis")

#3. Boolen type:-
# bool - boolen (Ex: True or False)

#4. Sequence type:-
# list is mutable (changeable)
# Ex: list_1=["Ironman", "Jarvis", 1,2,3])
# tuple is immutable
# Ex: coordinates=(3,9567, 78.9899)
# range 
# Ex: range(end), range(start, end), range(start, stop, step)
# range(3) #0,1,2,
# range(1,5) #2,3,4
# range(1, 5, 3) #2,4

#5. Set type:-
# It is used store unique values only
# Ex:- a={1,2,3}
#      b={3.4.5}
#      print(a | b) #union
#      #{1,2,3,4,5}
#      print(a & b) #intersection
#      #{3}
#      print(a - b) #difference
#      #{1,2}
# frozenset({}) is immutable

#6. Mapping type:-
#  dict is used store key-value pair.
#  dict={key:value}
#  Ex:- movie={
#        "name": "ironman";
#        "hero": "tony stark" 
#              } 

#7. Binary type:-
# it is used to handle raw data
# _01= b'hello' (bytes is immutable)
# _o2= bytearray(b"hello) (bytearray is mutable)
# _03= memoryview(b"hello)

#8.None type:-
# It is used to represent empty value

_1=20
_2="ironman"
_3=3.5
_4=True
_5={"hi":"hello"}
_6={1,2,3}
_7=[1,2,3]
_8=(1,2,3)

#type() is used to check datatype
print(type(_1)) #<class 'int'>
print(type(_2)) #<class 'str'>
print(type(_3)) #<class 'float'>
print(type(_4)) #<class 'bool'>
print(type(_5)) #<class 'dict'>
print(type(_6)) #<class 'set'>
print(type(_7)) #<class 'list'>
print(type(_8)) #<class 'tuple'>

#isinstance() is used to check datatype + inheritance
print(isinstance(_1,int)) #True
print(isinstance(_2,float)) #False
      