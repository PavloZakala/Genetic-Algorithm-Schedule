import pickle

def read_file_pickle(path):

    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data

def write_file_pickle(data, path):

    with open(path, "wb") as f:
        pickle.dump(data, f)