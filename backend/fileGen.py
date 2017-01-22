# generates multi-requirement file lists from single-requirement files
# by Peter Master, Alex Vossemeyer
# 1/21/17
#
#
# degree requirements can be found at
# https://my.sa.ucsb.edu/catalog/Current/UndergraduateEducation/GeneralSubjectAreaRequirements.aspx
# 
#
#
# INPUT:
# files that each represent a single requirement that contain all the classes
# that fulfill the respective requirement. These files should not end with a
# new line character.
#
# OUTPUT:
# files that each represent every possible combination of requirements, each
# which uniquely contains all the classes that fulfill at least that set of
# requirements
#
#
#
#
# ASSUMPTIONS:
#
# 1) 
#
#
#
# BEHAVIOR:
#
# 1) Area A1, Area A2, and Area B courses count towards only A1, A2, and B respectively;
# they do not count towards any other categories or requirements. Thus, we leave
# A1 and A2 off from our program as the user can select from the registrar's A1 and
# A2 lists completely individually of the rest of their requirements.
#
# 2) A stipulation from the registrar: "Please note that one course may only count
# toward one A-G requirement but that A-G courses may overlap with other Special
# Subject Requirements". Thus, for a user who needs at least one more course in each
# of areas D and E, a course that can cover either of area D and area E will 
# only have its fill ranking benefited by 1 rather than 2.
#
#
#
# NAMING CONVENTION:
# the 14 abbreviated categories are: amer, c, d, de, defgh, e, eth, euro, f, fg, g, quant, world, writ
#
# files are named a_b_c_d.txt where a, b, c, and d are distinct, alphabetically sorted requirements
# that are all filled by classes present in the file
#
# a class that fulfills requirements D, F, European Traditions, and Writing will be
# found in the textfiles: d.txt; de.txt; defgh.txt; d_euro.txt; de_euro.txt; defgh_euro.txt;
# d_writ.txt; de_writ.txt; defgh_writ.txt; d_euro_writ.txt; de_euro_writ.txt; defgh_euro_writ.txt;
# f.txt; fg.txt; euro_f.txt; euro_fg.txt; f_writ.txt; fg_writ.txt; euro_f_writ.txt;
# euro_fg_writ.txt
#
#
#
#
# notes to self: decide and execute on whether \r, \n, or nothing should
# be in the lists after each element -- also about what (if anything)
# should come at the end of the file
#

import re
from itertools import combinations   # for taking combinations of requirements

# open all files and store info (stripped of weird characters) in lists

pattern = re.compile(r"[^\w \-\_\"\n\,\(\)\']")
#pattern = re.compile(r" \-.*") # (RG ST 152 - blah blah blah) ---> (RG ST 152)


with open("inputLists/amer.txt") as amerFile:
	amerList = amerFile.read()
amerList = re.sub(pattern, "", amerList)
amerList = amerList.split("\n")
	
with open("inputLists/c.txt") as areaCFile:
	areaCList = areaCFile.read()
areaCList = re.sub(pattern, "", areaCList)
areaCList = areaCList.split("\n")
	
with open("inputLists/d.txt") as areaDFile:
	areaDList = areaDFile.read()
areaDList = re.sub(pattern, "", areaDList)
areaDList = areaDList.split("\n")
	
with open("inputLists/e.txt") as areaEFile:
	areaEList = areaEFile.read()
areaEList = re.sub(pattern, "", areaEList)
areaEList = areaEList.split("\n")
	
with open("inputLists/eth.txt") as ethFile:
	ethList = ethFile.read()
ethList = re.sub(pattern, "", ethList)
ethList = ethList.split("\n")
	
with open("inputLists/euro.txt") as euroFile:
	euroList = euroFile.read()
euroList = re.sub(pattern, "", euroList)
euroList = euroList.split("\n")
	
with open("inputLists/f.txt") as areaFFile:
	areaFList = areaFFile.read()
areaFList = re.sub(pattern, "", areaFList)
areaFList = areaFList.split("\n")
	
with open("inputLists/g.txt") as areaGFile:
	areaGList = areaGFile.read()
areaGList = re.sub(pattern, "", areaGList)
areaGList = areaGList.split("\n")
	
with open("inputLists/quant.txt") as quantFile:
	quantList = quantFile.read()
quantList = re.sub(pattern, "", quantList)
quantList = quantList.split("\n")
	
with open("inputLists/world.txt") as worldFile:
	worldList = worldFile.read()
worldList = re.sub(pattern, "", worldList)
worldList = worldList.split("\n")
	
with open("inputLists/writ.txt") as writFile:
	writList = writFile.read()
writList = re.sub(pattern, "", writList)
writList = writList.split("\n")




# generate de.txt, defgh.txt, fg.txt"""
areaDEList = areaDList
areaDEList.extend(areaEList)
areaDEList = list(set(areaDEList))
areaDEList.sort()
with open("outputLists/de.txt", 'w') as areaDEFile:
	areaDEFile.write("\n".join(item for item in areaDEList))

areaFGList = areaFList
areaFGList.extend(areaGList)
areaFGList = list(set(areaFGList))
areaFGList.sort()
with open("outputLists/fg.txt", 'w') as areaFGFile:
	areaFGFile.write("\n".join(item for item in areaFGList))

areaDEFGHList = areaDEList
areaDEFGHList.extend(areaFGList)
areaDEFGHList = list(set(areaDEFGHList))
areaDEFGHList.sort()
with open("outputLists/defgh.txt", 'w') as areaDEFGHFile:
	areaDEFGHFile.write("\n".join(item for item in areaDEFGHList))


# generate all combinations of one element of areas
# and one or more elements from reqs
areas = [("c",areaCList), ("d", areaDList), ("de", areaDEList), ("defgh", areaDEFGHList), ("e", areaEList), ("f", areaFList), ("fg", areaFGList), ("g", areaGList)]
reqs = {"amer": amerList, "eth": ethList, "euro": euroList, "quant": quantList, "world": worldList, "writ": writList}
reqAbbrevCombos = []
for i in range(1, len(reqs) + 1):
	reqAbbrevCombos.extend(combinations(sorted(list(reqs.keys())), i))


for areaAbbrev, areaList in areas:
	for reqAbbrevCombo in reqAbbrevCombos:
		outputList = set(areaList)
		reqAbbrevComboText = ""
		for reqAbbrev in reqAbbrevCombo:
			outputList = set(outputList) & set(reqs[reqAbbrev])
			#outputList = set(outputList).intersection(reqs[reqAbbrev])
			reqAbbrevComboText += "_" + reqAbbrev
		if outputList: # has at least one item
			with open("outputLists/" + areaAbbrev + reqAbbrevComboText + ".txt", 'w') as outputFile:
				outputList = sorted(set(outputList))
				outputFile.write("\n".join(item for item in outputList))