import pandas as pd

#DATA/intelligence_platform.db


def migrate_dataset_metdata(conn):
    data = pd.read_csv("DATA/datasets_metadata.csv")
    data.to_sql('datasets_metadata', conn)

def get_all_datasets_metadata(conn):
    sql = 'SELECT * FROM datasets_metadata'
    data = pd.read_sql(sql, conn)
    return data 
