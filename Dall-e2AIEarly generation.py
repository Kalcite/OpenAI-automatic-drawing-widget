import openai
import os
os.system('')
from PIL import Image
from io import BytesIO
import requests as req
 
ApiKey=input("\033[1;32m请输入您的有效ApiKey(登录https://openai.com/api/获取):\033[0m")
#注册的api_key
openai.api_key=ApiKey 
 

#用来生成图像的文本提示
Prompt1=input("\033[1;32m请输入您的要求\033[0m")
size1=input("\033[1;32m请输入您想要的尺寸\033[0m")
prompt=Prompt1 
#生成图像
response=openai.Image.create(prompt=prompt,
              n=3,
              model="image-alpha-001",
              size=size1,
              response_format="url") 
 
#第一张图片
image_rul=response["data"][0]["url"]
res=req.get(image_rul)
Image.open(BytesIO(res.content))
