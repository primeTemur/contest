FROM ubuntu:22.04
RUN apt update && apt install -y g++
WORKDIR /app
CMD ["tail", "-f", "/dev/null"]
