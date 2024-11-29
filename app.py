import os

# Paksa TensorFlow dinonaktifkan
os.environ["USE_TF"] = "0"
os.environ["TRANSFORMERS_NO_TF_WARNING"] = "1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Sembunyikan log error TensorFlow

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import torch
import base64
import io

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pretrained model and feature extractor
extractor = AutoFeatureExtractor.from_pretrained("rizvandwiki/gender-classification")
model = AutoModelForImageClassification.from_pretrained("rizvandwiki/gender-classification")

# Ensure the model runs on the appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Standard size for images
STANDARD_SIZE = (224, 224)  # Sesuaikan dengan input model Anda

# Route for checking if the model is running
@app.get("/")
async def root():
    return {"message": "The model API is running successfully!"}

# Define prediction endpoint
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Load image from uploaded file
        image = Image.open(file.file)

        # Convert image to RGB mode if needed
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Resize image to standard size
        image = image.resize(STANDARD_SIZE)

        # Preprocess image
        inputs = extractor(images=image, return_tensors="pt")
        inputs = {key: val.to(device) for key, val in inputs.items()}

        # Make predictions
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_label = logits.argmax(-1).item()
            label = model.config.id2label[predicted_label]

        # Convert the image to Base64 format
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        base64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return {
            "label": label,
            "image_base64": base64_image
        }

    except Exception as e:
        # Debug error jika terkait TensorFlow
        if "tensorflow" in str(e).lower():
            return {"error": "TensorFlow conflict detected. Please ensure PyTorch is set as default backend."}
        return {"error": str(e)}