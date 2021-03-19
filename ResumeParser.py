#Ashish Gour
#gourashish666@gmail.com

#install following libraries
#PyPDF2
#regex

import PyPDF4
import re

#change name of pdf(also include extension)
PDFfile = open("P.pdf","rb")
pdfread = PyPDF4.PdfFileReader(PDFfile)

#Doesn't work well on resume having BOTH left and right text alignment on SAME LINE like mine
pages=pdfread.getNumPages()
for page in range(0,pages):
	text = pdfread.getPage(page).extractText()
	email_pattern = re.compile(r'[a-zA-Z0-9_+-.]+@[a-zA-Z-.]+')
	emailids = email_pattern.finditer(text)
	print("Email Id(s)")
	for emailid in emailids:
		print(emailid.group(0))

#Bonus
#Assumption: Name, greetings, or String 'Name' are first things on resume
text = pdfread.getPage(0).extractText()
name_pattern = re.compile(r'[a-zA-Z ]+')
names = name_pattern.finditer(text)
flag=0
for name in names:
	if flag == 0:
		if (name.group(0) != "Name") and (name.group(0) != "Hello") and (name.group(0) != "Hi"):
			print("Name: ", name.group(0))
			flag=1
