import requests
from myconfig import *

def explain_text(content1, content2, api_key):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    
    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "你是一个聪明的文献总结师，你要通过我给你的文献名字以及一小段摘要，生成不超过150字的文献简述："
                    },
                    {
                        "type": "text",
                        "text": "文献名称"+content1
                    },
                    {
                        "type": "text",
                        "text": "文献部分摘要"+content2
                    },
                    
                ]
            }
        ],
        "stream": False,
        "max_tokens": 512,
        "stop": ["null"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"}
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return {"error": response.status_code, "message": response.text}
