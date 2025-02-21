import google.generativeai as ai

API='AIzaSyBggiwgga-qUWuDg2Seh-wFyhpxiZhs7vI'

ai.configure(api_key=API)

model=ai.GenerativeModel("gemini-pro")

chat= model.start_chat()

while True:
    message=input("Your message: ")
    if message.lower()=='bye':
        print("Good Bye")
        break
    response=chat.send_message(message)
    print('chat-app',response.text)
