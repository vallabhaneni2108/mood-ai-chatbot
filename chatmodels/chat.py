#open AI

# from dotenv import load_dotenv

# load_dotenv()

# from langchain.chat_models import init_chat_model


# model = init_chat_model("gpt-4.1") # initializing model

# # print(model)

# response = model.invoke(" What is cricket? ") # when we ask a question it will give a response we need to store it in response

# print(response.content)


# we can use model class instead of init chat model

# from dotenv import load_dotenv

# load_dotenv()

# from langchain_openai import ChatOpenAI


# model = ChatOpenAI(model = "gpt-5") # initializing model

# # print(model)

# response = model.invoke(" What is cricket? ") # when we ask a question it will give a response we need to store it in response

# print(response.content)


# using google gemini AI

# from dotenv import load_dotenv

# load_dotenv()
# from langchain.chat_models import init_chat_model

# model = init_chat_model("google_genai:gemini-3.7-flash")

# response = model.invoke("give me a paragraph on machine learning")

# print(response.content)

# you can use model class also

# from dotenv import load_dotenv

# load_dotenv()
# from langchain_google_genai import ChatGoogleGenerativeAI

# model = ChatGoogleGenerativeAI(model = "gemini-3.7-flash")

# response = model.invoke("give me a paragraph on cricket")

# print(response.content)

# using grok
#from dotenv import load_dotenv

# load_dotenv()
# from langchain.chat_models import init_chat_model

# model = init_chat_model("groq:openai/gpt-oss-120b") # you need to put groq infront of model

# response = model.invoke("give me a paragraph on machine learning")

# print(response.content)

# using model class of groq

from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(model= "openai/gpt-oss-120b",temperature=0.9,
                 max_tokens=20)
# you need not to put groq infront of model
# if you want to do creative task put temperature somewhat high
# if you want to do logical task put temperature somewhat low

response = model.invoke("write a poem on AI")

print(response.content)


# using mistral AI and model class instead of init chat model

# from dotenv import load_dotenv

# load_dotenv()

# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(model = "mistral-medium-3-5") # you need not to put groq infront of model

# response = model.invoke("give me a paragraph on deeplearning")

# print(response.content)