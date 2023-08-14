import requests

# 定义请求的 URL 和 API 密钥
API_URL = "BASE-URL"
API_KEY = "API-KEY"  # 请替换为您的实际 API 密钥

# 定义请求的 headers 和 payload
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "用户会给你输入一个地址文本，你要从中解析出相应信息，如果信息不知道或者没把握直接在该信息留空，请你严格按照格式，不要改动，以下是格式。名字: 电话: 省: 市: 区: 详细地址: "
        },
        {
            "role": "user",
            "content": input("请输入地址信息：")
        }
    ]
}

# 发送 POST 请求
response = requests.post(API_URL, headers=headers, json=payload)

# 检查请求是否成功
if response.status_code == 200:
    data = response.json()
    print(data['choices'][0]['message']['content'])
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
