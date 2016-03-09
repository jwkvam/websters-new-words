#!/usr/bin/env python
# -*- coding: utf-8 -*-

import joblib

import models

def main():
    X = joblib.load('./X_words.jbl')
    y = joblib.load('./y_words.jbl')

    print('loaded data')
    model = models.create_model(X.shape[1], X.shape[2])
    print('model compiled')
    print(model.summary())
    model.fit(X, y, batch_size=128, nb_epoch=1)
    model.save_weights('word_model.h5')

if __name__ == "__main__":
    main()
