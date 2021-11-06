###############################################################################
#-----------------------------    BUILD STAGE   ------------------------------#
###############################################################################

ARG PYTHON_VERSION_TAG
FROM python:$PYTHON_VERSION_TAG-slim-buster AS builder

ENV \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    # poetry:
    POETRY_VERSION=1.1.4 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin"

# System deps:
ARG DEBIAN_FRONTEND=noninteractive
RUN set -x \
    && apt-get update -qq \
    && apt-get install -qqy --no-install-recommends \
    # dependencies for building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev \
    # For exporting UML graphs
    graphviz \
    # Translations dependencies
    gettext \
    # Other tools
    git \
    curl \
    wget \
    unzip \
    htop \
    tmux \
    curl \
    ca-certificates \
    # tini
    tini \
    # cleaning up unused files
    && apt-get purge -y --auto-remove \
                     -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Installing `poetry` package manager:
# https://github.com/python-poetry/poetry
RUN curl -sSL \
'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' \
| python

WORKDIR /workspace

# Uses "Spaceship" theme with some customization. Uses some bundled plugins and installs some more from github
ENV TERM xterm
RUN sh -c "$(curl -fsSL https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)" -- \
    -p git \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/zsh-users/zsh-history-substring-search \
    -p https://github.com/zsh-users/zsh-syntax-highlighting \
    -p 'history-substring-search' \
    -a 'bindkey "\$terminfo[kcuu1]" history-substring-search-up' \
    -a 'bindkey "\$terminfo[kcud1]" history-substring-search-down'
SHELL ["/bin/zsh", "-c"]

ENTRYPOINT ["/usr/bin/tini", "--"]
