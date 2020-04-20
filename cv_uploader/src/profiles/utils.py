from PIL import Image 
import pytesseract
import sys 
from pdf2image import convert_from_path , convert_from_bytes
from PyPDF2 import PdfFileReader
import os 
import glob
from datetime import datetime
from copy import copy


def convert_pdf_to_images(pdf_name,path,name,document):
    pages = convert_from_bytes(document.file.getvalue(), 500) # Store all the pages of the PDF in a variable  
    image_counter = 1   # Counter to store images of each page of PDF to image
    outfile = str(name)+".txt" # prepare text file name 
    
    f = open(path+'/'+outfile, "a") # open the file to write into it 

    for page in pages: # Iterate through all the pages stored above 
      # For each page, filename will be:  
    # PDF page 1 -> page_1.jpg 
    # PDF page 2 -> page_2.jpg 
    # PDF page 3 -> page_3.jpg 
    # .... 
    # PDF page n -> page_n.jpg 
        filename = "page_"+str(image_counter)+".jpg" # Declaring name for each page of PDF as JPG
      
    # Save the image of the page in system 
        page.save(path+'/'+filename, 'JPEG') 
  
    # Increment the counter to update filename 
        image_counter = image_counter + 1
        print(page)
        print(path , filename)
    # convert the image into text 
        text = str(((pytesseract.image_to_string(Image.open(path+'/'+filename)))))
        text2 = str("hi")
        print(text)
    # write the text into a file in the HDD
        f.write(text) 
    f.close() 
    print('****finishing converting from pdf to jpg and applying OCR to convert the data into text*******')


def preprocess_pdf(pdf_name,document):
    # import pdb;pdb.set_trace()
    now = datetime.now()
    name = pdf_name.split('.')[0].split('/')[-1] 
    path = os.getcwd() +'/media/'+'CVS/{0}/{1}/{2}/'.format(now.year,'0'+str(now.month) if now.month <10 else now.month ,now.day)+name
    pdf_path = path+'.pdf'
    # f = open(document.read(), 'rb')
    pdf_copy = copy(document._file)
    pdf = PdfFileReader(document._file.file)
    # f.close()
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()
    try:
        os.mkdir(path)
    except OSError:
        #print ("Creation of the directory %s failed" % path)
        pass
    else:
        #print ("Successfully created the directory %s " % path)
        pass

    convert_pdf_to_images(pdf_name,path,name,pdf_copy)
    # f.close()
    # with open(pdf_name, 'rb') as f:
    #     import pdb;pdb.set_trace()
    #     pdf = PdfFileReader(f)
    #     information = pdf.getDocumentInfo()
    #     number_of_pages = pdf.getNumPages()
    #     name = pdf_name.split('.')[0]
    #     path = os.getcwd() +'/' +name
    #     try :
    #     	os.mkdir(path)
    #     except OSError:
    #     #print ("Creation of the directory %s failed" % path)
    #     	pass
    #     else:
    #     #print ("Successfully created the directory %s " % path)
    #     	pass
    # calling this function it converts pdf pages to images
        # convert_pdf_to_images(pdf_name,path,name)