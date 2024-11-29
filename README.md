# Gender Prediction API

```
git clone https://github.com/Nocturnailed-Community/Serving-Gender-Prediction.git
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

## Running the Server

After setting up the environment, you can run the FastAPI server locally using Uvicorn.

1. **Start the server**:

    Run the following command to start the FastAPI app on `http://127.0.0.1:8000`:

    ```bash
    uvicorn app:app --reload
    ```

    Alternatively, if you're using a different entry point for the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

    This will reload the server automatically upon code changes.

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