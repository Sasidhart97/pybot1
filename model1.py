def models(text1,model,message):
    if(text1.lower().replace(" ","")=="connecttoit"):
        import win32com.client as win32
        #import pythoncom
        #pythoncom.CoInitialize()
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = 'turaga.sasidhar@metro-services.in'
        mail.Subject = 'Unresolved Query from IT Bot'
        mail.Body = '***This is an auto-generated mail from IT BOT.***\n\nThis is an automated email from the Chatbot since it couldn\'t address the query from the user.\nPlease find below the query that the user was looking to resolve through the chatbot: "'+message+'"'
        mail.Send()
        return "Mail sent. Someone from IT team will contact you"    
    else:
        import scipy
        import numpy as np
        #from sentence_transformers import SentenceTransformer
        import warnings
        import pandas as pd
        warnings.filterwarnings("ignore")
        #model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
        def clean_text(text):
            import re
            from nltk.corpus import stopwords
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
            return ' '.join(ct)
        que=pd.read_excel("questionnare.xlsx")
        corpus=list(que["Question"])
        solution=list(que["Answer"])
        crp1=[]
        for i in range(len(corpus)):
            crp1.append(clean_text(corpus[i]))
        corpus_embeddings = model.encode(crp1)
        queries = [text1]
        for i in range(len(queries)):
            queries[i]=clean_text(queries[i])
        query_embeddings = model.encode(queries)
        closest_n = 1
        for query, query_embedding in zip(queries, query_embeddings):
            distances = scipy.spatial.distance.cdist([query_embedding], corpus_embeddings, "cosine")[0]
            
            results = zip(range(len(distances)), distances)
            results = sorted(results, key=lambda x: x[1])
            
            for idx, distance in results[0:closest_n]:
                simla=1-distance
                outs=solution[idx].strip()
                
                print(idx,corpus[idx].strip(),"(Score: %.4f)" % (1-distance))
                
            if(simla>0.56):
                if(idx<9):
                    foup=outs+"\n. If you are not satisfied with the response, please rephrase you query or type \"CONNECT TO IT\" so that a person from IT team will contact you"
                else:
                    foup=outs
            else:
                foup="Currently the requested information is not avaialble. Please try to rephrase you query or type \"CONNECT TO IT\" so that a person from IT team will contact you"

        return foup