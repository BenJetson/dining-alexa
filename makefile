
archive: clean

	@echo "\n\nMaking archive for upload...\n\n"

	uuidgen | tr "[:lower:]" "[:upper:]" | cut -c 10-23 > buildID

	zip -r upload.zip *

	@echo "\n\nThis build's ID is: "
	@cat buildID
	@echo "\n"

clean:

	@echo "\n\nCleaning up...\n\n"

	find ./ -type f -name '*.pyc' -exec rm {} \;
	rm -f upload.zip buildID
	rm -rf __pycache__
