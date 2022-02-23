

#Compiler

def pl( lst ):
	for i in lst:
		print( i )

import basecpuinf
import c

import math 
import bm 

##########################################################
#Show advanced infomation
#To show advanced info, set variable to "yes"
#Otherwise set it to "no"
##########################################################
show_adv_inf = "no"

#Get Basic Info about Simulated CPU and Folders
bw = basecpuinf.bit_width
bf = basecpuinf.base_folder
pf = basecpuinf.programs_folder
exeff = basecpuinf.executable_files_folder

function_names = [
	"declare",
	"save",
	"io",
	"for",
	"compute",
	"gl",
	"rar",
	"def",
	"mark",
	"else",
	"elif",
	"srar",
	"switch",
]

vov = [ 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1 ]

if_name = ["if","irar"]

scn = "case"

alu_funcs = [
	"+",
	"-",
	"*",
	"/",
	"and",
	"or",
	"xor",
	">>",
	"not",
]

alu_conv_funcs = [
	"add",
	"sub",
	"mul",
	"div",
	"and",
	"or",
	"xor",
	"shift",
	"not",
]

inscape_escape = [
	"{",
	"}"
]

if_names = [
	">",
	"==",
	">=",
	"<",
	"!=",
	"<=",
	"weird",
	"co",
	">c",
	"==c",
	">=c",
	"<c",
	"!=c",
	"<=c",
	"jump"
]

func_params = [
	[["0"],["0"]],
	[["0"],["to","from"],["0"]],
	[["input","print"],["0"]],
	[["0"],["0"],["0"],["0"]],
	[["0"],["add","sub","mul","div","&","+","(+)","|",">>","","","","","","","compare"],["0"],["0"]],
	[["0"],["0"],["0"]],
	[["to","from"],["0"],["0"]],
	[["0"],["0"],["0"]],
	[["0"],["0"],["0"]],
	[],
	[["0"],[">","==",">=","<","!=","<=","weird","co",">c","==c",">=c","<c","!=c","<=c","jump"],["0"]],
	[["to","from"],["0"],["0"]],
	[["0"]],
]

func_param_types = [
	["con","con","cop","cop","None"],
	["con","con","cop","cop","None"],
	["con","con","cop","None","None"],
	["con","cop","cop","None","None"],
	["con","cop","cop","con","cop"],
	["con","cop","None","None","None"],
	["con","con","cop","cop","None"],
	["cop","cop","cop","None","None"],
	["cop","cop","cop","None","None"],
	["cop","None","None","None","None"],
	["cop","cop","cop","cop","None"],
	["cop","cop","cop","cop","None"],
	["cop","cop","cop","None","None"],
]

lib_funcs = [
	"sqrt",
	"pow",
	"mod",
	"faculty",
	"create_table",
	"table_sg",
	#"tan",
	#"ln"
]

library_functions = [
	[						#sqrt uses ram address 0 to 5, returns to 2
		"def sqrt",
		"{",
		"save n from 0",
		"len = 15",
		"save len to 1",
		"t = 100000",
		"n = n * t",
		"save n to 0",
		"q = 10000",
		"save q to 2",
		"save len to 3",
		"for 0 null 1 3",
		"{",
		"save n from 0",
		"save q from 2",
		"ttr = 2",
		"tfo = 10000",
		"ton = q * q",
		"ttw = n - ton",
		"ttr = ttr * n",
		"ttr = ttr / tfo",
		"ttr = ttw / ttr",
		"q = q + ttr",
		"save q to 2",
		"}",
		"}"
	],
	[						#pow uses ram address 0 to 6, returns to 3
		"def pow",
		"{",
		"save a from 0",
		"save b from 1",
		"save b to 4",
		"save scalar from 2",
		"b = b * scalar",
		"save b to 3",
		"for 0 null 1 4",
		"{",
		"save q from 3",
		"save a from 0",
		"q = q * a",
		"save scalar from 2",
		"q = q / scalar",
		"save q to 3",
		"}",
		"}"
	],
	[						#mod uses ram address 0 to 2, returns to 2
		"def mod",
		"{",
		"save a from 0",
		"save b from 1",
		"t = a / b",
		"t = t * b",
		"t = a - t",
		"save t to 2",
		"}"
	],
	[						#faculty uses ram address 0 to 4, returns to 1
		"def faculty",
		"{",
		"save a from 0",
		"save a to 1",
		"save a to 2",
		"for 1 null 1 2",
		"{",
		"save a from 1",
		"save i from 3",
		"a = a * i",
		"save a to 1",
		"}",
		"}",
	],
	[						#create table uses ram address 0 to 10, start address for tables at 11
		"def create_table",
		"{",
		"save i	 from 0",
		"save j	 from 1",
		"save ofs from 2",
		"save i	 to 3",
		"save j	 to 6",
		"for 0 null 1 3",
		"{",
		"for 0 null 1 6",
		"{",
		"save i from 4",
		"save j from 7",
		"save il from 1",
		"save ofs from 2",
		"tt = 11",
		"t = i 	* il",
		"t = j	+ t",
		"t = ofs + t",
		"t = t + tt",
		"save t to 10",
		"tq = 0",
		"srar tq to 10",
		"}",
		"}",
		"}",
	],
	[						#table save/get uses ram address 0 to 7, returns to 7
		"def table_sg",
		"{",
		"save h from 0",
		"save w from 1",
		"save ofs from 2",
		"save i from 3",
		"save j from 4",
		"save sg from 5",
		"save d from 6",
		"if i <= h",
		"{",
		"if j <= w",
		"{",
		"tt = 11",
		"t = i * w",
		"t = j + t",
		"t = ofs + t",
		"t = tt + t",
		"save t to 7",
		"at = 0",
		"if sg == at",
		"{",
		"srar 7 from 7",
		"}",
		"else",
		"{",
		"srar d to 7",
		"}",
		"}",
		"else",
		"{",
		"q = -1",
		"print q",
		"}",
		"}",
		"else",
		"{",
		"q = -1",
		"print q",
		"}",
		"}",
	],
]

reserved_keywords = [
	"to",
	"from",
]

func_var_reserved_keywords = [
	"{",
	"}",
	"else",
	"elif",
	"to",
	"from",
]

add_info = [ 0,2,0,2,2,0,1,0,0,0,0,2,0 ]
run_info = [ 0,0,0,1,0,0,0,1,0,1,1,0,0 ]

def convert_var_one( v ):
	if v == func_params[2][0][0]:
		return "input"
	elif v == func_params[2][0][1]:
		return "output"
	else:
		return str( v )

