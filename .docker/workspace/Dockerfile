ARG TARGET_PYTHON_VERSION
# Use the Python base image
FROM python:${TARGET_PYTHON_VERSION}

RUN apt-get update -yqq && apt-get install -yqq \
    bash \
;

# Create the working directory
RUN mkdir /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Modify entrypoint to install Python packages via PIP
RUN echo "#!/bin/bash" >> /usr/bin/docker-entrypoint.sh && \
    echo "cd /usr/src/app" >> /usr/bin/docker-entrypoint.sh && \
    echo "pip3 install -r requirements.txt" >> /usr/bin/docker-entrypoint.sh && \
    echo "exec \"\$@\"" >> /usr/bin/docker-entrypoint.sh && \
    chmod +x /usr/bin/docker-entrypoint.sh

# The stdout and stderr streams are sent straight to terminal (e.g. your container log)
# Without being first buffered and that you can see the output of your application
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/usr/bin/docker-entrypoint.sh", "tail", "-f", "/dev/null"]
