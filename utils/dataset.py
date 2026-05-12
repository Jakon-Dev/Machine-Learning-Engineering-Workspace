import pandas as pd
def get_data_set(dataset_name: str = r"nba_player_stats_2026.csv"):
    complete_path = "C:\\Users\\marcl\\Documents\\GitHub\\Machine Learning Engineering Workspace\\.datasets\\" + dataset_name
    return pd.read_csv(complete_path)

def print_pretty_df(df: pd.DataFrame, max_rows: int = 10):
    print(df.head(max_rows).to_string(index=False))


if __name__ == '__main__':
    print_pretty_df(get_data_set())