def convert_var_two( v ):
	if v == func_params[1][1][0]:
		return func_params[1][1][1]
	elif v == func_params[1][1][1]:
		return func_params[1][1][0]
	return str( v )

def convert_var_tre( v ):
	return str( v )

def convert_func_var( v ):
	if v == function_names[0]:
		return "rom"
	elif v == function_names[1]:
		return "ramset"
	elif v == function_names[2]:
		return "io"
	elif v == function_names[4]:
		return "compute"
	elif v == function_names[5]:
		return "gbl"
	elif v == function_names[6]:
		return "rar"
	elif v == function_names[11]:
		return "rar"
	else:
		return v 

def inline( bool, line, filename, used_in_escape ):
	fh = open( bf + pf + filename, "r" )
	lines = fh.readlines()
	fh.close()
	if bool:
		if used_in_escape == 1 and inscape_escape[1] in lines[line]:
			return False
		else:
			return True
	else:
		if inscape_escape[0] in lines[line]:
			return False
		else:
			return True

#Dedicated function for figuring out if, def and for setup
def get_func( lines, line, temp_len, history, temp_temp ):
	temp_temp = len( history )
	temp_temp = len( history )
	if temp_temp > temp_len:
		return True 
	else:
		temp = lines[line].split()
		temp = temp.pop( 0 )
		if temp_temp == temp_len:
			if temp == "}" or "escape" in temp:
				return False
			else:
				return True 
		else:
			return False

#Find the index for the last for in history
def get_last_for( history ):
	i = len( history )-1
	l = 0
	for j in history:
		if history[i-l] == "for":
			return str( i-l+1 )
		l += 1
	return Error

#Find the index for the last function in history
def get_last_func( history ):
	i = len( history )-1
	l = 0
	for j in history:
		if history[i-l] == "func":
			return str( i-l+1 )
		l += 1
	return Error

#Return the index of the current function or -1
def get_func_num( ln_n, lines, m_func_index, m_func_start_ln, m_a_func_num ):
	for i in m_func_start_ln:
		if int( m_func_start_ln[i] ) < ln_n and ln_n < int( m_func_index[i] ):
			return m_a_func_num[i]
	return -1

#Change the order of parameters defined by add_info
def reverseOrder( order, var_one, var_two=None, var_tre=None ):
	if order == 0:
		return var_one, var_two, var_tre
	elif order == 1:
		return var_two, var_tre, var_one
	elif order == 2:
		return var_two, var_one, var_tre
	else:
		return -1

#Get Variable Type
def gvt( var ):
	if var == "0b" + var[2:]:
		return "bin"
	elif var == "0x" + var[2:]:
		return "hex"
	else:
		try:
			tuv = int( var )
			return "int"
		except:
			return "other"

def tfbh( var ):
	if var == "0b" + var[2:]:
		return False
	elif var == "0x" + var[2:]:
		return False
	elif var == "1b" + var[2:]:
		return False
	else:
		return True

#Convert Variable To String
def convertVar( var ):
	tt = gvt( var )
	t = var[2:]
	if tt == "bin":
		return str( bm.btd([int(i) for i in t]) )
	elif tt == "hex":
		return str( bm.htd( t ) )
	elif tt == "int":
		return str( var )
	elif tt == "other":
		return var
	else:
		return Error
	
#Find the line number in the lower level language
def getLine( lines, line, if_marks, table_index, funcs=[] ):
	l = 0
	line_rel_ln = 0
	vars = ["" for i in range(7)]
	for i in range( line ):
		temp_unused_var = lines[l].split()
		temp_func = temp_unused_var.pop( 0 )
		try:
			tttuv = lines[l+1].split()
			tf = tttuv.pop( 0 )
		except:
			tf = ""
		try:
			vars[0] = temp_unused_var.pop( 0 )
		except:
			vars[0] = None
		try:
			vars[1] = temp_unused_var.pop( 0 )
		except:
			vars[1] = None
		try:
			vars[2] = temp_unused_var.pop( 0 )
		except:
			vars[2] = None
		try:
			vars[3] = temp_unused_var.pop( 0 )
		except:
			vars[3] = None
		iint = 0
		for i in vars:
			try:
				t = vars[iint][2:]
				if vars[iint] == "0b" + t:
					vars[iint] = bm.btd([int(i) for i in t])
				elif vars[iint] == "0x" + t:
					vars[iint] = bm.htd(t)
			except:
				pass
			iint += 1
		if temp_func == inscape_escape[1]:
			line_rel_ln += 1
			b = False
			for j in range( len( if_marks ) ):
				for k in range( len( if_marks[str(j)] ) ):
					if if_marks[str(j)][str(k)]["1"] == l and if_marks[str(j)][str(int(k)-1)]["0"] == 1:
						line_rel_ln -= 1
						b = True
						break
				if b:
					break
		elif temp_func == "print":
			try:
				vars[0] = int( vars[0] )
				line_rel_ln += 2
			except:
				line_rel_ln += 1
		elif temp_func == inscape_escape[0]:
			line_rel_ln += 1
			b = False
			for j in range( len( if_marks ) ):
				for k in range( len( if_marks[str(j)] ) ):
					if if_marks[str(j)][str(k)]["1"] == l - 1 and if_marks[str(j)][str(k)]["0"] == 1:
						line_rel_ln -= 1
						b = True
						break
				if b:
					break
		elif temp_func == function_names[3]:
			line_rel_ln += 5
			if vars[0] == "null":
				line_rel_ln -=  1
			if vars[1] == "null":
				line_rel_ln -=  1
			if vars[2] == "null":
				line_rel_ln -=  1
		elif temp_func == "break":
			line_rel_ln += 2
		elif temp_func == lib_funcs[5] and table_index.get( vars[0] ) != None:
			line_rel_ln += 7
			if vars[1] != None:
				line_rel_ln += 1
			if vars[2] != None:
				line_rel_ln += 1
			if vars[3] != None:
				line_rel_ln += 1
		elif temp_func == lib_funcs[4] and table_index.get( vars[0] ) != None:
			line_rel_ln += 7
		elif temp_func in funcs:
			line_rel_ln += 4
			if vars[0] != None:
				line_rel_ln += 1
			if vars[1] != None:
				line_rel_ln += 1
			if vars[2] != None:
				line_rel_ln += 1
			if vars[3] != None:
				line_rel_ln += 1
		elif temp_func == function_names[3]+"escape":
			line_rel_ln += 4
		elif temp_func == function_names[7]+"escape":
			line_rel_ln += 4
		elif temp_func == function_names[9]:
			line_rel_ln += 2
		elif temp_func == function_names[10]:
			line_rel_ln += 4
		elif temp_func == function_names[12]:
			line_rel_ln += 12356789
		elif temp_func == scn:
			pass
		elif temp_func == if_name[0] and vars[1] in if_names:
			line_rel_ln += 2
		else:
			line_rel_ln += 1
		l += 1
	return line_rel_ln

