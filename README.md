# Gender Prediction API

```
git clone https://github.com/Nocturnailed-Community/gender-Prediction-API.git
```

## Install Library dependencies

```
torch
transformers
Pillow
fastapi
uvicorn
python-multipart
```

```
pip install -r requirements.txt
```

## Deployment

Instructions for running the model in docker

```
docker build -t gender-prediction .
docker run -d -p 8000:8000 gender-prediction
```

The instruction looks at running containers

```
docker ps
```

Push Docker Hub

```
docker build . -t your_username_docker/gender-prediction
docker login
docker push your_username_docker/gender-prediction
```