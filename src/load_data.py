import pandas as pd

file_path_ratings = "data/raw/title.ratings.tsv.gz"
file_path_basics = "data/raw/title.basics.tsv.gz"

def load_data(file_path):
    df = pd.read_csv(file_path, sep="\t")
    return df

ratings = load_data(file_path_ratings)
basics = load_data(file_path_basics)