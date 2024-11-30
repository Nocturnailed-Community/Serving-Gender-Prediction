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

**Start the server**:

    Run the following command to start the FastAPI app on `http://127.0.0.1:8000`:

    ```bash
    uvicorn app:app --reload
    ```

    Alternatively, if you're using a different entry point for the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

    This will reload the server automatically upon code changes.

## Testing the API

Once the FastAPI server is running, you can test the API by sending HTTP requests to it. You can use [Hoppscotch](https://hoppscotch.io/) or [Postman](https://www.postman.com/) to make requests.

### Using Hoppscotch to Test the API

1. Go to [Hoppscotch.io](https://hoppscotch.io/) in your web browser.

2. **Select the method**: Choose `POST` from the dropdown menu next to the URL input.

3. **Enter the API URL**: In the URL bar, type:

    ```
    http://127.0.0.1:8000/predict
    ```

4. **Set the request body**: In the body section, select the `multipart/form-data` option and enter the following:

    ```
    {
        "file": "Upload File"
    }
    ```

5. **Send the request**: Click on the `Send` button.

6. **Check the response**: You will receive a response from the server, such as:

    ```json
    {
        "label": "Male",
        "image_base64": "<base64_encoded_image>"
    }
    ```

This will show the predicted intent for the input text.

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

## Docker Hub Repository

The Docker image for the gender prediction API is available on Docker Hub. You can pull the image using the following command:

```bash
docker pull ikhwan17/gender-prediction
```

## Source

- HuggingFace: https://huggingface.co/rizvandwiki/gender-classification
- DockerHub: https://hub.docker.com/r/ikhwan17/gender-prediction