from .utils import call_openai
PATH = "./prompt/summarizer.txt"


def data_summarize(
        schemas: str,
        sampled_data: str,
        max_tokens: int = 4000,
        debug: bool = False
) -> str:
    global PATH
    with open(PATH, 'r', encoding="utf-8") as f:
        prompt = f.read()

    prompt = prompt.format(schemas, sampled_data)
    messages = [
        {"role": "system", "content": "You are an assistant tasked with summarizing a given table. "},
        {"role": "user", "content": prompt}
    ]
    summarization = call_openai(messages=messages, max_tokens=max_tokens)

    if debug:
        with open("./summarization.txt", 'w', encoding="utf-8") as f:
            f.write(summarization)

    return summarization
