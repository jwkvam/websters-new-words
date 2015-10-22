#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers.core import Activation, Dropout
from keras.layers.recurrent import LSTM
import joblib


def main():
    definitions = joblib.load('definitions.pkl')

    # chars should be 28 (alphabet + ' ' + '-')
    chars = set(np.unique(list(''.join(defs.keys()))))
    assert len(chars) == 28

    char_idx = dict((c, i) for i, c in enumerate(chars))
    idx_char = dict((i, c) for i, c in enumerate(chars))

if __name__ == '__main__':
    main()
