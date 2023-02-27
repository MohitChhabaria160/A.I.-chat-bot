fileopen=open("data\\api.txt", "r")
API=fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv




openai.api_key=API
load_dotenv()
completion=openai.Completion()

def qestionsanswer(question,chat_log=None):
    filelog=open("database\qna_log.txt","r")
    chat_log_template=filelog.read()
    filelog.close()

    if chat_log is None:
        chat_log=chat_log_template
    
    prompt=f"{chat_log}You : {question}\nJarvis : "
    response=completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    answer=response.choices[0].text.strip()
    chat_log_template_update=chat_log_template+f"\nYou : {question} \nJarvis : {answer}"
    filelog=open("database\qna_log.txt","w")
    filelog.write(chat_log_template_update)
    filelog.close()
    return answer