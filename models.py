#!/usr/bin/env python
# -*- coding: utf-8 -*-

import joblib

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.noise import GaussianNoise
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM, GRU
from keras.optimizers import RMSprop, Adam

def create_model(history, n_chars):
    NEURON = LSTM
    INIT = 'glorot_uniform'
    model = Sequential()
    model.add(NEURON(512, input_shape=(history, n_chars), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(NEURON(512, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(n_chars))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam')
    return model


