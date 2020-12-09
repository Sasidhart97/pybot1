from gensim.parsing.preprocessing import remove_stopwords, preprocess_string
from gensim.utils import simple_preprocess
from gensim.models import FastText
def embed():
    #que=pd.read_excel("data/questionnare.xlsx")
    corpus=['How To Add Photo and other Details', 'How To Add Proxy In Internet Explorer', 'How to add Signature in Outlook', 'How to raise JIRA ticket', 'How To map Home drive', 'How to map network drive', 'how to reset windows password', 'How To Use RSA Token', 'how to reset outlook password', 'vpn connection failed error', 'my system is slow', 'how to map share drive', 'windows account locked', 'access to share drive', 'Hello', 'Hi', 'Bye', 'Who created you']
    solution=['For adding photo and details open the file :  "DataTeams -> Chatbot Channel -> files -> How To Add Photo and other Details.pptx"', 'For adding proxy in internet explorer open the file :  "DataTeams -> Chatbot Channel -> files -> How To Add Proxy In Internet Explorer.pptx"', 'For Adding signature in outlook open the file :  "DataTeams -> Chatbot Channel -> files -> How to add Signature in Outlook.pptx"', 'To raise jira ticket open the file :  "DataTeams -> Chatbot Channel -> files -> How to raise JIRA ticket.pptx"', 'To map home drive open the file :  "DataTeams -> Chatbot Channel -> files -> How To map Home drive.pptx"', 'To map network drive open the file :  "DataTeams -> Chatbot Channel -> files -> How to map network drive.pptx"', 'To reset windows password open the file :  "DataTeams -> Chatbot Channel -> files -> how to reset windows password.pptx"', 'To use rsa token open the file :  "DataTeams -> Chatbot Channel -> files -> How To Use RSA Token.pptx"', 'To reset outlook password open the file :  "DataTeams -> Chatbot Channel -> files -> how to reset outlook password.pptx"', 'Please check whether your internet connection is stable or not and try restarting your system. If issue still prevails please contact IT team', 'Please restart your system and check your internet connectivity.  For application slowness need to contact with application team. If it is related to outlook, excel and overall VDI slowness contact to IT team.', 'To map the drive> open this PC>click on computer>Click on MAP Network drive>choose later>Paste the server path', 'Wait for 5 min account get unlocked autometicatly. If still not unlocked connect to IT team and they will unlock the account', 'connect to IT and they will provide you the access for share drive', 'Hello', 'Hi', 'Bye', 'ML Team from CI, having said that I have a special interest in sasidhar :)']
    corps1=[]
    for i in corpus:
        corps1.append(simple_preprocess(remove_stopwords(i.lower())))

    model = FastText(size=50,window=3, min_count=1)  # instantiate
    model.build_vocab(sentences=corps1)
    model.train(sentences=corps1, total_examples=len(corps1), epochs=10)
    return model,corps1,solution
