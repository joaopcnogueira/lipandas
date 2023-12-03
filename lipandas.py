import argparse

from IPython import start_ipython
import pandas as pd


def get_cli_args():
    parser = argparse.ArgumentParser(description='Load a CSV file into a Pandas DataFrame and open it in IPython.')
    parser.add_argument('filepath', type=str, help='Path to the CSV file')
    parser.add_argument('--sep', type=str, default=',', help='Separator for the CSV file')
    parser.add_argument('--nrows', type=int, default=None, help='Number of rows to read from the CSV file')
    args = parser.parse_args()

    return args

def main():
    args = get_cli_args()
    try:
        df = pd.read_csv(
            args.filepath, 
            sep=args.sep,
            nrows=args.nrows
        )
        print("\nDataFrame loaded. Use 'df' to access the data.\n")
        start_ipython(argv=[], user_ns={'df': df})
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
