# https://github.com/willhallonline/docker-git-sizer/blob/master/alpine/Dockerfile

# # build stage
# FROM golang:alpine AS build-env
# RUN apk add --no-cache git
# RUN go get github.com/github/git-sizer

# FROM alpine:latest
# RUN apk add --no-cache git
# WORKDIR /app
# COPY --from=build-env /go/bin/git-sizer /usr/bin/git-sizer

FROM python:3.11-rc-alpine

RUN apk add --no-cache git

ADD src /

RUN pip install -r requirements.txt

#WORKDIR src

#RUN python -m gitanalyser run

CMD [ "python", "main.py"]
