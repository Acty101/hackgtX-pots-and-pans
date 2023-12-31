FROM nvidia/cuda:11.7.1-devel-ubuntu20.04 as release

WORKDIR /root

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata && \
    apt-get install --no-install-recommends -y build-essential software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3-pip python3-distutils python3-venv gcc ffmpeg libsm6 libxext6 git wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# install runpod
RUN pip install runpod roboflow python-dotenv ultralytics==8.0.28

# copy all folders
COPY model model/
COPY recipe recipe/
COPY config config/

# copy test input file
COPY test_input.json ./

# copy main script
COPY main.py ./

CMD ["python3", "main.py"]

