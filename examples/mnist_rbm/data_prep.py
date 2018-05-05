
import sys
import pickle
import gzip

if __name__ == '__main__':

    f = gzip.open('mnist.pkl.gz', 'rb')
    train_set, valid_set, test_set = pickle.load(f)
    pickle.dump(train_set, gzip.open('train.pickle.gz','wb'), pickle.HIGHEST_PROTOCOL)
    pickle.dump(valid_set, gzip.open('valid.pickle.gz','wb'), pickle.HIGHEST_PROTOCOL)
    pickle.dump(test_set, gzip.open('test.pickle.gz','wb'), pickle.HIGHEST_PROTOCOL)