def lastHis( list ):
	temp_var = list.pop( -1 )
	list.append( temp_var )
	return temp_var

def bif( lines ):
	ln_n = 0
	lib_funcs_used = dict()
	while ln_n < len( lines ):
		line = lines[ln_n]
		func = line.split()
		func_var = func.pop( 0 )
		if func_var in lib_funcs:
			if func_var in lib_funcs_used:
				pass 
			else:
				lib_funcs_used[func_var] = "used"
		ln_n += 1
	t = [*lib_funcs_used.keys()]
	for i in t:
		temp = lib_funcs.index( i )
		temptemp = len( library_functions[temp] )
		for j in range( temptemp ):
			lines.insert( j, str( library_functions[temp][j] ) + "\n" )
	return lines, lib_funcs_used

def gin( if_marks, ts ):
	if len( if_marks[ts] ) == 0:
		return str( ts )
	else:
		ts = int( ts )
		for j in range( len( if_marks ) ):
			t = if_marks[str(ts-j)]
			if len( t ) == 0:
				return str( ts-j )
			else:
				iint = 1
				for i in range( len( t ) ):
					if t[str(i)]["0"] == 0:
						break
					elif iint == len( t ):
						return str( ts-j )
					iint += 1
	return str( 0 )

#Check if vars[0] is viable for user_vars
def var_one_viable_var( var, func_var, user_vars ):
	return tfbh( var ) and func_var != if_name[0] and func_var != "break" and func_var != function_names[7] and func_var != function_names[8] and func_var != function_names[10] and vov[function_names.index(func_var)] == 1 and user_vars.get( var ) == None and str( var ) != "null" and var not in reserved_keywords

#Check if vars[1] is viable for user_vars
def var_two_viable_var( var, func_var, user_vars ):
	return tfbh( var ) and var != "null" and func_var != function_names[1] and func_var != function_names[10] and user_vars.index( var ) == None and var not in reserved_keywords

#Check if vars[2] is viable for user_vars
def var_tre_viable_var( var, func_var, user_vars ):
	return tfbh( var ) and var not in alu_funcs and func_var != function_names[7] and func_var != function_names[10] and user_vars.index( var ) == None and func_var != "defescape" and var not in reserved_keywords

#Check if vars[3] is viable for user_vars
def var_for_viable_var( var, user_vars ):
	return tfbh( var ) and var not in reserved_keywords and user_vars.index( var ) == None

