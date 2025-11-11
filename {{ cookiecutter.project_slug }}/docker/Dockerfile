# Alpine + micromamba + Python 3.8 (auto-activated)
FROM mambaorg/micromamba:git-9a50bbf-alpine3.21

# Make sure conda-style activation works in later RUN steps
ARG MAMBA_DOCKERFILE_ACTIVATE=1
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 \
    MAMBA_ROOT_PREFIX=/opt/conda \
    PATH=/opt/conda/bin:$PATH \
    CONDA_ENV_NAME=py38

# Create the env and auto-activate on login shells
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN micromamba create -y -n "$CONDA_ENV_NAME" python=3.8 \
 && micromamba clean -a -y \
 && echo "micromamba activate $CONDA_ENV_NAME" >> /home/mambauser/.bashrc

USER root
RUN apk update ; apk add git
user $MAMBA_USER

# Use bash as default (image includes it)
#SHELL ["/bin/bash", "-lc"]

# Prove it works
#RUN source /root/.bashrc && python --version && micromamba info

RUN mkdir /tmp/{{ cookiecutter.project_slug }}
COPY ./ /tmp/{{ cookiecutter.project_slug }}/
RUN /opt/conda/envs/py38/bin/pip install git+https://github.com/digitaltumors/aixport.git

RUN /opt/conda/envs/py38/bin/pip install /tmp/{{ cookiecutter.project_slug }}

USER root
RUN rm -rf /tmp/{{ cookiecutter.project_slug }}
USER $MAMBA_USER


ENTRYPOINT ["/opt/conda/envs/py38/bin/{{ cookiecutter.__runner_name }}.py"]

CMD ["--help"]
