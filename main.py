import sys
import os,openai
basedir= os.path.abspath(os.path.dirname(__file__))

def chatGPT(messages):
    openai.api_key=''
    response=openai.ChatCompletion().create(
        model='gpt-3.5-turbo',
        temperature=1,
        messages=messages,
    )
    # print(response['usage']['prompt_tokens'],response['usage']['completion_tokens'])
    return response['choices'][0]['message']['content']
class Bot:
    messages=[]
    def __init__(self):
        self.messages=[]
    def log(self):
        for i in range(1,len(self.messages)):
            print(self.messages[i]['content'])
    def append(self,role,content): 
        self.messages.append({
                'role':role,
                'content':content
            }
        )
    def get_messages(self):
        return self.messages
bot=Bot()
with open(os.path.join(basedir,'ans.txt'), mode='w',encoding='utf-8') as result:
        result.write('以下是回答\n')
        result.close()
for i in range(10):
    with open(os.path.join(basedir,'prompts',str(i+1)+'.txt'), mode='r',encoding='utf-8') as prompt:
        bot.append('user',prompt.read())
        prompt.close()
    response=chatGPT(bot.get_messages())
    bot.append('assistant',response)
    with open(os.path.join(basedir,'ans.txt'), mode='a',encoding='utf-8') as result:
        result.write('Q'+str(i+1)+'\n'+response+'\n')
        result.close()
    bot.log()