
#Schön Core Delta v.0.5.0 python Edition


#Import libraries
import basecpuinf

import math
import bm
import rom
import stdn_gate as g 
import importlib as il
import time

#All types of memory storage units, including ram and registers
ram = [

	bm.dtb(0) for i in range(1024)	#Random Access Memory, emulated 1024, but is capable of 4.294.967.296

]

regs = [
	[bm.dtb(0) for i in range(32)],	#General Purpose Registers
	[bm.dtb(0) for i in range(32)],	#Arithmetic/Logic Unit Registers
	[bm.dtb(0) for i in range(32)],	#Stack Pointers
	[bm.dtb(0) for i in range(32)],	#Interrup Stack Pointers
]

buffer = bm.dtb(0)

#Functions to manage buffer, registers and other memory storage units
def buf(rw, list=bm.dtb(0)):
	global buffer 
	if rw == 0:
		return buffer 
	
	buffer = list

def reg(rw, index, list=[0,0]):
	global regs
	try:
		list[0] = bm.dtb(list[0])
	except Exception:
		pass 
	if rw == 0:
		return regs[int(list[1])][int(index)]
	
	regs[int(list[1])][int(index)] = list[0]

def rar(rw, index, list=[0,0], bt=0):
	global regs 
	try:
		list[0] = bm.dtb(list[0])
	except Exception:
		pass 
	if rw == 0:
		t = bm.btd(regs[list[1]][index])
		return regs[bm.btd(list[0])][t]
		
	t = bm.btd(regs[list[1]][index])
	regs[bm.btd(bt)][t] = list[0]
		

def oar(index, list=[0,0]):
	global regs
	return rom.rom(0, regs[list[1]][index])

#Basic CPU info variables
bw = basecpuinf.bit_width

bf = basecpuinf.base_folder
pf = basecpuinf.programs_folder
exeff = basecpuinf.executable_files_folder

ena_list = reg(0, 2,[0,3])
set_list = reg(0, 1,[0,3])

#Test ALU
try:
	if set_list[8] == 1:
		tmp = buf(0)
		reg(1, 0, [tmp,1])

	if ena_list[1] == 1:
		var = reg(0, 1, [0,1])
		buf(1, var)
except Exception:
	print("Internal ALU: -1")

#Setup ALU

def la(la, lb, ci=0):
	a = bm.btd(la)
	b = bm.btd(lb)
	tq = a + b + ci
	if math.sqrt(tq**2) >= 2**bw:
		ci = 1
	return bm.dtb(tq), ci

def ls(la, lb, ci=0):
	a = bm.btd(la)
	b = bm.btd(g.nl(lb))
	ci = 1-ci
	tq = a + b + ci
	if math.sqrt(tq**2) >= 2**bw:
		ci = 1
	return bm.dtb(tq), ci

def mul(al, bl):
	a = bm.btd(al)
	b = bm.btd(bl)
	return bm.dtb(a * b)

def div(al, bl):
	a = bm.btd(al)
	b = bm.btd(bl)
	return bm.dtb(math.floor(a / b))

def mod(n, b):
	return n-math.floor(n/b) * b

def shift(list, leng, ud=1):
	if ud == 1:
		tq = bm.dtb(math.floor( bm.btd(list) * 2**leng))
		return tq, list[mod(bw-leng,bw)]
	
	tq = bm.dtb(math.floor(bm.btd(list) / 2**leng))
	return tq, list[mod(leng-1,bw)]

