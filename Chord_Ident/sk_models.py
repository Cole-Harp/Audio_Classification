from pandas import read_pickle, DataFrame
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from plots import Plotting
df = None
preprocessingsteps = []
def main():
    df = read_pickle("wavs/processed_data.pickle")
    le = LabelEncoder()
    df['instrument']= le.fit_transform(df['instrument'])
    preprocessingsteps.append(le)
    amps = []
    freq2 = []
    for index in range(len(df)):
        peaks = df.at[index, 'peaks']
        freq = df.at[index, 'freq']
        amps.append(df.at[index,'fft'][peaks])
        freq2.append(df.at[index,'freq'][peaks])


    df_training = DataFrame()
    df_training['target-instrument'] = df['instrument']
    for num_peaks in range():
        df_training[f'peak{index}']
        df_training[f'amp-peak{index}']

    plt.scatter(peaks,amps)
    plt.show()



    print(df.dtypes)
    print(df.head)

if __name__ == "__main__":
    main()

