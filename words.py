#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from keras.models import Sequential
from keras.layers.core import Activation, Dropout
from keras.layers.recurrent import LSTM
import joblib


def main():
    definitions = joblib.load('definitions.pkl')

    # chars should be 28 (alphabet + ' ' + '-')
    chars = set(np.unique(list(''.join(definitions.keys()))))
    chars.add(':')
    assert len(chars) == 29

    char_idx = {c: i for i, c in enumerate(chars)}
    idx_char = {i: c for i, c in enumerate(chars)}

    max_length = 30
    # + len(definitions) to signal word end by ':'
    n_samples = sum(map(len, definitions.keys())) + len(definitions)

    X = np.zeros((n_samples, max_length, len(chars)), dtype=np.bool)
    y = np.zeros((n_samples, len(chars)), dtype=np.bool)

    # initialize to all spaces
    y[:, char_idx[' ']] = True
    X[:, :, char_idx[' ']] = True

    i = 0
    for word in definitions.keys():
        for j, char in enumerate(word):
            y[i, char_idx[char]] = True
            for k, p_char in enumerate(word[:j]):
                if j - k > max_length:
                    continue
                X[i, k-j, char_idx[p_char]] = True

            i += 1

        # add colon
        y[i, char_idx[':']] = True
        for k, p_char in enumerate(word):
            if len(word) - k > max_length:
                continue
            X[i, k-len(word), char_idx[p_char]] = True
        i += 1


    joblib.dump(X, 'X_words.jbl', compress=3)
    joblib.dump(y, 'y_words.jbl', compress=3)
    joblib.dump(char_idx, 'char_idx.jbl', compress=3)
    joblib.dump(idx_char, 'idx_char.jbl', compress=3)



if __name__ == '__main__':
    main()
