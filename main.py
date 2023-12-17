import argparse

from utils import FileReader
from modules import data_summarize, generate_tasks

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-d", "--data", type=str, required=True, help="Specify the data path been analyzed")
# parser.add_argument("-o", "--objective", type=str, required=True, help="Objective of data analyze")
args = parser.parse_args()


def main():
    reader = FileReader(path=args.data, debug=False)
    schemas, sampled_data = reader.load_schemas(), reader.sample_data()
    data_summarization = data_summarize(schemas=schemas, sampled_data=sampled_data, debug=True)
    objective = input("\033[96m\033[1m" + "> 你想从这份数据中获取什么信息？:" + "\033[96m\033[0m")
    task_list = generate_tasks(
        step="init",
        objective=objective,
        max_tokens=4000,
        summarization=data_summarization
    )
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
