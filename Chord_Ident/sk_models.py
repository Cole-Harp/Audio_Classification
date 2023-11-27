from pandas import read_pickle, DataFrame
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from plots import Plotting
df = None
preprocessingsteps = []
def main():
    df = read_pickle("wavs/processed_data.pickle")
    le = LabelEncoder()
    df['instrument']= le.fit_transform(df['instrument'])
    preprocessingsteps.append(le)
    lengths_peak = []
    lengths_chords =[]
    for index in range(len(df)):
        lengths_peak.append(len(df.at[index, 'peaks']))
        lengths_chords.append(len(df.at[index, 'notes']))
    df['peak-len'] = lengths_peak
    df['notes-len'] = lengths_chords

    for index in range(len(df)):
        peaks = df.at[index, 'peaks']
        freq = df.at[index, 'freq']



    # y-col = 'notes-len'
    # x-col = 'peaks-top'
    #
    # svc = SVC()



    print(df.dtypes)
    print(df.head)

if __name__ == "__main__":
    main()

