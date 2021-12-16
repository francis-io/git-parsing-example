
# crappy hack below, but just for dev work, should be in a makefile, or docker-compose
docker build -t git-parser:latest .
docker run --rm -it -v $(pwd):/repo git-parser:latest
