from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

# now we will use chains to create a pipeline 

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'India'})
print(result)