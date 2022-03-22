#!/bin/bash

N=6
(
for f in raw/*.md; do 
   ((i=i%N)); ((i++==0)) && wait
   pandoc "$f" --pdf-engine=xelatex -V geometry:"margin=0.75in" -o "pdfs/${f:4:-3}.pdf" & 
done
)

