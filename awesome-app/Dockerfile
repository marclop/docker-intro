FROM lincheney/alpine-passenger

RUN apk --update add \
    bash \
    python \
    python-dev \
    py-pip \
    && pip install virtualenv \
    && rm -rf /var/cache/apk/*

ADD ./run.sh /run.sh

ENTRYPOINT ["/run.sh"]
