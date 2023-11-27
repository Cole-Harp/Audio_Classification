from pandas import read_pickle, DataFrame
from sklearn.preprocessing import LabelEncoder
from plots import Plotting
df = None
preprocessingsteps = []
def main():
    df = read_pickle("wavs/processed_data.pickle")
    le = LabelEncoder()
    df['instrument']= le.fit_transform(df['instrument'])
    preprocessingsteps.append(le)
    lengths = []
    for index in range(len(df)):
        lengths.append(len(df.at[index, 'peaks']))
    print(lengths)
    print(df.dtypes)
    print(df.head)

if __name__ == "__main__":
    main()

