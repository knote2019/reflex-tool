FROM python:3.12-slim
RUN set -x \
&& apt update \
&& apt install -y curl \
&& apt install -y unzip \
&& curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
&& apt install -y nodejs \
&& pip install httpx \
&& pip install reflex \
&& echo "end"
WORKDIR /app
COPY . .
EXPOSE 8080 8000
CMD ["reflex", "run", "--env", "prod"]