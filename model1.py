import scipy
import numpy as np
import win32com.client as win32
import pandas as pd
import re
import nltk
nltk.download('wordnet')
nltk.download('punkt')
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from nltk.corpus import stopwords
import socket

def models(text1,message):
    if(text1.lower().replace(" ","")=="connecttoit"):
        server = smtplib.SMTP('64.233.184.108')
        server.ehlo()
        server.starttls()
        server.login('sasidharturaga@gmail.com', 'felixsasi1997')
        body = "Please resolve it ----- " + message
        msg = MIMEText(body,'plain','utf-8')
        subject = 'Email test'
        msg["Subject"] = Header(subject, 'utf-8')
        from1 = 'sasidharturaga@gmail.com'
        to = 'turaga.sasidhar@metro-services.in'
        msg["From"] = Header(from1, 'utf-8')
        msg["To"] = Header(to, 'utf-8')
        txt = msg.as_string()
        server.sendmail(from1, to, txt)
        #import pythoncom
        #pythoncom.CoInitialize()
        #outlook = win32.Dispatch('outlook.application')
        #mail = outlook.CreateItem(0)
        #mail.To = 'turaga.sasidhar@metro-services.in'
        #mail.Subject = 'Unresolved Query from IT Bot'
        #mail.Body = '***This is an auto-generated mail from IT BOT.***\n\nThis is an automated email from the Chatbot since it couldn\'t address the query from the user.\nPlease find below the query that the user was looking to resolve through the chatbot: "'+message+'"'
        #mail.Send()
        return "Mail sent. Someone from IT team will contact you"    
    else:
        
        #from sentence_transformers import SentenceTransformer
        #import warnings
        
        #warnings.filterwarnings("ignore")
        #model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
        def clean_text(text):
            que=pd.read_excel("questionnare.xlsx")
            corpus=list(que["Question"])
            solution=list(que["Answer"])
            stopwords_english = stopwords.words('english')
            stopwords_english=list(stopwords_english)
            #print(stopwords_english)
            find_words = re.compile(r'\w+').findall
            text=text.lower()
            temp1=find_words(text)
            ct=[]
            for word in temp1:
                if (word not in stopwords_english):
                    #print(word)
                    ct.append(word.lower())
            return ' '.join(ct)+" "+solution[-1]
        return clean_text(text1)
