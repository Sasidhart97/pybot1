from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.utils import simple_preprocess
from numpy import dot
from numpy.linalg import norm
def psf(text1,corps1,solution,model):
    if((text1.replace(" ","")[0:11].lower()=="connecttoit") | (text1.replace(" ","")[0:10].lower()=="connectoit")):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        email = '' # the email where you sent the email
        password = ''
        send_to_email = "" # for whom
        subject = "Query from chatbot"
        if(len(text1.split("-"))>1):
            message = text1.split("-")[1]

            msg = MIMEMultipart()
            msg["From"] = email
            msg["To"] = send_to_email
            msg["Subject"] = subject

            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, send_to_email, text)
            server.quit()
            return "Mail Sent to IT. Someone will contact you soon with the resolution."
        else:
            return 'Please type your query in this format' + '"' + "CONNECT TO IT - Your query" + '"'
    else:

        inp=text1
        test=simple_preprocess(remove_stopwords(inp.lower()))
        if(len(test)==0):
            test=simple_preprocess(inp)

        def simil_fun(a,b):
            a1=a.sum(axis=0)
            b1=b.sum(axis=0)
            return dot(a1, b1)/(norm(a1)*norm(b1))

        indi=0
        responses=[]
        for i in range(len(corps1)):
            if(simil_fun(model.wv[test],model.wv[corps1[i]])>0.5):
                indi=1
                #print(i,solution[i].replace("\\n","\n"),simil_fun(model.wv[test],model.wv[corps1[i]]))
                responses.append(solution[i].replace("\\n","\n"))
        if(indi!=1):
            responses.append("The requested information is not avaialble. Please rephrase your question or type \"CONNECT TO IT - Your query\" so that a person from IT team will contact you")
            #print("The requested information is not avaialble. Please rephrase your question or type \"CONNECT TO IT\" so that a person from IT team will contact you")

        reply=""
        if(len(responses)==1):
            reply=responses[0]
        else:
            reply="Found "+str(len(responses))+" related responses for your query"+"\n\n"
            for i in range(len(responses)):
                reply=reply+"\n\n"+responses[i]
        return reply
