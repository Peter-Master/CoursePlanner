# by Peter Master, Alex Vossmeyer
# 1/21/17
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
# 1) Area A1 and Area A2 courses count towards only A1 and A2 respectively,
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



import re



areaBFile = open("b.txt")
areaBList = bFile.read()
newAreaBList = areaBList.split("\n")

areaCFile = open("c.txt")
areaCList = cFile.read()
newAreaCList = areaCList.split("\n")

culturesFile = open("cultures.txt")
culturesList = culturesFile.read()
newCulturesList = culturesList.split("\n")

ethnicityFile = open("ethnicity.txt")
ethnicityList = ethnicityFile.read()
newEthnicityList = ethnicityList.split("\n")

europeanFile = open("european.txt")
europeanList = europeanFile.read()
newEuropeanList = europeanList.split("\n")

quantitativeFile = open("quantitative.txt")
quantitativeList = quantitativeFile.read()
newQuantitativeList = quantitativeList.split("\n")

writingFile = open("writing.txt")
writingList = writingFile.read()
newWritingList = writingList.split("\n")



# for i in range(0,len(newsymbollist)):
# url = "https://my.sa.ucsb.edu/catalog/2012-2013/UndergraduateEducation/WritingReqCourses.aspx"
# htmlfile = urllib.urlopen(url)
# htmltext = htmlfile.read()
# regex = '<p style="text-indent: -10px; margin-top: 0px; margin-bottom: 0px; padding: 0px; margin-left: 23px;">'
# pattern = re.compile(regex)
# course = re.findall(pattern, htmltext)
# print course
