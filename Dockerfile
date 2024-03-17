FROM ubuntu:latest
LABEL authors="a.bogomolov"

ENTRYPOINT ["top", "-b"]