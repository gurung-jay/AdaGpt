import openai
import config

openai.api_key = config.ApiConfig.OPENAI_KEY


def adaResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "You are a botanist  expert"})

    chatInput = {}
    chatInput['role'] = 'user'
    chatInput['content'] = prompt
    messages.append(chatInput)


    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)

    try: 
        ans = response['choices'][0]['message']['content']
    
    except:
        ans = "sorry,something went wrong!"

    return ans