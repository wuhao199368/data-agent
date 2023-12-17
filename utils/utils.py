import sys


def user_input_await(prompt: str) -> str:
    # print("\033[94m\033[1m" + "> COPY FOLLOWING TEXT TO CHATBOT\n" + "\033[0m\033[0m")
    # print(prompt)
    # print("\033[91m\033[1m" + "AFTER PASTING, PRESS: (ENTER), (CTRL+Z), (ENTER) TO FINISH\n" + "\033[0m\033[0m")
    print("\033[96m\033[1m" + "> 你想从这份数据中获取什么信息？:" + "\033[96m\033[0m")
    input_text = input()

    return input_text.strip()


if __name__ == "__main__":

    result = user_input_await("test")
    print(result)