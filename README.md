# CPU_0.4.0
My own CPU version 0.4.0 and related programs

My own Central Processing Unit emulator written in python and runs proprietary machine code encoded in files as 32 bits per line.
Accompanying is an assembler for low level programming and a compiler for higher level programming.

There are 7 basic functions in this instruction set:
if
read          from rom
read/write to/from ram  #This is an outdated implementation, as I'm implementing a newer better way in a wip project
read/write to/from gpio
get binary line         #for low level markers
register associated regist #My own implementation of accessing arbitrary address registers through a known register
compute                 #Used for general purpose computation is in addition, subtraction, logical and, logical nor etc.

With these I've created an assembler to abstract concepts like if elif else and functions.

And on top of that I've created a compiler to abstract concepts like for loops, with lost functionality of 
automatic equation parsing to time, though it is planned to be reimplemented in future implementations
