import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def Agri_Bot_System(user_query):
    #model defination
    '''
    Model Info:
    model_name=Chat-GPT-4
    api=openai api
    '''
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role":"system",#defining role of model
                "content":"You are my friendly agricultural chat-bot."
            },
            {"role": "user",
            "content":f"Answer the following query {user_query}?."}
            ],
            max_tokens=3000#each token=70-80 chars or words 
    )
    
    return response["choices"][0]["message"]["content"].strip()

'''
# Example Usage
user_query=input()
print(Agri_Bot_System(user_query))
'''


