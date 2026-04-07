from langchain.agents import create_agent   
from langchain_openai import ChatOpenAI
from dotenv.ipython import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain.tools import Tool

load_dotenv(override=True)

def get_employee_info(name: str) -> str:
    """
        Get employee information about a given employee (name, salary, seniority) 
    """
    print("get_employee_info tool invoked")
    return {"name":name,"salary":1200,"seniority":5}
@tool
def send_email(email:str,subject:str,content:str) -> str:
    """
        Send an email with a subject and content 
    """
    print(f"Email sent to {email} with subject {subject} and content {content}")
    return f"Email succesfully sent to {email} with subject {subject} and content {content}"