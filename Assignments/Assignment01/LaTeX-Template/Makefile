TEX = xelatex
TEXFLAGS = -interaction=nonstopmode -halt-on-error
TARGET = HW

all:
	$(TEX) $(TEXFLAGS) $(TARGET).tex
	$(TEX) $(TEXFLAGS) $(TARGET).tex
	rm -f *.aux *.log *.lop *.out

.PHONY: all clean