#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as rng

import joblib
import models

def main(arg1):
    model = models.create_model

def spaces(char_idx):
    Xn = np.zeros((30, 29))
    Xn[:, char_idx[b' ']] = 1
    return Xn

def sample_char(probs):
    return np.nonzero(rng.multinomial(1, probs))[0][0]

def addchar(context, idx):
    context = np.roll(context, -1, axis=0)
    context[-1, :] = 0
    context[-1, idx] = 1
    return context

def generate_word(model, char_idx, idx_char):
    context = spaces(char_idx)

    word = []

    for i in range(100):
        probs = model.predict(context[None, :, :]).ravel()
        idx = sample_char(probs)

        letter = idx_char[idx]

        if letter == ':':
            break

        word.append(letter)
        context = addchar(context, idx)

    return ''.join(w.decode() for w in word)


if __name__ == "__main__":
    main()
