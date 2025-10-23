from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv
import os 
load_dotenv()

### for huggingface calls ####
# hf_token = os.getenv("HUGGINGFACE_API_KEY_FINEGRAINED") 
# model= HuggingFaceEndpoint(endpoint_url="Qwen/Qwen3-Next-80B-A3B-Instruct",
#                     task ="text-generation",
#                     huggingfacehub_api_token=hf_token)

# llm1 = ChatHuggingFace(llm = model, temperature = 0.5)
llm = ChatOpenAI(model="gpt-4o", temperature=0.5)

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

prompt1 = PromptTemplate(template="Generate an ellaborate paragraph about the {topic}",
                         input_variables=["topic"])

prompt2 = PromptTemplate(template="Give me a 5 pointer summary about the {response}.",
                         input_variables=["response"])



#### for RunnableSequence Calls#####
# seq_chain = RunnableSequence(prompt1,llm, str_parser, prompt2,llm, str_parser)

##### for LCEL #####
topic_chain = prompt1 | llm | str_parser 
summary_cum_output_chain = RunnableBranch(
    (lambda x : len(x.split())>100, prompt2 | llm | str_parser),    
    RunnablePassthrough())
chain = topic_chain | summary_cum_output_chain
result = chain.invoke({"topic":"Russia Ukraine Conflict"})
print("Response:", result)
