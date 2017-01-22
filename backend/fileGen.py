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
# toward one A‐G requirement but that A‐G courses may overlap with other Special
# Subject Requirements". Thus, for a user who needs at least one more course in each
# of areas D and E, a course that can cover either of area D and area E will 
# only have its fill ranking benefited by 1 rather than 2.
#
#
#
#
# NAMING CONVENTION:
# the 14 abbreviated categories are: amer, c, d, de, defg, e, eth, euro, f, fg, g, quant, world, writ
#
# files are named a_b_c_d.txt where a, b, c, and d are distinct, alphabetically sorted requirements
# that are all filled by classes present in the file
#
# a class that fulfills requirements D, F, European Traditions, and Writing will be
# found in the textfiles: d.txt; de.txt; defg.txt; d_euro.txt; de_euro.txt; defg_euro.txt;
# d_writ.txt; de_writ.txt; defg_writ.txt; d_euro_writ.txt; de_euro_writ.txt; defg_euro_writ.txt;
# f.txt; fg.txt; euro_f.txt; euro_fg.txt; f_writ.txt; fg_writ.txt; euro_f_writ.txt;
# euro_fg_writ.txt


# open all files

with open("inputLists/amer.txt") as amerFile:
	amerList = amerFile.read()
amerList = amerList.split("\n")
	
with open("inputLists/c.txt") as areaCFile:
	areaCList = areaCFile.read()
areaCList = areaCList.split("\n")
	
with open("inputLists/d.txt") as areaDFile:
	areaDList = areaDFile.read()
areaDList = areaDList.split("\n")
	
with open("inputLists/e.txt") as areaEFile:
	areaEList = areaEFile.read()
areaEList = areaEList.split("\n")
	
with open("inputLists/eth.txt") as ethFile:
	ethList = ethFile.read()
newEthList = ethList.split("\n")
	
with open("inputLists/euro.txt") as euroFile:
	euroList = euroFile.read()
newEuroList = euroList.split("\n")
	
with open("inputLists/f.txt") as areaFFile:
	areaFList = areaFFile.read()
areaFList = areaFList.split("\n")
	
with open("inputLists/g.txt") as areaGFile:
	areaGList = areaGFile.read()
areaGList = areaGList.split("\n")
	
with open("inputLists/quant.txt") as quantFile:
	quantList = quantFile.read()
quantList = quantList.split("\n")
	
with open("inputLists/world.txt") as worldFile:
	worldList = worldFile.read()
worldList = worldList.split("\n")
	
with open("inputLists/writ.txt") as writFile:
	writList = writFile.read()
writList = writList.split("\n")



# generate de.txt, defg.txt, fg.txt

areaDEList = areaDList
areaDEList = list(set(areaDEList.extend(areaEList)))
areaDEList.sort()
with open("outputLists/de.txt", 'w') as areaDEFile:
	areaDEFile.write("\n".join(item for item in areaDEList))

areaFGList = areaFList
areaFGList = list(set(areaFGList.extend(areaGList)))
areaFGList.sort()
with open("outputLists/fg.txt", 'w') as areaFGFile:
	areaFGFile.write("\n".join(item for item in areaFGList))

areaDEFGList = areaDEList
areaDEFGList = list(set(areaDEFGList.extend(areaFGList)))
areaDEFGList.sort()
with open("outputLists/defg.txt", 'w') as areaDEFGFile:
	areaDEFGFile.write("\n".join(item for item in areaDEFGList))




areaLists = [areaCList, areaDList, areaDEList, areaDEFGList, areaEList, areaFList, areaFGList, areaGList]
requirementLists = [amerList, ethList, euroList, quantList, worldList, writList]


