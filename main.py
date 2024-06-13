import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

chat=ChatGroq(temperature=0,groq_api_key="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",model_name="llama3-8b-8192")

prompt=ChatPromptTemplate.from_template("tell me a short story {topic}")
output_parser=StrOutputParser()

chain=prompt | chat| output_parser

respons =chain.invoke({"topic":"tell me a hinduism"})

print("1*"*60)
print("Resonse -->>>>  ", respons)
prompt_value=prompt.invoke({"topic":"muslim"})

print("2*"*60)
print(prompt_value)

print("3*"*60)
message=chat.invoke(prompt_value)
print(message)