def alu():		#//Update for new ALU
	global reg
	spec_func_var = reg(0, 6, [0,3])
	ena_list = reg(0, 2,[0,3])
	set_list = reg(0, 1,[0,3])
	ln = reg(0, 0, [0,3])
	num_a = buf(0)
	if ena_list[2] == 0:
		num_b = reg(0, 0, [0,1])
	else:
		num_b = bm.dtb(1)
	func = reg(0, 2, [0,1])
	tmp = [0 for i in range(4)]
	for i in range(4):
		tmp[i] = func[i]
	func = bm.blts(tmp)
	tmp_a = bm.btd(num_a)
	tmp_b = bm.btd(num_b)
	co = 0
	if tmp_a > tmp_b:
		comp = [1,0,0]
	elif tmp_a == tmp_b:
		comp = [0,1,0]
	else:
		comp = [0,0,1]
	q = []
	if func == "0000":
		q, co = la(num_a, num_b)
	elif func == "1000":
		q, co = ls(num_a, num_b)
	elif func == "0100":
		q = mul(num_a, num_b)
	elif func == "1100":
		q = div(num_a, num_b)
	elif func == "0010":
		q = g.al(num_a, num_b)
	elif func == "1010":
		q = g.ol(num_a, num_b)
	elif func == "0110":
		q = g.xl(num_a, num_b)
	elif func == "1110":
		q = g.nl(num_a)
	elif func == "0001":
		if bm.btd(spec_func_var) == 1:
			q, co = shift(num_b, bm.btd(num_a), 0)
		else:
			q, co = shift(num_b, bm.btd(num_a))
	elif func == "1111":
		q = num_b
	else:
		print("Error: In alu, ln " + str(bm.btd(ln)) + ", No such function")
		raise Exception
	comp.append(co)
	reg(1, 1, [q,1])
	if set_list[7] == 1:
		reg(1, 3, [comp,1])
	return 1

