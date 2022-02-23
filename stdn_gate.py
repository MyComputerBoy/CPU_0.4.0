
#Basic logic gate functions

import basecpuinf
import math as m

bw = basecpuinf.bit_width

def mod( n, b ):
	return n-m.floor( n/b )* b 

#Logical and
def a( na, nb ):
	return na * nb 

#Logical or
def o( na, nb ):
	return m.ceil( na/2 + nb/2 )

#Logical xor
def x( na, nb ):
	return mod( na + nb, 2 )

#Logical not
def n( na ):
	return 1-na 

#Logical and in list format
def al( la, lb ):
	q = []
	for i in range( bw ):
		q.append( a( la[i], lb[i] ) )
	return q

#Logical or in list format
def ol( la, lb ):
	q = []
	for i in range( bw ):
		q.append( o( la[i], lb[i] ) )
	return q

#Logical xor in list format
def xl( la, lb ):
	q = []
	for i in range( bw ):
		q.append( x( la[i], lb[i] ) )
	return q

#Logical not in list format
def nl( la ):
	q = []
	for i in range( bw ):
		q.append( n( la[i] ) )
	return q