#The first logical iteration of the program
def pon_han_specs( lines ):
	pon_han_r_len = 13		#pon_han return length
	ln_n = 0
	for_lines = dict()
	m_for_index = dict()
	m_for_out_index = dict()
	m_func_num = dict()
	m_func_start_ln = dict()
	m_a_func_num = dict()
	table_index = dict()
	if_marks = dict()
	marks = dict()
	user_vars = dict()
	switch_index = dict()
	vars = ["" for i in range(7)]
	history = []
	funcs = dict()
	func_calls = []
	m_func_index = dict()
	while ln_n < len( lines ):
		line = lines[ln_n]
		func = line.split()
		func_var = func.pop( 0 )
		try:
			temp_unused_var = int( lines[ln_n] )
		except:
			if func_var != inscape_escape[0] and func_var != inscape_escape[1] and func_var != function_names[9]:
				try:
					vars[0] = func.pop( 0 )
					try:
						tuv = int( vars[0] )
					except:
						if var_one_viable_var( vars[0], func_var, user_vars ):
							vars[0] = str( vars[0] )
							user_vars[vars[0]] = len( user_vars )
				except:
					if func_var in function_names:
						print( "Error: ln " + str( ln_n + 1 ) + ", Variable one missing" )
						return [-1 for i in range( pon_han_r_len )]
					elif "escape" in func_var or func_var == "break" or func_var in marks or func_var in funcs or func_var in lib_funcs:
						pass 
					elif str( vars[0] ) == "=":
						if user_vars.get( func_var ) == None:
							user_vars[str( func_var )] = len( user_vars )
					else:
						if show_adv_inf == "yes":
							print( "Warning: ln " + str( ln_n + 1 ) + ", Variable one missing, 1" )
				vars[2] = None 
				if func_var != if_name[0] and func_var != if_name[1] and func_var != function_names[5] and func_var != function_names[7]:
					try:
						vars[1] = func.pop( 0 )
						try:
							tuv = int( vars[1] )
						except:
							if var_two_viable_var( vars[1], func_var, user_vars ):
								vars[1] = str( vars[1] )
								user_vars[vars[1]] = len( user_vars )
					except:
						vars[1] = 0
					try:
						vars[2] = func.pop( 0 )
						try:
							tuv = int( vars[2] )
						except:
							if var_two_viable_var( vars[2], func_var, user_vars ):
								vars[2] = str( vars[2] )
								user_vars[vars[2]] = len( user_vars )
					except:
						vars[2] = 0
					try:
						vars[3] = func.pop( 0 )
						try:
							tuv = int( vars[3] )
						except:
							if var_for_viable_var( vars[3], user_vars ):
								vars[3] = str( vars[3] )
								user_vars[vars[3]] = len( user_vars )
					except:
						if func_var == function_names[3]:
							print( "Error: ln " + str( ln_n + 1 ) + ", Variable four is missing" )
							return [-1 for i in range( pon_han_r_len )]
						else:
							vars[3] = 0
				else:
					vars[1] = ""
					vars[2] = ""
					vars[3] = ""
		iint = 0
		for i in vars:
			try:
				t = vars[iint][2:]
				if vars[iint] == "ob" + t:
					vars[iint] = str( bm.btd( [int( i ) for i in t] ) )
				elif vars[iint] == "0x" + t:
					vars[iint] = str( bm.htd( t ) )
				elif vars[iint] == "1b" + t:
					vars[iint] = int( t ) + len( funcs )
			except:
				pass
			iint += 1
		if func_var == if_name[0]:
			if vars[0] != "jump":
				history.append( "if" )
				if_marks[ str( len( if_marks ) ) ] = dict()
		elif func_var == lib_funcs[4]:
			table_index[vars[0]] = { "0": vars[1], "1": vars[2], "2": vars[3] }
		elif func_var == function_names[3]:
			history.append( "for" )
		elif func_var == function_names[7]:
			history.append( "def" )
			funcs[str( vars[0] )] = ln_n + 2
		elif func_var == function_names[8]:
			marks[vars[0]] = ln_n
		elif func_var == function_names[9]:
			ts = str( len( if_marks ) - 1 )
			ts = gin( if_marks, ts )
			tss = str( len( if_marks[ ts ] ) )
			if_marks[ ts ][ tss ] = { "0": 1, "1": ln_n }
			history.append( "else" )
		elif func_var == function_names[10]:
			ts = str( len( if_marks ) - 1 )
			ts = gin( if_marks, ts )
			tss = str( len( if_marks[ ts ] ) )
			if vars[0] in if_names:
				if_marks[ ts ][ tss ] = { "0": 2, "1": ln_n }
			else:
				if_marks[ ts ][ tss ] = { "0": 3, "1": ln_n }
			history.append( "elif" )
		elif func_var == function_names[12]:
			switch_index[len(switch_index)] = []
		elif func_var == scn:
			switch_index[len(switch_index)-1].append( [vars[0], ln_n] )
		elif func_var == inscape_escape[1]:
			try:
				tt = lines[ln_n + 1].split()
				tt = tt.pop( 0 )
			except:
				tt = ""
			ts = str( len( if_marks ) - 1 )
			ts = gin( if_marks, ts )
			if str( tt ) != function_names[9] and str( tt ) != function_names[10] and len( if_marks[ts] ) > 0:
				tss = str( len( if_marks[ ts ] ) )
				if_marks[ ts ][ tss ] = {"0": 0, "1": ln_n }
		elif func_var == inscape_escape[0]:
			temp_unused_var = lastHis( history )
			temp_len = len( history )
			temp_temp = lines[ln_n-1].split()
			temp_temp = temp_temp.pop( 0 )
			if str( temp_temp ) == str( temp_unused_var ):
				if temp_temp != function_names[7]:
					vars[0] = ""
				vars[1] = ""
				vars[2] = ""
				if temp_temp == function_names[3] or temp_temp == function_names[7] or temp_temp == if_name[0]:
					rel_ln = 1
					try:
						while get_func( lines, ln_n + rel_ln, temp_len, history, temp_temp ):
							temp_temp_1 = lines[ln_n + rel_ln].split()
							temp_unused_func = temp_temp_1.pop( 0 )
							try:
								tt = lines[ln_n + rel_ln + 1]
								tt_uf = tt.pop( 0 )
							except:
								tt_uf = ""
							if temp_unused_func == "if":
								temp_if_var = lines[ln_n + rel_ln + 1].split()
								temp_if_func = temp_if_var.pop( 0 )
								if temp_if_func == inscape_escape[0]:
									history.append( "if" )
							elif temp_unused_func == "for":
								history.append( "for" )
							elif temp_unused_func == "def":
								history.append( "def" )
							elif temp_unused_func == "else":
								history.append( "else" )
							elif temp_unused_func == "elif":
								history.append( "elif" )
							elif temp_unused_func == "}" and tt_uf != "elif" and tt_uf != "else":
								history.pop( -1 )
							elif temp_len < len( history ) and temp_unused_func == function_names[7]+"escape":
								history.pop( -1 )
							elif temp_len < len( history ) and temp_unused_func == function_names[3]+"escape":
								history.pop( -1 )
							rel_ln += 1
						nel = ln_n + 1 + rel_ln		#nel = End Line
						hl = str( len( history ) )	#hl  = History Length
						if str( temp_temp ) == function_names[3]:	#For function
							m_for_index[ hl ] = ln_n 
							m_for_out_index[ hl ] = nel
							lines[ ln_n + rel_ln ] = str( temp_temp ) + "escape # " + hl + "\n"
						elif str( temp_temp ) == function_names[7]:	#User Defined Function
							m_func_start_ln[ str( vars[0] ) ] = ln_n
							m_func_index[ str( vars[0] ) ] = nel
							m_func_num[ hl ] = len( funcs )
							m_a_func_num[str( vars[0] )] = len( funcs )
							lines[ nel - 1 ] = str( temp_temp ) + "escape # " + hl + "\n"
					except:
						print( "Error: ln " + str( ln_n + 1 ) + ": Expected escape, got none" )
						return [-1 for i in range( pon_han_r_len )]
			else:
				print( "Error: ln " + str( ln_n + 1 ) + ": Missing core function for inscape" )
				return [-1 for i in range( pon_han_r_len )]
		ln_n += 1
	return [lines, m_for_index, m_for_out_index, funcs, m_func_num, m_a_func_num, m_func_index, user_vars, marks, if_marks, table_index, switch_index, m_func_start_ln]

