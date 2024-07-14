#!/usr/bin/env python

import sys

current_category = None
current_count = 0

for line in sys.stdin:
    category, _ = line.strip().split("\t")
    if current_category == category:
        current_count += 1
    else:
        if current_category:
            sys.stdout.write(f"{current_category}\t{current_count}\n")
        current_category = category
        current_count = 1

if current_category:
    sys.stdout.write(f"{current_category}\t{current_count}\n")