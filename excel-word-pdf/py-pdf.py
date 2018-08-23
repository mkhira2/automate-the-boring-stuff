import PyPDF2, os

# download example pdfs from:
# http://autbor.com/meetingminutes1.pdf
# http://autbor.com/meetingminutes2.pdf

# rb = read binary, wb = write binary
# necessary for pdf files

os.chdir('c:\\users\\mkhir\\documents')
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages) # print number of pages

page = reader.getPage(0)
print(page.extractText()) # print text from page 1

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText()) # print all pdf text

# combining pdf's

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile) # writes new pdf to hard drive

outputFile.close()
pdf1File.close()
pdf2File.closer()
