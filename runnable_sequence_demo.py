from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
import os 
load_dotenv()


hf_token = os.getenv("HUGGINGFACE_API_KEY_FINEGRAINED") 

### for huggingface calls ####
# model= HuggingFaceEndpoint(endpoint_url="Qwen/Qwen3-Next-80B-A3B-Instruct",
#                     task ="text-generation",
#                     huggingfacehub_api_token=hf_token)

# llm1 = ChatHuggingFace(llm = model, temperature = 0.5)
llm = ChatOpenAI(model="gpt-4o", temperature=0.5)

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

prompt1 = PromptTemplate(template="Tell me about the {topic}",
                         input_variables=["topic"])

prompt2 = PromptTemplate(template="Give me a 5 pointer summary about the {response} in the following format {format_specifications}",
                         input_variables=["response"],
                         partial_variables={"format_specifications": json_parser.get_format_instructions()})



#### for RunnableSequence Calls#####
# seq_chain = RunnableSequence(prompt1,llm, str_parser, prompt2,llm, str_parser)

##### for LCEL #####
seq_chain = prompt1 | llm | str_parser | prompt2 | llm | json_parser 
result = seq_chain.invoke({"topic":"Russia Ukraine Conflict"})
print("Final Response:", result)


