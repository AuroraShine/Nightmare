#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib


def hash_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()
