from config import settings
from llm_factory import LLMFactory
from actions import ActionRegistry
from prompts import Prompts
from time import sleep
import re

llm = LLMFactory.create(
    provider="groq",
    model="llama-3.1-70b-versatile",
    temperature=0.0
)

class Agent:
    def __init__(self, llm, system=""):
        self.llm = llm
        self.messages = []
        if system:
            self.messages.append(("system", system))
        self.action_pattern = re.compile(r"^Ação: (\w+): (.*)$")

    def __call__(self, message):
        self.messages.append(("human", message))
        result = self.execute()
        self.messages.append(("assistant", result))
        return result

    def execute(self):
        response = self.llm.invoke(self.messages,
                                   stop = ["PAUSA"])
        return response.content


def query(question, max_turns=3):
    turn = 0
    agent = Agent(llm, Prompts.get("agent_loop").format())
    next_prompt = question

    while turn < max_turns:
        turn += 1

        print(next_prompt)
        result = agent(next_prompt) 
        sleep(5)
        print(f'Passo {turn}: {result}')
        
        # Check for actions in the response
        action_matches = [
            agent.action_pattern.match(line) 
            for line in result.split("\n") 
            if agent.action_pattern.match(line)
        ]
        print(action_matches)       

        if not action_matches or action_matches[0].groups()[0] == 'final_answer':
             _, _, response = result.partition("Resposta: ")
             return response.strip()
            
        action_match = action_matches[0]
        action_name, action_input = action_match.groups()
        
        try:
            print('Executando ação:', action_name, action_input)
            observation = ActionRegistry.execute_action(action_name, action_input.strip())
            next_prompt = f"Observação: {observation}"
        except Exception as e:
            return f"Error executing action: {str(e)}"
    
    return result

if __name__ == "__main__":
    question = "Qual é a o combinado de massa entre terra, venus, saturno e juputer"
    result = query(question, 10)
    if result:
        print('Resposta final:', result)
    else:
        print(result)
