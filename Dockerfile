FROM ubuntu:24.04
# set entrypoint.
RUN set -x \
&& echo > /boot.sh \
&& chmod +x /boot.sh \
&& echo '#!/usr/bin/env bash' >/usr/bin/entrypoint \
&& echo 'bash /boot.sh' >>/usr/bin/entrypoint \
&& echo 'cat' >>/usr/bin/entrypoint \
&& chmod +x /usr/bin/entrypoint
ENV DEBIAN_FRONTEND=noninteractive
ENTRYPOINT ["/usr/bin/entrypoint"]
WORKDIR /root
#-----------------------------------------------------------------------------------------------------------------------
# install common.
RUN set -x \
&& apt update \
&& apt install -y wget \
&& apt install -y curl \
&& apt install -y tar \
&& apt install -y zip \
&& apt install -y git \
&& apt install -y vim \
&& apt install -y g++ \
&& apt install -y make \
&& apt install -y pkg-config \
&& apt install -y iproute2 \
&& apt clean all \
&& echo "end"
#-----------------------------------------------------------------------------------------------------------------------
# install python.
RUN set -x \
&& apt update \
&& apt install -y python3 \
&& apt install -y python3-pip \
&& apt install -y python3-dev \
&& ln -sf /usr/bin/python3 /usr/bin/python \
&& pip config set global.index-url https://pypi.org/simple \
&& pip config set global.extra-index-url https://pypi.nvidia.com \
&& pip config set global.cache-dir false \
&& pip config set global.disable-pip-version-check true \
&& pip config set global.break-system-packages true \
&& apt clean all \
&& echo "end"
#-----------------------------------------------------------------------------------------------------------------------
# install nodejs.
RUN set -x \
&& curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
&& apt install -y nodejs \
&& echo "end"
#-----------------------------------------------------------------------------------------------------------------------
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN reflex init
EXPOSE 8080 8090
CMD ["reflex", "run", "--env", "prod"]
