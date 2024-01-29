OUTPUT_FILE = document.pdf


$(OUTPUT_FILE): build/main.pdf
	cp $< $@

build/main.pdf: src/*.tex src/*/*
	@if ! [ -d build/ ]; then\
		mkdir build/;\
	fi
	mv build src/
	latexmk -g -shell-escape -output-directory=build -pdf -cd src/main.tex | scripts/pplatex -i
	mv -f src/build ./

clean:
	@if [ -f $(OUTPUT_FILE) ]; then\
		rm $(OUTPUT_FILE);\
		echo "Cleaned";\
	else\
		echo "All clean";\
	fi