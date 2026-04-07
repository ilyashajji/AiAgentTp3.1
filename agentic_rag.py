from langchain.agents import create_agent   
from langchain_openai import ChatOpenAI
from dotenv.ipython import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain.tools import tool
from langchain.messages import HumanMessage
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.tools import create_retriever_tool

load_dotenv(override=True)
chunks=[
    "Je m'appelle Yassine, je suis un développeur de 30 ans avec 5 ans d'expérience dans le développement web. Mon salaire actuel est de 1200 euros par mois.",
    "je travaille chez OpenAI  et j'ai un salaire de 1200 euros par mois",
    "j'ai obtenu mon diplôme en informatique il y a 5 ans et je travaille chez OpenAI depuis 5 ans avec un salaire de 1200 euros par mois"
    "apres les études, j'ai travaillé chez OpenAI pendant 5 ans avec un salaire de 120_0 euros par mois"
]

embedding_model=OpenAIEmbeddings()

vector_store=Chroma.from_texts(
    texts=chunks,
    collection_name="cv",
    embedding=embedding_model
)

retriever=vector_store.as_retriever() 

def get_employee_info(name: str):
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
llm =ChatOpenAI(model="gpt-4o", temperature=0)
agent=create_agent(
    model=llm,
    tools=[send_email,get_employee_info],
    system_prompt="Answer to user query using provided tools"
)
#resp=agent.invoke(input={"messages":[HumanMessage("Quel est le salaire de yassine")]})
#print(resp["messages"][-1].content)