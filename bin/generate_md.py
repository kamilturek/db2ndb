#!/usr/bin/env python3

from db2ndb.transformations import TRANSFORMATIONS

if __name__ == "__main__":
    for transformation in TRANSFORMATIONS:
        print(f"- `{transformation.code}` - {transformation.transformer.__doc__}")
