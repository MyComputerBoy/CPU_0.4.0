
#Schön Low Level Compiler for Schön Core Delta v.0.4.0


import basecpuinf

import importlib as il 
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
	[	"if", "irar", ],
	[	"rom", "ramset", "io", "gbl", "rar", "oar", ],
	[	"compute" ],
	[	"mark",	"else",	"elif",	"pass", ],
]
#Start end indicator
sei = [ "{", "}", ]
#To from names
tfn = [ "to", "from", ]
#Register names in order
regs = ["gpr","alur","ram","spr"]

function_params = [
	[	#Setup special parameters, at the moment only if is implemeted, thus only the if operators
		[">", "==", ">=", "<", "!=", "<=", "weird", "co", ">c", "==c", ">=c", "<c", "!=c", "<=c", "jump",],
		["jump"],
	],
	[	#Setup general function parameters, True=types of regs, False=to/from, None=nan (copy user input in general), "pass"=stop checking for parameters
		[	[True], [None], ["pass"], ],
		[	[False],[True], [None], [True],[None], ],
		[	["input","output",],    [True],[None], ],
		[	[True], [None], ["pass"], ],
		[	[False],[True], [None], [True],[None], ],
		[	[True], [None], ["pass"], ],
	],
	[	#Setup special device parameters (e.g. ALU)
		[	["add","sub","mul","div","and","or","xor","not","shift","","","","","","","compare"], [True],[None],[True],[None],[True],[None], ],
	],
]
#Function parameter offset for skipped variables
function_param_offset = [
	[
		0, 0,
	],
	[
		1, 0, 0, 0, 0, 0,
	],
	[
		0,
	],
]
#Amount of variables expected
function_var_amount = [
	[
		1,
		1,
	],
	[
		2,
		5,
		3,
		2,
		5,
		2,
	],
	[
		[ 7 ],
	],
]
#EOF indicator name
eof = "eof"

var_excp = [
	[	#Functions that need no variables
		sei[0],sei[1],eof,function_names[3][1],
	],
	[	#Functions that need only first variables
		function_names[0][0],
		function_names[1][5],
		function_names[3][0],
		function_names[3][2],
	],
]
#Get function parameter index
def getParIndex( indx=[0,0,0], var="" ):
	temp_par = function_params[indx[0]][indx[1]][indx[2]][0]
	if temp_par == True:
		return regs.index( var )
	elif temp_par == False:
		return tfn.index( var )
	elif temp_par == None:
		return int( var )
	elif temp_par == "pass":
		return "pass"
	else:
		try:
			return function_params[indx[0]][indx[1]][indx[2]].index( var )
		except:
			return temp_par.index( var )
#Write to file exception
wtf_excp = [
	sei[0],
	sei[1],
	function_names[3][0],
	"",
]
#Function to manage if statements
def inline( bool, line, filename, used_in_escape ):
	fh = open( bf + pf + filename, "r" )
	lines = fh.readlines()
	fh.close()
	if bool:
		if used_in_escape == 1 and sei[1] in lines[line]:
			return False
		else:
			return True
	else:
		if sei[0] in lines[line]:
			return False
		else:
			return True

def getFuncNum( func_var, bool=False ):
	if bool == False:
		m = 1
	else:
		m = 0
	if func_var in function_names[1]:
		return function_names[1].index( func_var ) + 1 * m
	elif func_var in function_names[2]:
		return function_names[2].index( func_var ) + 15 * m

def getBinLine( lines, line, marks ):
	blns = {
		function_names[1][0]: 2,
		function_names[1][1]: 2,
		function_names[3][0]: 0,
		function_names[3][1]: 1,
		function_names[3][2]: 3,
		sei[1]: 0,
	}
	l = 0
	bin_rel_ln = 0
	for i in range( line ):
		gblln = lines[l].split()
		gblf = gblln.pop( 0 )
		if gblf in blns:
			bin_rel_ln += blns[gblf]
		elif gblf in marks:
			bin_rel_ln += 2
		else:
			bin_rel_ln += 1
		l += 1
	return bin_rel_ln
#Function to manage if statement order
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

