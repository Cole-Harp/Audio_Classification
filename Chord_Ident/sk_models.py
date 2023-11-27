import pandas as pd
from sklearn.preprocessing import LabelEncoder
from plots import Plotting
df = None
preprocessingsteps = None
def main():
    df = pd.read_pickle("wavs/processed_data.pickle")
    plot = Plotting(df)
    plot.plots(2)


    #le = LabelEncoder()

    print(df.dtypes)


if __name__ == "__main__":
    main()

