FROM alpine:latest

MAINTAINER Marc Lopez

RUN apk --update add mysql-client
CMD ["sh", "-c", "mysql -u $USER -h $HOST -p$PASS"]
