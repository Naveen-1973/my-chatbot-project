"""
git init 
git add .
git commit -m "Initial comment"

git remote add orgint https://github.com/Naveen-1973/my-chatbot-project.git
git branch -M main
git push -u origin main
##after executing above file is added in github



"""



import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.docstore.document import Document

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in .env file")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Sample chatbot function
def chat_with_ai(prompt):
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    response = llm(prompt)
    return response

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    answer = chat_with_ai(user_input)
    print("Bot:", answer)
