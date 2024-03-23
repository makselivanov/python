#!/bin/bash
cd /home/latex_generator_makselivanov
python test.py
cd /home/artifacts
pdflatex table.tex