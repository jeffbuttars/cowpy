#!/bin/bash


export VERSION=`cat setup.py | grep __version__ | head -1 | sed "s/__version__ = //" | sed "s/'//g"`
export PREFIX=""

if [ -d 'venv' ] ; then
    export PREFIX="venv/bin/"
fi

if [ -d '.venv' ] ; then
    export PREFIX=".venv/bin/"
fi

if ! command -v "${PREFIX}twine" &>/dev/null ; then
    echo "Unable to find the 'twine' command."
    echo "Install from PyPI, using '${PREFIX}pip install twine'."
    exit 1
fi

${PREFIX}python setup.py sdist
${PREFIX}twine upload dist/*

# If you want to test first
#${PREFIX}twine upload --repository testpypi  dist/*

echo "You probably want to also tag the version now:"
echo "git tag -a ${VERSION} -m 'version ${VERSION}'"
echo "git push --tags"

rm -r dist
