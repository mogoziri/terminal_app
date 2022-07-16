#!/bin/bash

echo "formatting python files"
find . -name "*.py" -exec autopep8 --in-place --aggressive '{}' \;
echo "done"