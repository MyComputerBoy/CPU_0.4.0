# CPU_0.4.0
My own CPU version 0.4.0 and related programs


Parts:
PART ONE: Introduction
PART TWO: information about files and use



PART ONE:
My own Central Processing Unit emulator written in python and runs proprietary machine code encoded in files as 32 bits per line.
Accompanying is an assembler for low level programming and a compiler for higher level programming.

There are 7 basic functions in this instruction set:
if,
read          from rom,
read/write to/from ram,  #This is an outdated implementation, as I'm implementing a newer better way in a wip project
read/write to/from gpio,
get binary line,         #for low level markers
register associated register, #My own implementation of accessing arbitrary address registers through a known register
compute,                 #Used for general purpose computation is in addition, subtraction, logical and, logical nor etc.

With these I've created an assembler to abstract concepts like if elif else and functions.

And on top of that I've created a compiler to abstract concepts like for loops, with lost functionality of 
automatic equation parsing to time, though it is planned to be reimplemented in future implementations



PART TWO:
bm is used for basic mathematic functions

stdn_gate is my implementation of logic gates in my format

ucu is the main emulator used for running the CPU - to run the emulator call ucu.run(), 
which takes the parameters filename, gui_type (normally prints integers), force_show_exceptions 
(some exceptions are due to a quirk of how some of the functions run, which can be enabled for debugging)

c is the assembler  - takes parameters input_file and destination_file where input_file requires extension name

ac is the compiler  - takes parameters input_file and destination_file where input_file requires extension name

