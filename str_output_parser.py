from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model= ChatHuggingFace(llm=llm)

#1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)
#2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 lines summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1= template1.invoke({'topic':'India'})
result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text':'result1.content '})
result2 = model.invoke(prompt2)

print(result1.content)
print(result2.content)