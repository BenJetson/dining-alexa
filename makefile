
archive: clean

	@echo "\n\nMaking archive for upload...\n\n"

	zip -r upload.zip *

clean:

	@echo "\n\nCleaning up...\n\n"

	find ./ -type f -name '*.pyc' -exec rm {} \;
	rm -f upload.zip
	rm -rf __pycache__
