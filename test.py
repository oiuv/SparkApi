from dotenv import load_dotenv
import os
import SparkApi

# 加载 .env 文件
load_dotenv()

# 以下密钥信息从控制台获取
# 从环境变量中读取密钥信息
appid = os.getenv('APPID')  # 填写控制台中获取的 APPID 信息
api_secret = os.getenv('API_SECRET')  # 填写控制台中获取的 APISecret 信息
api_key = os.getenv('API_KEY')  # 填写控制台中获取的 APIKey 信息

# 用于配置大模型版本，默认“general/generalv2”
domain = "general" if os.getenv('MODEL_VERSION') == '1.5' else "generalv2"
# 云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat" if os.getenv('MODEL_VERSION') == '1.5' else "ws://spark-api.xf-yun.com/v2.1/chat"

text = []

# length = 0


def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text


def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text


if __name__ == '__main__':
    text.clear()
    while (1):
        Input = input("\n" + "我:")
        question = checklen(getText("user", Input))
        SparkApi.answer = ""
        print("星火:", end="")
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        getText("assistant", SparkApi.answer)
        # print(str(text))
