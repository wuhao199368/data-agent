import argparse

from utils import FileReader
from modules import summarize

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-d", "--data", type=str, required=True, help="Specify the data path been analyzed")
parser.add_argument("-o", "--objective", type=str, required=True, help="Objective of data analyze")
args = parser.parse_args()


def main():
    reader = FileReader(path=args.data, debug=False)
    schemas, sampled_data = reader.load_schemas(), reader.sample_data()
    data_summarization = summarize(schemas=schemas, sampled_data=sampled_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reader = FileReader(
        path="../data/archive/202312/202312_CombinedData.csv/202312_CombinedData.csv",
        debug=True
    )
    reader.load_schemas("./result")
    reader.sample_data("./result")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
