FROM python:3.10-bookworm
RUN apt-get update
RUN apt-get install texlive-latex-base -y
WORKDIR /home
COPY latex_generator_makselivanov latex_generator_makselivanov
RUN mkdir "artifacts"
COPY images images
COPY entrypoint.sh entrypoint.sh
CMD ["/home/entrypoint.sh"]
