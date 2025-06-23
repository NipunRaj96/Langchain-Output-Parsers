from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser ,ResponseSchema

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model= ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact 1', description='fact 1 about the topic'),
    ResponseSchema(name='fact 2', description='fact 2 about the topic'),
    ResponseSchema(name='fact 3', description='fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template = ' give 3 facts about the {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions( )}
)

chain = template | model | parser

result = chain.invoke({'topic':'Avengers'})

print(result)