#The second logical iteration of the program
def pse_han_specs( funcies, lines, m_for_index, funcs, m_func_index, marks, if_marks, table_index, m_func_start_ln, m_a_func_num ):
	for_index = dict()
	for_lines = dict()
	func_index = dict()
	divided_user_vars = dict()
	divided_user_vars[-1] = dict()
	for i in m_func_index:
		divided_user_vars[m_a_func_num[i]] = dict()
	vars = ["" for i in range(7)]
	for j in funcies:
		history = []
		ln_n = 0
		s_ln = 0
		while ln_n < len( lines ):
			line = lines[ln_n]
			func = line.split()
			func_var = func.pop( 0 )
			try:
				temp_unused_var = int( lines[ln_n] )
			except:
				if func_var != inscape_escape[0] and func_var != inscape_escape[1] and str( func_var ) != "break" and func_var not in marks and func_var != function_names[9]:
					if func_var in funcs:
						pass
					else:
						try:
							vars[0] = func.pop( 0 )
						except:
							print( "Error: ln " + str( ln_n + 1 ) + ", Variable one missing" )
							return -1, -1, -1, -1, -1, -1
						vars[2] = None 
						if func_var != if_name[0] and func_var != if_name[1] and func_var != function_names[5] and func_var != function_names[7]:
							try:
								vars[1] = func.pop( 0 )
							except:
								vars[1] = 0
							try:
								vars[2] = func.pop( 0 )
							except:
								vars[2] = 0
							try:
								vars[3] = func.pop( 0 )
							except:
								vars[3] = 0
						else:
							vars[1] = ""
							vars[2] = ""
							vars[3] = ""
			iint = 0
			fn = get_func_num( ln_n, lines, m_func_index, m_func_start_ln, m_a_func_num )
			if vars[0] == "=":
				if divided_user_vars[fn].get( func_var ) == None and func_var not in func_var_reserved_keywords:
					divided_user_vars[fn][func_var] = len( divided_user_vars[fn] )
			for i in vars:
				try:
					if i == 0:
						if var_one_viable_var( vars[0], func_var, divided_user_vars[fn] ):
							divided_user_vars[fn][vars[0]] = len( divided_user_vars[fn] )
					elif i == 1:
						if var_two_viable_var( vars[1], func_var, divided_user_vars[fn] ):
							divided_user_vars[fn][vars[1]] = len( divided_user_vars[fn] )
					elif i == 2:
						if var_tre_viable_var( vars[2], func_var, divided_user_vars[fn] ):
							divided_user_vars[fn][vars[2]] = len( divided_user_vars[fn] )
					elif i == 3:
						if var_for_viable_var( vars[3], func_var, divided_user_vars[fn] ):
							divided_user_vars[fn][vars[3]] = len( divided_user_vars[fn] )
					t = vars[iint][2:]
					if vars[iint] == "0b" + t:
						vars[iint] = bm.btd([int(i) for i in t])
					elif vars[iint] == "0x" + t:
						vars[iint] = bm.htd(t)
				except:
					pass
				iint += 1
			if func_var == if_name[0]:
				if vars[0] != "jump":
					history.append( "if" )
			elif func_var == function_names[3]:
				history.append( "for" )
			elif func_var == function_names[7]:
				history.append( "def" )
			elif func_var == function_names[9]:
				history.append( "else" )
			elif func_var == function_names[10]:
				history.append( "elif" )
			elif func_var == inscape_escape[0]:
				temp_temp = lines[ln_n-1].split()
				temp_temp = temp_temp.pop( 0 )
				if j != 7:
					vars[0] = ""
				vars[1] = ""
				vars[2] = ""
				if temp_temp == function_names[j]:
					rel_ln = 1
					temp_p_a = 0
					#try:
					hist_len = str( len( history ) )
					if j==3:
						for_lines[ hist_len ] = getLine( lines, m_for_index[ hist_len ], if_marks, table_index, funcs ) - 1
						for_index[ hist_len ] = vars[3]
					elif j==7:
						lines[ln_n-1] = function_names[7] + " " + vars[0] + " " + hist_len + "\n"
						func_index[ vars[0] ] = getLine( lines, m_func_index[ vars[0] ], if_marks, table_index, funcs )
					#except:
					#	print( "Error: ln " + str( ln_n + 1 ) + ": Expected escape, got none" )
					#	return -1, -1, -1, -1, -1, -1
			ln_n += 1
	return lines, for_lines, for_index, funcs, func_index, history, divided_user_vars

