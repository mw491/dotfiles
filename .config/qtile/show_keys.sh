#!/bin/bash

sed -n -e '/START_KEYS/,/END_KEYS/p' ~/.config/qtile/config.py | \
    sed -e '/END_KEYS/d' -e '/START_KEYS/d' \
    -e 's/^[ \t]*//' \
    -e 's/desc=*//' | \
    yad --text-info
