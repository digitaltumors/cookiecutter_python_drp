# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y build-essential 

RUN mkdir /tmp/{{ cookiecutter.project_slug }}
COPY ./ /tmp/{{ cookiecutter.project_slug }}/
RUN pip install /tmp/{{ cookiecutter.project_slug }}

RUN rm -rf /tmp/{{ cookiecutter.project_slug }}

ENTRYPOINT ["/opt/conda/bin/{{ cookiecutter.__runner_name }}.py"]

CMD ["--help"]
