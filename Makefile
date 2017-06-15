all:
	cd src ; \
	zip ../CryptoTracker.alfredworkflow . -r --exclude=*.DS_Store* --exclude=*.pyc*

clean:
	rm -f *.alfredworkflow