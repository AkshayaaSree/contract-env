from pydantic import BaseModel
from typing import List
import random
from tasks.tasks import tasks
from graders.grader import grade


class Observation(BaseModel):
    contract_text: str
    task_type: str
    instructions: str
    previous_actions: List[str]


class Action(BaseModel):
    type: str
    content: str


class ContractEnv:
    def __init__(self):
        self.tasks = tasks

    def reset(self):
        self.current_step = 0
        self.done = False
        self.history = []

        self.task = random.choice(self.tasks)

        instruction_map = {
            "clause_classification": "Identify the clause type.",
            "risk_detection": "Identify risks and explain why.",
            "contract_improvement": "Suggest a safer version of the clause."
        }

        return Observation(
            contract_text=self.task["contract"],
            task_type=self.task["type"],
            instructions=instruction_map[self.task["type"]],
            previous_actions=[]
        )

    def step(self, action: Action):
        if self.done:
            raise Exception("Episode already finished")

        self.current_step += 1

        base_score = grade(self.task, action.content)

        # reward shaping
        reward = base_score * 0.7

        if len(action.content.split()) > 5:
            reward += 0.1

        if len(action.content.split()) < 3:
            reward -= 0.2

        if action.content in self.history:
            reward -= 0.1

        if base_score > 0.8:
            reward += 0.3
            self.done = True

        if self.current_step >= 5:
            self.done = True

        self.history.append(action.content)

        observation = Observation(
            contract_text=self.task["contract"],
            task_type=self.task["type"],
            instructions=self._get_instruction(),
            previous_actions=self.history
        )

        return observation, round(reward, 2), self.done, {}

    def _get_instruction(self):
        return {
            "clause_classification": "Identify the clause type.",
            "risk_detection": "Identify risks and explain why.",
            "contract_improvement": "Suggest a safer version."
        }[self.task["type"]]

    def state(self):
        return {
            "task": self.task,
            "history": self.history,
            "step": self.current_step,
            "done": self.done
        }