def find_marks( lines ):
	marks = dict()
	if_marks = dict()
	vars = ["","","",""]
	iml = []
	ln = 0
	for line in lines:
		func = line.split()
		try:
			func_snd = lines[ln+1].split()
			func_snd_var = func_snd.pop( 0 )
		except:
			func_snd = None
		func_var = func.pop( 0 )
		for i in range( 3 ):
			try:
				vars[i] = func.pop( 0 )
			except:
				vars[i] = None
		if func_var == function_names[3][0]:
			marks[vars[0]] = ln 
		elif func_var == function_names[0][0] and func_snd_var != function_names[3][0] and func_snd_var != function_names[3][1] and vars[0] != "jump":
			if_marks[ str( len( if_marks ) ) ] = dict()
		elif func_var == function_names[3][1]:
			ts = str( len( if_marks ) - 1 )
			ts = gin( if_marks, ts )
			tss = str( len( if_marks[ ts ] ) )
			lines[ln] = function_names[8] + " # " + str( ts ) + " " + str( tss )
			if_marks[ ts ][tss] = {'0': 1, '1': ln}
		elif func_var == function_names[3][2]:
			ts = str( len( if_marks ) - 1 )
			ts = gin( if_marks, ts )
			tss = str( len( if_marks[ ts ] ) )
			if vars[1] != None:
				lines[ln] = function_names[9] + " " + str( vars[0] ) + " " + str( vars[1] ) + " " + str( vars[2] ) + " # " + str( ts ) + " " + str( tss )
			else:
				lines[ln] = function_names[9] + " " + str( vars[0] ) + " # " + str( ts ) + " " + str( tss )
			if_marks[ ts ][tss] = {'0': 2, '1': ln}
		elif func_var == sei[0]:
			ts = str( len( if_marks ) - 1 )
			ts = gin( if_marks, ts )
			tss = str( len( if_marks[ ts ] ) )
			if_marks[ ts ][tss] = {'0': 0, '1': ln}
		ln += 1
	return marks, if_marks

#Test For Binary Or Hexadicmal
def tfbh( var ):
	if var == "0b" + var[2:]:
		return False
	elif var == "0x" + var[2:]:
		return False
	else:
		return True

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

