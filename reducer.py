#!/usr/bin/env python

import sys

current_category = None
current_count = 0

for line in sys.stdin:
    category, _ = line.strip().split("\t")
    if current_category == category:
        current_count += 1
    else:
        if current_category and current_count > 114:
            sys.stdout.write("{0}\t{1}\n".format(current_category, current_count))
        current_category = category
        current_count = 1

if current_category and current_count > 114:
    sys.stdout.write("{0}\t{1}\n".format(current_category, current_count))