import base64
from openai import OpenAI
import base64


API_BASE = "https://xdaicn.top/v1"
API_KEY = "sk-4Y9hIZXOQY8WmLm5R6Fr7hKDdyDPy64TNqXyw6FIcrZXJNUM"


# client = OpenAI()

# # Function to encode the image
# def encode_image(image_path):
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')

# # Path to your image
# image_path = "path_to_your_image.jpg"

# # Getting the base64 string
# base64_image = encode_image(image_path)

# response = client.chat.completions.create(
#   model="gpt-4o",
#   base_url="https://chat.xdaicn.top/openapi/v1/upload",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "What is in this image?",
#         },
#         {
#           "type": "image_url",
#           "image_url": {
#             "url":  f"data:image/jpeg;base64,{base64_image}"
#           },
#         },
#       ],
#     }
#   ],
# )

# print(response.choices[0])







# import openai
# from openai import OpenAI
# API_BASE = "https://chat.xdaicn.top/openapi/v1/upload"
# API_KEY = "sk-4Y9hIZXOQY8WmLm5R6Fr7hKDdyDPy64TNqXyw6FIcrZXJNUM"
# client = OpenAI(
#   api_key=API_KEY,
#   base_url=API_BASE
# )
# completion = client.chat.completions.create(
#   model="gpt-4o-2024-08-06",
#   messages=[{"role": "user", "content": "Hi, who are you?"}]
# )
# print(completion)



client = OpenAI(
  api_key=API_KEY,
  base_url=API_BASE
)

# Approach 3: use local image and encode it to base64
image1_path = "./Strandard.png"
image2_path = "./View1.JPG"


with open(image1_path, "rb") as image_file:
  image1 = "data:image/jpeg;base64," + base64.b64encode(image_file.read()).decode('utf-8')
with open(image2_path, "rb") as image_file:
  image2 = "data:image/jpeg;base64," + base64.b64encode(image_file.read()).decode('utf-8')
  
print(image1)
# Make a request, can be multi round gemini-1.0-pro-vision-latest
completion = client.chat.completions.create(
  model="gpt-4o-2024-08-06",
  # model="gemini-1.0-pro-vision-latest",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "请你根据第一张图片中的判断标准，判断第二张图片所归属的类型。第一段输出描述，第二段输出判断结果并在判断结果的左右添加$符号。按照以下格式填写：$判断结果$",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": image1
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": image2
          }
        },
      ]
    },
  ]
)

print(completion.json())