def comp( filename, dest_name ):
	fh = open( bf + pf + filename )
	lines = fh.readlines()
	fh.close()
	fh = open( bf + exeff + dest_name + ".schonexe", "w+" )
	ln_n = 0
	bin_ln = 0
	il = 0
	ignore_ln = []
	marks, if_marks = find_marks( lines )
	eofln = 0
	for i in lines:
		if eof in i:
			break 
		eofln += 1
	if show_adv_inf == "yes":
		print( "EOL: " + str( eofln ) )
		print( "IF_MARKS: " )
		print( if_marks )
	eofbln = getBinLine( lines, eofln, marks )
	while ln_n < len( lines ):
		if show_adv_inf == "yes":
			print( "ln_n: " + str( ln_n ) )
		line = lines[ln_n].split()
		func_var = line.pop( 0 )
		try:
			sline = lines[ln_n+1].split()
			sfunc_var = sline.pop( 0 )
		except:
			sfunc_var = None
		full_binary_function = [0 for i in range( bw )]
		nextLines = [None,None,None]
		vars = ["","","","","","",""]
		t = lines[ln_n]
		tt = gvt( t )
		if tt == "bin":
			lines[ln_n] = str( bm.btd([int(i) for i in t[2:]]) )
		elif tt == "hex":
			lines[ln_n] = str( bm.htd( t[2:] ) )
		elif tt == "int":
			pass
		else:
			if func_var not in var_excp[0] and func_var not in marks:
				try:
					vars[0] = line.pop( 0 )
				except:
					print( "Error: ln " + str( ln_n ) + ", Variable one missing" )
					return -1
				vars[2] = ""
				if func_var not in var_excp[1]:
					try:
						vars[1] = line.pop( 0 )
					except:
						print( "Error: ln " + str( ln_n ) + ", Variable two missing" )
						return -1
					if func_var in sei:
						vars[2], vars[3] = ("",)*2
					for i in range( 2, 7 ):
						try:
							vars[i] = line.pop( 0 )
						except:
							break
			iint = 0
			for i in vars:
				try:
					t = vars[iint][2:]
					tt = gvt( vars[iint] )
					if tt == "bin":
						vars[iint] = str( bm.btd([int(i) for i in t]) )
					elif tt == "hex":
						vars[iint] = str( bm.htd(t) )
				except:
					pass
				iint += 1
		bin_rel_ln = 0
		if func_var == eof:
			full_binary_function = bm.dtb( -1 )
		elif func_var == function_names[0][0]:
			if vars[0] == function_params[0][1][0]:
				full_binary_function[18] = 1
				nextLines[0] = bm.dtb( getBinLine( lines, int( lines[ln_n+1] ), marks ) )
				ln_n += 1
			else:
				il += 1
				rel_ln = 1
				used_in_escape = 1
				try:
					temp_unused_var = lines[ln_n + rel_ln]
				except:
					print( "Error: ln " + str( ln_n + 1 ) +": Expected if inscape, got none" )
					return -1
				rel_rel_ln = 1
				iblns = {
					function_names[1][0]: 2,
					function_names[1][1]: 2,
					function_names[3][0]: 0
				}
				while inline( True, ln_n + 1 + rel_rel_ln, filename, used_in_escape ):
					try:
						temp_unused_var = lines[ln_n + rel_ln + rel_rel_ln].split()
						temp_func = temp_unused_var.pop( 0 )
						try:
							temp_var = temp_unused_var.pop( 0 )
						except:
							temp_var = ""
						try:
							temp_temp_unused_var = lines[ln_n + rel_ln + rel_rel_ln + 2].split()
							temp_temp_func = temp_temp_unused_var.pop( 0 )
						except:
							temp_temp_func = ""
						if temp_func in iblns:
							bin_rel_ln += iblns[temp_func]
						elif temp_func == sei[0]:
							used_in_escape += 1
							bin_rel_ln += 1
						elif temp_func == sei[1] and used_in_escape > 1:
							used_in_escape -= 1
						elif temp_func in marks:
							bin_rel_ln += 2
						else:
							bin_rel_ln += 1
						rel_rel_ln += 1
						try:
							temp_unused_var = lines[ln_n + 1 + rel_rel_ln]
						except:
							print( "Error: ln " + str( ln_n + 1 ) +": Expected if escape, got none, 0" )
							return -1							
					except:
						print( "Error: ln " + str( ln_n + 1 ) +": Expected if escape, got none, 1" )
						return -1
				if temp_temp_func == function_names[3][1] or temp_temp_func == function_names[3][2]:
					bin_rel_ln += 2
				nextLines[0] = bm.dtb( bin_ln + 2 + bin_rel_ln )
				bin_vars[0] = bm.dtb( function_params[0][0].index( vars[0] )+1, 4 )
				for i in range( 4 ):
					full_binary_function[i+5] = bin_vars[0][i]
		elif func_var in marks:
			full_binary_function[18] = 1
			bin_rel_ln = getBinLine( lines, marks[func_var], marks )
			nextLines[0] = bm.dtb( bin_rel_ln )
		elif func_var == function_names[0][1]:
			bin_vars[1] = bm.dtb( getParIndex( [1,0,0],vars[0] ), 2 )
			bin_vars[2] = bm.dtb( getParIndex( [1,0,1],vars[1] ), 5 )
			for i in range( 2 ):
				full_binary_function[i+ 9] = bin_vars[1][i]
			full_binary_function[30] = 1
		elif func_var == function_names[3][1]:
			full_binary_function[18] = 1
			nextLines[0] = None
			t = if_marks[ str( il - 1 ) ]
			for i in range( len( t ) ):
				if t[str(i)]["0"] == 0:
					nextLines[0] = bm.dtb( getBinLine( lines, t[str(i)]["1"], marks ) )
					break
			if nextLines[0] == None:
				print( "Error, if statement was not encoded right, 0" )
				return -1
		elif func_var == function_names[3][2]:
			full_binary_function = [0 for i in range( bw )]
			t_bin_vars[0] = bm.dtb( getParIndex( [0,0,0],vars[0] ) + 1 )
			nextLines[0] = None
			nextLines[1] = [0 for i in range( bw )]
			for i in range( 4 ):
				nextLines[1][i+5] = t_bin_vars[0][i]
			nextLines[2] = None
			t = if_marks[ str( il - 1 ) ]
			for i in range( len( t ) ):
				if t[str(i)]["0"]  == 0:
					nextLines[0] = bm.dtb( getBinLine( lines, t[str(i)]["1"], marks ) )
					break
			for i in range( len( t ) ):
				if t[str(i)]["1"]  == ln_n:
					tn = i
					break
			try:
				tnn = t[str(tn+1)]["0"]
			except:
				tnn = None
			if tnn == None:
				nextLines[2] = nextLines[0]
			else:
				if tnn == 0:
					nextLines[2] = bm.dtb( getBinLine( lines, t[str(tn+1)]["1"], marks ) )
				elif tnn == 1 or tnn == 2:
					nextLines[2] = bm.dtb( getBinLine( lines, t[str(tn+1)]["1"] + 2, marks ) )
			if nextLines[0] == None:
				print( "Error, if statement was not encoded right, 1" )
				return -1
		elif func_var == sei[1] and sfunc_var != function_names[3][1] and sfunc_var != function_names[3][2]:
			il -= 1
		elif func_var in sei or func_var == function_names[3][0] or func_var == "":
			pass
		else:
			t = gvt( lines[ln_n] )
			tt = lines[ln_n].rstrip()
			if t == "bin":
				full_binary_function = bm.dtb(bm.btd([int(i) for i in tt[2:]]))
			elif t == "hex":
				full_binary_function = bm.dtb(bm.htd(tt[2:]))
			elif t == "int":
				full_binary_function = bm.dtb(int( tt ))
			else:
				func_num = getFuncNum( func_var )
				f_func_num = getFuncNum( func_var, True )
				bin_func = bm.dtb( func_num, 4 )
				bvl = [ 4,2,5,2,5,2,5 ]
				bvi = [ 5,9,11,16,18,23,25 ]
				bin_vars = []
				for j in range( 7 ):
					bin_vars.append( [0 for k in range( bvl[j] )] )
				if func_var == function_names[2][0]:
					is_alu = 1
					bin_func = bm.dtb( getParIndex( [2,0,0], vars[0] ), 4 )
					if vars[0] == function_params[2][0][0][8]:
						bin_vars[0] = bm.dtb( 1, 4 )
					for i in range( 1, 7 ):
						bin_vars[i] = bm.dtb( getParIndex( [2,0,i], vars[i] ), bvl[i] )
				else:
					is_alu = 0
					function_names_index = function_names[1].index( func_var )
					for i in range( function_var_amount[1][function_names_index] ):
						try:
							temp_type = function_params[1][f_func_num][i][0]
						except:
							break
						fpo = function_param_offset[1][function_names_index]
						bin_vars[fpo + i] = bm.dtb( getParIndex( [1,function_names_index,i], vars[i] ), bvl[i + fpo] )
						if bin_vars[i] == "pass":
							bin_vars[i] = None
							break
						if func_var == function_names[1][0]:
							nextLines[0] = bm.dtb( eofbln + int( vars[2] ) + 1 )
						elif func_var == function_names[1][1]:
							nextLines[0] = bm.dtb( int( vars[4] ) )
				full_binary_function[4] = is_alu
				for i in range( 4 ):
					full_binary_function[i] = bin_func[i]
				for i in range( len( bvl ) ):
					for j in range( bvl[i] ):
						full_binary_function[ bvi[i] + j ] = bin_vars[i][j]
		if func_var not in wtf_excp:
			fh.write( bm.blts( full_binary_function ) + "\n" )
			bin_ln += 1
			for i in range( len( nextLines ) ):
				if isinstance( nextLines[i], list ):
					fh.write( bm.blts( nextLines[i] ) + "\n" )
					bin_ln += 1
		ln_n += 1
	fh.close()
