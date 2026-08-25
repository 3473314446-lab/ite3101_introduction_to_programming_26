# Python 3.11 development container based on Debian 12 Bookworm
ARG VARIANT="3.11-bookworm"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# Install Python dependencies during image build.
# The build context is the repository root, so requirements.txt
# is available directly from the root directory.
COPY requirements.txt /tmp/pip-tmp/requirements.txt

RUN pip3 --disable-pip-version-check \
         --no-cache-dir \
         install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Optional: install additional operating-system packages.
# RUN apt-get update \
#     && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get install -y --no-install-recommends vim \
#     && rm -rf /var/lib/apt/lists/*