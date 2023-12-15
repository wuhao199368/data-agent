from .utils import call_openai
PATH = "../prompt/summarizer.txt"


def data_summarize(
        schemas: str,
        sampled_data: str,
) -> str:
    global PATH
    with open(PATH, 'r', encoding="utf-8") as f:
        prompt = f.read()

    prompt.format(schemas, sampled_data)

    summarization = call_openai(prompt)
    return summarization
