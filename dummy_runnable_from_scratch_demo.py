from abc import ABC, abstractmethod
import warnings


class Runnable(ABC):
    @abstractmethod
    def invoke(args):
        pass

class dummyPromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    
    def invoke(self, kwargs):
        return self.template.format(**kwargs)
    
    
    def format(self, kwargs):
        warnings.warn(
            "The 'format' method is deprecated and will be removed in a future version. "
            "Please use 'invoke' method instead.",
            DeprecationWarning,
            stacklevel=2
        )
        return self.template.format(**kwargs)      

class dummyLLM(Runnable):
    def __init__(self):
        print("LLM Instance Created")
        
    def invoke(self, prompt):
        if "Bengal" in prompt:
            return {"response":"Kolkata is the capital of West Bengal. These two teams are from Kolkata."}
        elif "IFA" in prompt:
            return {"response":"The East Bengal–Mohun Bagan rivalry in the IFA Shield is one of Indian football’s most storied battles, symbolizing passion, pride, and regional identity. Since their first clash in the early 20th century, their encounters have transcended sport, capturing the emotions of millions across Bengal. Each IFA Shield duel between the Red and Gold of East Bengal and the Green and Maroon of Mohun Bagan turns into a festival of fierce competition, unforgettable goals, and iconic moments that continue to define the legacy of Kolkata football."}
        else :
            return {"response":"Sorry! I dont have enough context to answer this question."}
     
       
    def predict(self,prompt):
        warnings.warn(
            "The 'predict' method is deprecated and will be removed in a future version. "
            "Please use 'invoke' method instead.",
            DeprecationWarning,
            stacklevel=2
        )
        if "Bengal" in prompt:
            return "Kolkata is the capital of West Bengal. These two teams are from Kolkata."
        elif "IFA" in prompt:
            return "The East Bengal–Mohun Bagan rivalry in the IFA Shield is one of Indian football’s most storied battles, symbolizing passion, pride, and regional identity. Since their first clash in the early 20th century, their encounters have transcended sport, capturing the emotions of millions across Bengal. Each IFA Shield duel between the Red and Gold of East Bengal and the Green and Maroon of Mohun Bagan turns into a festival of fierce competition, unforgettable goals, and iconic moments that continue to define the legacy of Kolkata football."
        else :
            return "Sorry! I dont have enough context to answer this question."
class dummyStringOutputParser(Runnable):
    def __init__(self):
        pass
    def invoke(self, output):
        return output["response"]   

class dummyChain(Runnable):
    def __init__(self, compoment_list):
        self.component_list = compoment_list
    
    def invoke(self, inputs):
        present_input = inputs
        for component in self.component_list:
            present_input = component.invoke(present_input)
        
        return present_input
                
  
if __name__ == "__main__" :
    prompt_template1 = dummyPromptTemplate(template="Tell me about the rivalry between {teams} in {tournamnet}", 
                                 input_variables=["teams","tournament"])
    prompt_template2 = dummyPromptTemplate(template="Where are these {response} based out of ?",
                                           input_variables=["response"])
    llm = dummyLLM()
    parser = dummyStringOutputParser()
    chain1 = dummyChain([prompt_template1, llm])
    chain2 = dummyChain([prompt_template2, llm, parser])
    chain = dummyChain([chain1,chain2])
    result = chain.invoke({"teams":"East Bengal and Mohun Bagan", "tournamnet": "IFA Shield"})
    print("Chain Response:", result)
        