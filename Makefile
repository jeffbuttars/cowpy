
.PHONY: clean

TARGET := dist/cowpy-$(shell python ./setup.py --version).tar.gz

$(TARGET): 
	poetry build

publish: $(TARGET)
	scripts/publish

publishtest: $(TARGET)
	twine upload --repository testpypi dist/*

clean:
	rm -fr dist build