#The final compilation of the program
def comp( filename, dest_name ):
	fh = open( bf + pf + filename )
	lines = fh.readlines()
	fh.close()
	fh = open( bf + pf + dest_name + ".s", "w+" )
	ev = []
	ieep = True
	ln_n = 0
	s_ln = 0
	il = 0
	lines, lib_funcs_used = bif( lines )
	lines_length = len( str( len( lines ) ) )
	vars = ["" for i in range(7)]
	print( "First Logical Iteration." )
	[lines, m_for_index, m_for_out_index, funcs, m_func_num, m_a_func_num, m_func_index, user_vars, marks, if_marks, table_index, switch_index, m_func_start_ln] = pon_han_specs( lines )
	if show_adv_inf == "yes":
		print( "if_marks: " + str( if_marks ) )
	if lines == -1:
		return -1
	print( "Second Logical Iteration." )
	lines, for_lines, for_index, funcs, func_index, history, divided_user_vars = pse_han_specs( [3,7], lines, m_for_index, funcs, m_func_index, marks, if_marks, table_index, m_func_start_ln, m_a_func_num )
	if show_adv_inf == "yes":
			print( "History: " )
			print( history )
			print( "Divided User Vars: " )
			print( divided_user_vars )
			print( "Functions: " )
			print( funcs )
			print( "For info: " )
			print( "m_for_index: " + str( m_for_index ) )
			print( "for_index: " + str( for_index ) )
			print( "for_lines: " + str( for_lines ) )
			print( "m_for_out_index: " + str( m_for_out_index ) )
			print( "marks: " + str( marks ) )
			print( "tables: " + str( table_index ) )
			print( "switch_index: " + str( switch_index ) )
			print( "" )
			print( "" )
			print( "Lines: " )
			i = 0
			for line in lines:
				t = ""
				for j in range( lines_length-len( str( i ) ) ):
					t += " "
				print( t + str( i ) + ": " + line, end='' )	
				i += 1
			print( "" )
			print( "" )
	history = []
	print( "ram offset: " + str( len( funcs ) ) )
	if lines == -1:
		return -1
	if lines == -1:
		return -1
	print( "Final compilation." )
	fnl = 0
	for i in divided_user_vars:
		if len( str( i ) ) > fnl:
			fnl = len( str( i ) )
	while ln_n < len( lines ):
		line = lines[ln_n]
		fn = get_func_num( ln_n, lines, m_func_index, m_func_start_ln, m_a_func_num )
		if show_adv_inf == "yes":
			t = ""
			for j in range( lines_length-len( str( ln_n ) ) ):
				t += " "
			print( t + str( ln_n ), end=', ' )
			t = ""
			for j in range( fnl - len( str( fn ) ) ):
				t += " "
			print( t + str( fn ), end=": " )
		func = line.split()
		if show_adv_inf == "yes":
			print( func )
		vars[0] = ""
		vars[1] = ""
		vars[2] = ""
		vars[3] = ""
		func_var = func.pop( 0 )
		full_line_function = ""
		line_var_one = ""
		line_var_two = ""
		line_var_tre = ""
		line_var_for = ""
		line_var_fiv = ""
		line_var_six = ""
		line_var_sev = ""
		nextLine = None 
		nextLineTwo = None
		for_lns = None
		try:
			temp_unused_var = int( lines[ln_n] )
		except:
			if func_var != inscape_escape[0] and str( func_var ) != "break" and func_var not in marks and func_var != function_names[9]:
				try:
					vars[0] = func.pop( 0 )
					if vars[0] in user_vars:
						if vars[0] not in marks and func_var not in lib_funcs and func_var not in funcs and func_var != function_names[7] and func_var != "print" and tfbh( vars[0] ):
							vars[0] = divided_user_vars[fn][vars[0]]
				except:
					if func_var == inscape_escape[1] or func_var in lib_funcs or func_var in funcs:
						pass
					else:
						print( "Error: ln " + str( ln_n + 1 ) + ", Variable one missing" )
						return -1
				vars[2] = None 
				if func_var == if_name[1] or func_var == function_names[5] or func_var in func_params[2][0] or func_var == function_names[8] or func_var == function_names[12] or func_var == scn:
					vars[1] = ""
					vars[2] = ""
					vars[3] = ""
				else:
					try:
						vars[1] = func.pop( 0 )
						if vars[1] in user_vars and func_var != function_names[7] and func_var != lib_funcs[5] and func_var not in funcs and tfbh( vars[1] ):
							vars[1] = divided_user_vars[fn][vars[1]]
					except:
						if func_var == inscape_escape[1] or func_var == if_name[0] or func_var == function_names[11] or func_var in funcs or func_var in lib_funcs:
							pass 
						else:
							print( "Error: ln " + str( ln_n + 1 ) + ", Variable two missing" )
							return -1
					try:
						vars[2] = func.pop( 0 )
						if vars[2] in user_vars and func_var != function_names[7] and func_var != lib_funcs[5] and tfbh( vars[2] ):
							vars[2] = divided_user_vars[fn][vars[2]]
					except:
						vars[2] = ""
					try:
						vars[3] = func.pop( 0 )
						if vars[3] in user_vars and func_var != lib_funcs[5] and func_var != function_names[7] and tfbh( vars[3] ):
							vars[3] = divided_user_vars[fn][vars[3]]
					except:
						vars[3] = ""
		iint = 0
		for i in vars:
			try:
				t = vars[iint][2:]
				if vars[iint] == "0b" + t:
					vars[iint] = bm.btd([int(i) for i in t])
				elif vars[iint] == "0x" + t:
					vars[iint] = bm.htd(t, True)
				elif vars[iint] == "1b" + t:
					vars[iint] = int( t ) - len( funcs )
			except:
				pass
			iint += 1
		if func_var == if_name[0]:
			if vars[0] == "jump":
				full_line_function = "if jump"
				nextLine = str( getLine( lines, int( lines[ln_n + 1] ), if_marks, table_index, funcs ) )
				ln_n += 1
			else:
				history.append( "if" )
				il += 1
				if vars[0] in if_names:
					full_line_function = "if " + str( vars[0] )
				elif vars[1] in if_names:
					full_line_function = "compute compare gpr " + str( vars[0] ) + " gpr " + str( vars[2] ) + " gpr " + str( vars[2] )
					nextLine = "if " + str( vars[1] )
			vars[0] = ""
			vars[1] = ""
			vars[2] = ""
		elif func_var == if_name[1]:
			full_line_function = "irar " + str( vars[0] )
		else:
			try:
				full_line_function = int( lines[ln_n] )
			except:
				try:
					func_num = function_names.index( func_var )
				except:
					pass
				try:
					vars[0], vars[1], vars[2] = reverseOrder( add_info[function_names.index(func_var)], vars[0], vars[1], vars[2] )
				except:
					line_var_one = ""
					line_var_two = ""
					line_var_tre = ""
				try:
					t = lines[ln_n+1].split()
					t = t.pop( 0 )
				except:
					t = ""
				if func_var in lib_funcs:
					nextLineTwo = "poss"
					for_lns = []
					if func_var == lib_funcs[5] and table_index.get( vars[0] ) != None:
						for_lns.append( "rom ram " + str( len( funcs ) + 0 ) +  " " + str( len( ev ) ) )
						ev.append( table_index[vars[0]]["0"] )
						for_lns.append( "rom ram " + str( len( funcs ) + 1 ) +  " " + str( len( ev ) ) )
						ev.append( table_index[vars[0]]["1"] )
						for_lns.append( "rom ram " + str( len( funcs ) + 2 ) +  " " + str( len( ev ) ) )
						ev.append( table_index[vars[0]]["2"] )
						try:
							vars[1] = int( vars[1] )
							for_lns.append( "rom ram " + str( len( funcs ) + 3 ) + " " + str( len( ev ) ) )
							ev.append( vars[1] )
						except:
							try:
								for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[1]] ) + " ram " + str( len( funcs ) + 3 ) )
							except:
								if show_adv_inf == "yes":
									print( "Warning: ln " + str( ln_n ) + ", unknown function parameter two" )
						try:
							vars[2] = int( vars[2] )
							for_lns.append( "rom ram " + str( len( funcs ) + 4 ) + " " + str( len( ev ) ) )
							ev.append( vars[2] )
						except:
							try:
								for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[2]] ) + " ram " + str( len( funcs ) + 4 ) )
							except:
								if show_adv_inf == "yes":
									print( "Warning: ln " + str( ln_n ) + ", unknown function parameter three" )
						try:
							vars[3] = int( vars[3] )
							for_lns.append( "rom ram " + str( len( funcs ) + 5  ) + " " + str( len( ev ) ) )
							ev.append( vars[3] )
						except:
							try:
								for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[3]] ) + " ram " + str( len( funcs ) + 5 ) )
							except:
								if show_adv_inf == "yes":
									print( "Warning: ln " + str( ln_n ) + ", unknown function parameter four" )
					elif func_var == lib_funcs[4] and table_index.get( vars[0] ) != None:
						for_lns.append( "rom ram " + str( len( funcs ) + 0 ) +  " " + str( len( ev ) ) )
						ev.append( table_index[vars[0]]["0"] )
						for_lns.append( "rom ram " + str( len( funcs ) + 1 ) +  " " + str( len( ev ) ) )
						ev.append( table_index[vars[0]]["1"] )
						for_lns.append( "rom ram " + str( len( funcs ) + 2 ) +  " " + str( len( ev ) ) )
						ev.append( table_index[vars[0]]["2"] )
					else:
						try:
							vars[0] = int( vars[0] )
							for_lns.append( "rom ram " + str( len( funcs ) ) + " " + str( len( ev ) ) )
							ev.append( vars[0] )
						except:
							try:
								for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[0]] ) + " ram " + str( len( funcs ) ) )
							except:
								if show_adv_inf == "yes":
									print( "Warning: ln " + str( ln_n ) + ", unknown function parameter one" )
						try:
							vars[1] = int( vars[1] )
							for_lns.append( "rom ram " + str( len( funcs ) + 1 ) + " " + str( len( ev ) ) )
							ev.append( vars[1] )
						except:
							try:
								for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[1]] ) + " ram " + str( len( funcs ) + 1 ) )
							except:
								if show_adv_inf == "yes":
									print( "Warning: ln " + str( ln_n ) + ", unknown function parameter two" )
						try:
							vars[2] = int( vars[2] )
							for_lns.append( "rom ram " + str( len( funcs ) + 2 ) + " " + str( len( ev ) ) )
							ev.append( vars[2] )
						except:
							try:
								for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[2]] ) + " ram " + str( len( funcs ) + 2 ) )
							except:
								if show_adv_inf == "yes":
									print( "Warning: ln " + str( ln_n ) + ", unknown function parameter three" )
						try:
							vars[3] = int( vars[3] )
							for_lns.append( "rom ram " + str( len( funcs ) + 3  ) + " " + str( len( ev ) ) )
							ev.append( vars[3] )
						except:
							try:
								for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[3]] ) + " ram " + str( len( funcs ) + 3 ) )
							except:
								if show_adv_inf == "yes":
									print( "Warning: ln " + str( ln_n ) + ", unknown function parameter four" )
					for_lns.append( "gbl gpr 0" )
					for_lns.append( "ramset from gpr 0 ram " + str( m_a_func_num[func_var]-1 ) )
					for_lns.append( "if jump" )
					for_lns.append( str( getLine( lines, funcs[ func_var ], if_marks, table_index, funcs ) ) )
				elif func_var in funcs:
					nextLineTwo = "poss"
					for_lns = []
					try:
						vars[0] = int( vars[0] )
						for_lns.append( "rom ram " + str( len( funcs ) ) + " " + str( len( ev ) ) )
						ev.append( vars[0] )
					except:
						try:
							for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][str(vars[0])] ) + " ram " + str( len( funcs ) ) )
						except:
							if show_adv_inf == "yes":
								print( "Warning: ln " + str( ln_n ) + ", unknown function parameter one" )
					try:
						vars[1] = int( vars[1] )
						for_lns.append( "rom ram " + str( len( funcs ) + 1 ) + " " + str( len( ev ) ) )
						ev.append( vars[1] )
					except:
						try:
							for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[1]] ) + " ram " + str( len( funcs ) + 1 ) )
						except:
							if show_adv_inf == "yes":
								print( "Warning: ln " + str( ln_n ) + ", unknown function parameter two" )
					try:
						vars[2] = int( vars[2] )
						for_lns.append( "rom ram " + str( len( funcs ) + 2 ) + " " + str( len( ev ) ) )
						ev.append( vars[2] )
					except:
						try:
							for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[2]] ) + " ram " + str( len( funcs ) + 2 ) )
						except:
							if show_adv_inf == "yes":
								print( "Warning: ln " + str( ln_n ) + ", unknown function parameter three" )
					try:
						vars[3] = int( vars[3] )
						for_lns.append( "rom ram " + str( len( funcs ) + 3  ) + " " + str( len( ev ) ) )
						ev.append( vars[3] )
					except:
						try:
							for_lns.append( "ramset from gpr " + str( divided_user_vars[fn][vars[3]] ) + " ram " + str( len( funcs ) + 3 ) )
						except:
							if show_adv_inf == "yes":
								print( "Warning: ln " + str( ln_n ) + ", unknown function parameter four" )
					for_lns.append( "gbl gpr 0" )
					for_lns.append( "ramset from gpr 0 ram " + str( m_a_func_num[func_var]-1 ) )
					for_lns.append( "if jump" )
					for_lns.append( str( getLine( lines, funcs[ func_var ], if_marks, table_index, funcs ) ) )
				elif func_var == function_names[0]:
					line_var_one = "gpr"
					line_var_two = str( vars[0] )
					line_var_tre = str( len( ev ) )
					ev.append( vars[1] )
				elif vars[0] == "=":
					if vars[2] in alu_funcs:
						line_var_one = alu_conv_funcs[alu_funcs.index( vars[2] )]
						line_var_two = "gpr"
						line_var_tre = str( vars[1] )
						line_var_for = "gpr"
						line_var_fiv = str( vars[3] )
						line_var_six = "gpr"
						if func_var in user_vars:
							func_var = divided_user_vars[fn][str( func_var )]
						line_var_sev = str( func_var )
						func_var = function_names[4]
						func_num = 4
					else:
						line_var_one = "gpr"
						line_var_two = str( divided_user_vars[fn][func_var] )
						line_var_tre = str( len( ev ) )
						ev.append( vars[1] )
						func_var = function_names[0]
						func_num = 0
				elif func_var == function_names[1]:
					line_var_one = convert_var_two( vars[0] )	
					line_var_two = "gpr"
					line_var_tre = str( vars[1] )
					line_var_for = "ram"
					line_var_fiv = str( int( vars[2] ) + len( funcs ) )
				elif func_var in func_params[2][0]:
					try:
						vars[0] = int( vars[0] )
						func_var = function_names[0]
						func_num = 0
						line_var_two = "gpr"
						line_var_tre = "32"
						line_var_for = str( len( ev ) )
						ev.append( str( vars[0] ) )
						nextLine = "io output gpr 32"
					except:
						line_var_two = "output"
						line_var_tre = "gpr"
						line_var_for = str( divided_user_vars[fn][vars[0]] )
						func_var = function_names[2]
						func_num = 2
				elif func_var == function_names[2]:
					line_var_one = convert_var_one( vars[0] )
					line_var_two = "gpr"
					line_var_tre = str( vars[1] )
				elif func_var == "break":
					nextLineTwo = "poss"
					for_lns = []
					for_lns.append( "if jump" )
					for_lns.append( str( getLine( lines, m_for_out_index[get_last_for( history )], if_marks, table_index, funcs ) ) )
				elif func_var == function_names[3] + "escape":
					num = vars[1]
					nextLineTwo = "poss"
					base_num = for_index[str(num)]
					for_lns = []
					for_lns.append( "compute add ram " + str( int( base_num ) + 2 + len( funcs ) ) + " ram " + str( int( base_num ) + 1 + len( funcs ) ) + " ram " + str( int( base_num ) + 1 + len( funcs ) ) )
					for_lns.append( "if jump" )
					for_lns.append( str( int( for_lines[str(num)] ) - 1 ) )
					for_lns.append( "}" )
				elif func_var == function_names[3]:
					history.append( "for" )
					nextLineTwo = "poss"
					for_lns = []
					if vars[0] != "null":
						for_lns.append( "rom ram " + str( int( vars[3] ) + len( funcs ) ) + " " + str( len( ev ) ) )
						ev.append( str( vars[0] ) )
					if vars[1] != "null":
						for_lns.append( "rom ram " + str( int( vars[3] ) + 1 + len( funcs ) ) + " " + str( len( ev ) ) )
						ev.append( str( vars[1] ) )
					if vars[2] != "null":
						for_lns.append( "rom ram " + str( int( vars[3] ) + 2 + len( funcs ) ) + " " + str( len( ev ) ) )
						ev.append( str( vars[2] ) )
					for_lns.append( "compute compare ram " +  str( int( vars[3] ) + len( funcs ) ) + " ram " + str( int( vars[3] ) + 1 + len( funcs ) ) + " ram " + str( int( vars[3] ) + 1 + len( funcs ) ) )
					for_lns.append( "if >" )
				elif func_var == function_names[4]:
					line_var_one = str( vars[0] )
					line_var_two = "gpr"
					line_var_tre = str( vars[1] )
					line_var_for = "gpr"
					line_var_fiv = str( vars[2] )
					line_var_six = "gpr"
					line_var_sev = str( vars[3] )
				elif func_var == function_names[6]:
					line_var_one = str( vars[0] )
					line_var_two = "gpr"
					line_var_tre = str( vars[1] )
					line_var_fiv = "gpr"
					line_var_six = str( vars[2] )
				elif func_var == function_names[7] + "escape":
					nextLineTwo = "poss"
					ram_index = str( m_func_num[get_last_func(history)]-1 )
					for_lns = []
					for_lns.append( "ramset to gpr 0 ram " + ram_index )
					for_lns.append( "rom gpr 1 " + str( len( ev ) ) )
					ev.append( "4" )
					for_lns.append( "compute add gpr 1 gpr 0 gpr 0" )
					for_lns.append( "irar gpr 0" )
				elif func_var == function_names[7]:
					history.append( "func" )
					num = vars[0]
					nextLineTwo = "poss"
					for_lns = []
					for_lns.append( "if jump" )
					for_lns.append( str( func_index[str(num)] ) )
					ln_n += 1
				elif func_var == function_names[9]:
					history.append( "else" )
					nextLineTwo = "poss"
					for_lns = []
					for_lns.append( "if jump" )
					tt = ""
					for i in range( len( if_marks ) ):
						tb = False
						for j in range( len( if_marks[str(i)] ) ):
							if if_marks[str(i)][str(j)]["1"] == ln_n:
								ti = i
								tj = j
								tb = True
								break
						if tb:
							break
					for i in range( len( if_marks[str(ti)] ) ):
						if if_marks[str(ti)][str(i)]["0"] == 0:
							tt = str( getLine( lines, if_marks[str(ti)][str(i)]["1"], if_marks, table_index, funcs ) )
							for_lns.append( tt )
					ln_n += 1
					ieep = False
					for_lns.append( "}" )
				elif func_var == function_names[10]:
					history.append( "elif" )
					nextLineTwo = "poss"
					for_lns = []
					for_lns.append( "if jump" )
					tt = ""
					for i in range( len( if_marks ) ):
						tb = False
						for j in range( len( if_marks[str(i)] ) ):
							if if_marks[str(i)][str(j)]["1"] == ln_n:
								ti = i
								tj = j
								tb = True
								break
						if tb:
							break
					for i in range( len( if_marks[str(ti)] ) ):
						if if_marks[str(ti)][str(i)]["0"] == 0:
							tt = str( getLine( lines, if_marks[str(ti)][str(i)]["1"] + 1, if_marks, table_index, funcs ) )
							for_lns.append( tt )
					for_lns.append( "}" )
					if tt == "":
						print( "Error, if statement was not encoded right, 0" )
						return -1
					for_lns.append( "compute compare gpr " + str( vars[0] ) + " gpr " + str( vars[2] ) + " gpr " + str( vars[2] ) )
					for_lns.append( "if " + str( vars[1] ) )
				elif func_var == function_names[11]:
					if vars[0] == "to":
						line_var_one = "to"
						line_var_two = "gpr"
						line_var_tre = str( vars[1] )
						line_var_fiv = "ram"
						line_var_six = str( int( vars[2] ) + len( funcs ) )
					elif vars[0] == "from":
						line_var_one = "from"
						line_var_two = "gpr"
						line_var_tre = str( int( vars[1] ) )
						line_var_fiv = "ram"
						line_var_six = str( int( vars[2] ) + len( funcs ) )
				elif func_var == function_names[12]:
					pass
				elif func_var == inscape_escape[1]:
					if t == function_names[9] or t == function_names[10]:
						ieep = False
					else:
						for i in range( len( if_marks ) ):
							for j in range( len( if_marks[str(i)] ) ):
								if if_marks[str(i)][str(j)]["1"] == ln_n and if_marks[str(i)][str(j)]["0"] == 0 and if_marks[str(i)][str(int(j)-1)]["0"] == 1:
									ieep = False
									break
							if ieep == False:
								break
						if ieep:
							il -= 1
				else:
					if func_param_types[func_num][1] == "con":
						line_var_one = convert_var_one( vars[0] )
					else:
						line_var_one = str( vars[0] )
					if func_param_types[func_num][2] == "con":
						line_var_two = convert_var_two( vars[1] )
					else:
						line_var_two = str( vars[1] )
					if func_param_types[func_num][3] == "con":
						line_var_tre = convert_var_tre( vars[2] )
					elif func_param_types[func_num][3] == "None":
						line_var_tre = ""
					else:
						line_var_tre = str( vars[2] )
					if func_param_types[func_num][4] == "con":
						line_var_for = convert_vars[3]( vars[3] )
					else:
						line_var_for = str( vars[3] )
				vars[3] = ""
				if func_var != function_names[3] and func_var != function_names[3] + "escape" and func_var != function_names[7] and func_var not in funcs and func_var != function_names[9] and func_var != function_names[10]:
					full_line_function = convert_func_var( func_var )
					if line_var_one != "":
						full_line_function += " " + line_var_one
					if line_var_two != "":
						full_line_function += " " + line_var_two
					if line_var_tre != "":
						full_line_function += " " + line_var_tre
					if line_var_for != "":
						full_line_function += " " + line_var_for
					if line_var_fiv != "":
						full_line_function += " " + line_var_fiv
					if line_var_six != "":
						full_line_function += " " + line_var_six
					if line_var_sev != "":
						full_line_function += " " + line_var_sev
		if ieep == False:
			ieep = True
		elif func_var == inscape_escape[0] or func_var == inscape_escape[1]:	#Write final line to destination file
			fh.write( func_var + "\n" )
			s_ln += 1
		elif run_info[func_num] != 1 and func_var != "break":
			if func_var != function_names[3] + "escape" and func_var != function_names[7] + "escape" and func_var not in funcs:
				if func_var == if_name[0] and vars[1] in if_names:
					pass 
				else:
					fh.write( full_line_function + "\n" )
					s_ln += 1
					if isinstance( nextLine, str ):
						fh.write( nextLine + "\n" )
						s_ln += 1
		if isinstance( nextLineTwo, str ):
			nextLineTwo = None
			for i in for_lns:
				fh.write( i + "\n" )
				s_ln += 1
		ln_n += 1
	fh.write( "eof \n" )
	for i in ev:	#Write variables to end of file
		fh.write( str( i ) + "\n" )
	fh.close()
	return 1

