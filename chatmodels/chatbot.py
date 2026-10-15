from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatGroq(model= "openai/gpt-oss-120b",temperature=0.9)
# you need not to put groq infront of model
# if you want to do creative task put temperature somewhat high
# if you want to do logical task put temperature somewhat low

print("choose your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode")
print("press 3 for sad mode")

choice = int(input("enter your mode: "))

if choice == 1:
    mode = "you are an Angry AI agent . you respond aggresively and impatient.."
elif choice ==2:
    mode = "you are a very Funny Agent. you respond with humour and jokes."
elif choice == 3:
    mode="you are a very sad agent.you should respond with very sorrow."
messages=[
    SystemMessage(content=mode) # you are telling ai agent that you are fuuny AI
] # to store chat history


while True:
    print("------------------Welcome Type 0 to exit the application----------")

    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt)) # to add into chat history

    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content)) # to add into chat history
    print("Bot:",response.content)

print(messages)