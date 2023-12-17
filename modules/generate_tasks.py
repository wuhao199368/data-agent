import re
from .utils import call_openai


def generate_tasks(
        step: str,
        objective: str,
        max_tokens: int=4000,
        **kwargs,
):
    if step == "init":
        with open("./prompt/task_generator.txt", 'r', encoding="utf-8") as f:
            prompt = f.read()
        prompt = prompt.format(objective, kwargs.get("summarization", None))
        messages = [
            {
                "role": "system",
                "content": "You are an data scientist tasked with generating a list of tasks based on "
                           "the given objective and data summarization"
            },
            {"role": "user", "content": prompt}
        ]

        tasks = call_openai(messages=messages, max_tokens=max_tokens)
    elif step == "internal":
        tasks = None
    else:
        print("Something wrong")

    new_tasks = tasks.split('\n')
    new_tasks_list = []
    for task_string in new_tasks:
        task_parts = task_string.strip().split(".", 1)
        if len(task_parts) == 2:
            task_id = ''.join(s for s in task_parts[0] if s.isnumeric())
            task_name = re.sub(r'[^\w\s_]+', '', task_parts[1]).strip()
            if task_name.strip() and task_id.isnumeric():
                new_tasks_list.append(task_name)
            # print('New task created: ' + task_name)

    out = [{"task_name": task_name} for task_name in new_tasks_list]

    return out