from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
import os 
load_dotenv()

llm = ChatOpenAI(model = "gpt-4o", temperature = 0.5)
str_parser = StrOutputParser()

prompt_article = PromptTemplate(template="Generate a news paper report  article about the following : {topic}.",
                        input_variables=["topic"])


prompt_tweet = PromptTemplate(template="Generate an official tweet like a any global media house on the following : {topic}.",
                        input_variables=["topic"])

parallel_chain = RunnableParallel(
    {"article": prompt_article | llm | str_parser,
     "tweet": prompt_tweet | llm | str_parser }
)

result = parallel_chain.invoke({"topic":"Russia Ukraine Conflict"})
print("Article:", result["article"])
print("\n")
print("Tweet:", result["tweet"])
