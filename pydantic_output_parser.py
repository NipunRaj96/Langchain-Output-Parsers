from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model= ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str=Field(description="Name of the person")
    age: int=Field(gt=18 , description="age of the person")
    city: str=Field(description="City name where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="Generate the name , age and city of a famous {universe} superhero \n {format_instructions}",
    input_variables=['universe'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

# prompt = template.invoke({'universe':'Marvel'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template | model | parser
final_result = chain.invoke({'universe':'Marvel'})
print(final_result)

