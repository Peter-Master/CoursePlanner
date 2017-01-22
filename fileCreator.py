import urllib
import re
import time

areaAFile = open("a.txt")
areaAList = aFile.read()
newAreaAList = areaAList.split("\n")

culturesFile = open("cultures.txt")
culturesList = culturesFile.read()
newCulturesList = culturesList.split("\n")

europeanFile = open("european.txt")
europeanList = europeanFile.read()
newEuropeanList = europeanList.split("\n")

ethnicityFile = open("ethnicity.txt")
ethnicityList = ethnicityFile.read()
newEthnicityList = ethnicityList.split("\n")

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