#Setup Processor
func_descr = [
	[
		[				#If set 
			[0,0,0,0,1,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0,0,0,0,0],
		],
		[				#ROM set 
			[0,1,0,0,1,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,1,0,0,0,0],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		],
		[				#RAM to set 
			[0,1,0,0,1,0,0,0,0,0,0,0,0,0],
			[0,0,1,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,1,0,0,0,0],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		],
		[				#RAM from set 
			[0,1,0,0,1,0,0,0,0,0,0,0,0,0],
			[0,0,1,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,1,0,0,0,0,0,0,0,0,0,0],
			[1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		],
		[				#IO input set 
			[0,0,0,0,0,0,0,0,0,1,0,0,0,0],
		],
		[				#IO output set 
			[0,0,0,0,0,1,0,0,0,0,0,0,0,0],
		],
		[				#Get Binary Line (gbl) set 
			[0,1,0,0,0,0,0,0,0,1,0,0,0,0],
		],
		[				#RAR to set 
			[0,0,0,0,0,0,0,0,0,0,0,0,0,1],
		],
		[				#RAR from set 
			[0,0,0,0,0,0,0,0,0,1,0,0,0,0],
		],
		[				#OAR from set
			[0,0,0,0,1,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,1,0,0,0,0],
		]
	],
	[
		[				#If ena 
			[1,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
		],
		[				#ROM ena 
			[1,0,1,0,0,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
			[0,1,0,0,0,0,0,0,0,0],
		],
		[				#RAM to ena 
			[1,0,1,0,0,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
			[0,0,0,1,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,0,0,0],
		],
		[				#RAM from ena 
			[1,0,1,0,0,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
			[0,0,0,0,0,0,1,0,0,0],
			[0,1,0,0,0,0,0,0,0,0],
		],
		[				#IO input ena 
			[0,0,0,0,0,1,0,0,0,0]
		],
		[				#IO output ena 
			[0,0,0,0,0,0,1,0,0,0]
		],
		[				#Get Binary Line (gbl) ena 
			[1,0,0,0,0,0,0,0,0,0],
		],
		[				#RAR to ena 
			[0,0,0,0,0,0,1,0,0,0],
		],
		[				#RAR from ena 
			[0,0,0,0,0,0,0,0,0,1],
		],
		[				#OAR from ena
			[0,0,0,0,0,0,1,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
		]
	]
]

irar_descr = [
	[
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0]
	],
	[
		[0,0,0,0,0,0,1,0,0,0]
	]
]

func_def = [ 1, 0, 0, 0, 0, 0, 0, 0, 0 ]

fetch = [
	[
		[0,1,0,0,1,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,0]
	],
	[
		[1,0,1,0,0,0,0,0,0,0],
		[0,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,0,0,0,0,0]
	]
]

alu_descr = [
	[
		[0,0,0,0,0,0,0,0,1,0,0,0,0,0],
		[0,1,0,0,0,0,0,1,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,1,0,0]
	],
	[
		[0,0,0,0,0,0,0,1,0,0],
		[0,0,0,0,0,0,1,0,0,0],
		[0,1,0,0,0,0,0,0,0,0]
	]
]

next_address = [
	[
		[0,1,0,0,1,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0]
	],
	[
		[1,0,1,0,0,0,0,0,0,0],
		[0,1,0,0,0,0,0,0,0,0]
	]
]

set_address = [
	[
		[1,0,0,0,0,0,0,0,0,0,0,0,0,0]
	],
	[
		[0,0,0,0,1,0,0,0,0,0]
	]
]

#Clear Registers
def cls(r=0, g=0, b=0):
	rll, rlw = ram.gl()
	if b == 1:
		buf(1, bm.dtb(0))
	if r == 1:
		for i in range(rll-1):
			ram.ram(1, i, bm.dtb(0))
	if g == 1:
		for i in range(70):
			reg(1, i, [bm.dtb(0),0])
		for i in range(22):
			reg(1, i, [bm.dtb(0),1])
		for i in range(7):
			reg(1, i, [bm.dtb(0),3])
		reg(1, 1, [[0,0,0,0,0,0,0,0,0,0,0,0,0],3])
		reg(1, 2, [[0,0,0,0,0,0,0,0],3])
		reg(1, 2, [[0,0,0,0],1])
		reg(1, 3, [[0,0,0,0],1])

def pr(lst, gui=False):#Print function
	if gui == True:
		print(str(bm.blts(lst, False, True)))
	elif gui == "not":
		print(str(bm.btd(lst)))
	elif gui == "bin":
		print(bm.btbs(lst))
	else:
		print("Output: " + str(bm.btd(lst)))

#Set Set Pins
def set(list):		#pc, aor, rama, ramd, roma, gpoa, gpod, flg, airb, rega, regb, regc, cui, rarb
	reg(1, 1, [list,3])

#Set Enable Pins
def enable(list):		#pc, aor, ai_one, ramd, romd, gpi, rega, regb, regc, rara
	reg(1, 2, [list,3])

def sr(lst, comp):	#Should Run?
	for i in range(4):
		if g.a(comp[i], lst[i]) == 1:
			return False 
	return True

def ofs(func, var_a):	#Offset
	
	try:
		ofs_array		= [0, 1, 2, 4, 6, 7, 9]
		ofs_use_var_a	= [0, 0, 1, 1, 0, 1, 0]
		
		return ofs_array[func] + (ofs_use_var_a[func]*bm.btd(var_a))
	except Exception:
		return "Error"

def sa(bool):				#Set Address
	if bool:
		iint = 0
		for i, _ in enumerate(set_address):
			execute(set_address[0][i], set_address[1][i], bm.btd(reg_a))

#Define actions dictated by set/enable pins
def execute(set_list, ena_list, gui=False, reg_a=[0,0], reg_b=[0,0], reg_c=[0,0]):
	global reg
	set(set_list)
	enable(ena_list)
	var = bm.dtb(0)
	
	#Enable actions:
	if ena_list[0] == 1:	#pc 
		var = reg(0, 0, [0,3])
		buf(1, var)
	if ena_list[1] == 1:	#aor 
		var = reg(0, 1, [0,1])
		buf(1, var)
	if ena_list[3] == 1:	#ramd 
		tmp = reg(0, 3, [0,3])
		var = reg(0, bm.btd(tmp), [0,2])
		buf(1, var)
	if ena_list[4] == 1:	#romd 
		tmp = reg(0, 4, [0,3])
		var = rom.rom(0, bm.btd(tmp))
		buf(1, var)
	if ena_list[5] == 1:	#gpi 
		var = bm.dtb(int(input("Number: ")))
		buf(1, var)
	if ena_list[6] == 1:	#rega 
		var = reg(0, reg_a[0], [0,reg_a[1]])
		buf(1, var)
	if ena_list[7] == 1:	#regb 
		var = reg(0, reg_b[0], [0,reg_b[1]])
		buf(1, var)
	if ena_list[8] == 1:	#regc
		var = reg(0, reg_c[0], [0,reg_c[1]])
		buf(1, var)
	if ena_list[9] == 1:	#rara
		var = rar(0, reg_b[0], [reg_a[1],reg_b[1]], reg_b[1])
		buf(1, var)
		
	var = buf(0)
	
	#Set actions:
	if set_list[0] == 1:	#pc
		reg(1, 0, [var, 3])
	if set_list[1] == 1:	#aor
		alu_r = alu()
		if alu_r != 1:
			raise Exception
	if set_list[2] == 1:	#rama
		reg(1, 3, [var,3])
	if set_list[3] == 1:	#ramd
		tmp = reg(0, 3, [0,3])
		reg(1, bm.btd(tmp), [var,2])
	if set_list[4] == 1:	#roma
		reg(1, 4, [var,3])
	if set_list[5] == 1:	#gpoa
		pr(var, gui)
	if set_list[6] == 1:	#gpod
		print("")
		print("OUTPUT: " + str(bm.btd(var)))
	if set_list[7] == 1:	#flg
		pass
	if set_list[8] == 1:	#airb
		reg(1, 0, [var,1])
	if set_list[9] == 1:	#rega
		reg(1, reg_a[0], [var,reg_a[1]])
	if set_list[10] == 1:	#regb
		reg(1, reg_b[0], [var,reg_b[1]])
	if set_list[11] == 1:	#regc
		reg(1, reg_c[0], [var,reg_c[1]])
	if set_list[12] == 1:	#cui
		reg(1, 5, [var,3])
	if set_list[13] == 1:	#rarb
		rar(1, reg_b[0], [var,reg_b[1]], reg_b[1])

#Run Single Instruction
def single_instruction(r=0, gui=False, print_line_nr=False, force_show_exceptions=False):
	global reg
	#il.reload(gpr)
	if r == 1:	#Reset
		buf(1, bm.dtb(0))
		for i, _ in enumerate(regs):
			for j, _ in enumerate(regs[i]):
				reg(1, j, [bm.dtb(0),i])
		reg(1, 1, [[0,0,0,0,0,0,0,0,0,0,0,0,0],3])
		reg(1, 2, [[0,0,0,0,0,0,0,0],3])
		reg(1, 2, [[0,0,0,0],1])
		reg(1, 3, [[0,0,0,0],1])
		
		return 0
			#Run instruction
	ln = reg(0, 0, [0,3])
	
	reg(1, 2, [0,1])
	
	#fetch next instruction 
	for i, _ in enumerate(fetch[0]):
		execute(fetch[0][i], fetch[1][i])
	inp = reg(0, 5, [0,3])
	
	if print_line_nr:
		print("ln: %s, %s" % (bm.btd(ln),bm.blts(inp)))
	
	#if input is all 1s, exit with return code 1
	if inp == bm.dtb(-1):
		return 1
		
	comp = reg(0, 3, [0,1])
	
	#get input variables
	
	#Length of variables 
	var_lengs = [4,4,7,7,7,2]
	var_ofs = [0]
	
	temp_leng = 1
	for i, _ in enumerate(var_lengs):
		try:
			temp_leng += var_lengs[i]
			var_ofs[i+1] = temp_leng
		except Exception:
			if force_show_exceptions:
				print("indexerror: list assignment index out of range")
	
	#Where the different variables start in input space
	var_ofs = [0, 5, 9, 16, 23, 30]
	
	#Create variables according to lengths
	func  = [0 for i in range(var_lengs[0])]
	var_a = [0 for i in range(var_lengs[1])]
	reg_a = [0 for i in range(var_lengs[2])]
	reg_b = [0 for i in range(var_lengs[3])]
	reg_c = [0 for i in range(var_lengs[4])]
	var_b = [0 for i in range(var_lengs[5])]
	
	#Populate variables according to offsets and lengths
	for i, e in enumerate( func):
		func[ i] = inp[i + var_ofs[0]]
	for i, e in enumerate(var_a):
		var_a[i] = inp[i + var_ofs[1]]
	for i, e in enumerate(reg_a):
		reg_a[i] = inp[i + var_ofs[2]]
	for i, e in enumerate(reg_b):
		reg_b[i] = inp[i + var_ofs[3]]
	for i, e in enumerate(reg_c):
		reg_c[i] = inp[i + var_ofs[4]]
	for i, e in enumerate(var_b):
		var_b[i] = inp[i + var_ofs[5]]
	
	#convert input to ints then to registers 
	
	reg_a_int = bm.btd(reg_a)
	reg_b_int = bm.btd(reg_b)
	reg_c_int = bm.btd(reg_c)
	
	#Convert ints to register format, or [all but lower 2 bits removed as int,2 lower bits as int]
	reg_a = [math.floor((reg_a_int-(reg_a_int%4))/4),reg_a_int%4]
	reg_b = [math.floor((reg_b_int-(reg_b_int%4))/4),reg_b_int%4]
	reg_c = [math.floor((reg_c_int-(reg_c_int%4))/4),reg_c_int%4]
	
	#logic 
	if inp[4] == 1:		#if the function is an alu operation
		reg(1, 2, [func,1])
		reg(1, 6, [var_a,3])
		for i, _ in enumerate(alu_descr[0]):
			execute(alu_descr[0][i], alu_descr[1][i], gui, reg_a, reg_b, reg_c)
		return 0
	
	#else if the function is a logical operation
	if func_def[bm.btd(func)] != 1:
		try:	
			_ofs = ofs(bm.btd(func), var_a)
			if _ofs == "error":
				print("")
				print("error")
				print(func + " at line " + bm.btd(ln))
			for i, _ in enumerate(func_descr[0][_ofs]):
				execute(func_descr[0][_ofs][i], func_descr[1][_ofs][i], gui, reg_a, reg_b, reg_c)
		except exception:
			if force_show_exceptions:
				print("")
				print("error")
				print("invalid execution of function %s at line %s" % (func,bm.btd(ln))) 
		return 0
	
	if bm.btd(var_b) != 1:
		for i, _ in enumerate(next_address[0]):
			execute(next_address[0][i], next_address[1][i], gui, reg_a)
		if sr(var_a, comp):
			for i, _ in enumerate(set_address[0]):
				execute(set_address[0][i], set_address[1][i], gui, reg_a)
		return 0
	
	for i, _ in enumerate(irar_descr[0]):
		execute(irar_descr[0][i], irar_descr[1][i], gui, reg_a, reg_b)
	
	return 0
			
			
			


def run(filename, gui=False, print_line_nr=False, force_show_exceptions=False):
	
	#Open and read file for execution 
	temp_fh = open(bf + exeff + filename + ".schonexe", "r")
	lines = temp_fh.readlines()
	temp_fh.close()
	
	#Setup cpu sattelite files for executions 
	reg(1, 5, [0,3])
	single_instruction(1, gui)
	fh = open(bf + "rom/fn.txt", "w")
	fh.write(filename)
	fh.close()
	il.reload(rom)
	start_time = time.time()
	#Execute program 
	while True:
		q = single_instruction(0, gui, print_line_nr, force_show_exceptions)
		if isinstance(q, int):
			if q == 1:
				end_time = time.time()
				print("elapsed time: %s" % (end_time-start_time))
				return [1, end_time-start_time]
			elif q == -1:
				break
			elif q != 0:
				print(q)



