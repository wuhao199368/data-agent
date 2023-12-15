import os
import numpy
import pandas as pd


class FileReader(object):

    def __init__(self, path, debug=False):
        self.data = pd.read_csv(path)
        self.debug = debug

    def load_schemas(self, result_path=None):
        schemas = ", ".join(self.data.columns)
        if self.debug:
            if not os.path.exists(result_path):
                os.mkdir(result_path)

            with open(f"{result_path}/schema.txt", 'w', encoding="utf-8") as f:
                f.write(schemas)

        return schemas

    def sample_data(self, result_path=None, num=10):
        sampled_data = self.data.sample(num).to_string()
        if self.debug:
            if not os.path.exists(result_path):
                os.mkdir(result_path)

            with open(f"{result_path}/sampled_data.txt", 'w', encoding="utf-8") as f:
                f.write(sampled_data)

        return sampled_data


if __name__ == "__main__":
    reader = FileReader(
        path="../data/archive/202312/202312_CombinedData.csv/202312_CombinedData.csv",
        debug=True
    )
    reader.load_schemas("./result")
    reader.sample_data("./result")
