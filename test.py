import re
from pypdf import PdfReader
file=input("Enter the file name with extension: ")
if file.endswith('.pdf'):
    reader = PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
elif file.endswith('.txt'):
    with open(file, 'r') as f:
        text = f.read()

else:   
    print("Unsupported file format. Please provide a .pdf or .txt file.")
    exit()
def extract_links_and_emails(text):
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@gmail.com'
    url_pattern = r'https?://[^\s]+'
    phone_pattern = r'[+91][6-9][0-9]{9}'
    phone_pattern1 = r'[6-9][0-9]{9}'

    emails = re.findall(email_pattern, text)
    urls = re.findall(url_pattern, text)
    phones = re.findall(phone_pattern , text)
    phones1 = re.findall(phone_pattern1 , text)
    phones.extend(phones1)
    return emails, urls, phones



emails, urls,phones = extract_links_and_emails(text)

print("Emails:", emails)
print("URLs:", urls)
print("Phones:", phones)
