#!/usr/bin/env python
# -*- coding: utf-8 -*-

import joblib

import models

def main():
    X = joblib.load('./X_words.jbl')
    y = joblib.load('./y_words.jbl')

    models.create_model(X.shape[1], X.shape[2])

    model.fit(X, y, batch_size=128, nb_epoch=1)
    models.save_weights('word_model.h5')
    # joblib.dump(model.get_weights(), 'model_weights.jbl', compress=3)

if __name__ == "__main__":
    main()
