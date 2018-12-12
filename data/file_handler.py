import pandas as pa



def load_file(path):
    de = pa.read_pickle(path)
    return de
