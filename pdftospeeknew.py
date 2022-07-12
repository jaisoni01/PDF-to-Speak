import PyPDF2
from pdf2image import convert_from_path
import pyttsx3
  
path = open('INHV.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(path)
print("1 : Say Text Of PDF\n2 : Save a audio file for complete pdf\n")
choice = int(input("Enter Your Choice : "))
while(choice>=2 and choice <=1):
     print("Please enter a valid choice")
     choice = int(input("Enter Your Choice : "))

if choice == 1:  
 speaker = pyttsx3.init()
 for page_num in range(pdfReader.numPages):   
    text = pdfReader.getPage(page_num).extractText()  ## extracting text from the PDF
    cleaned_text = text.strip().replace('\n',' ')
    print(cleaned_text)
    speaker.say(cleaned_text)
    speaker.runAndWait()
 speaker.stop()
elif choice == 2:
 cleaned_text = ""
 speaker = pyttsx3.init() 
 for page_num in range(pdfReader.numPages):   
    text = pdfReader.getPage(page_num).extractText()  ## extracting text from the PDF
    cleaned_text += text.strip().replace('\n',' ')  ## Removes unnecessary spaces and break lines
    print(cleaned_text)                ## Print the text from PDF
    speaker.save_to_file(cleaned_text,'story.mp3')  ## Saving Text In a audio file 'story.mp3'
    speaker.runAndWait()
 speaker.stop()
