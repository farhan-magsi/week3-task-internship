from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib
import pandas as pd
import os

# ---------- Initialize FastAPI ----------
app = FastAPI(title="Energy Prediction Dashboard")

# ---------- Setup Templates & Static ----------
templates = Jinja2Templates(directory="Templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# ---------- Load Model ----------
model_path = "model.joblib"
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print(" Model loaded successfully!")
    # Auto-detect features from model
    if hasattr(model, "feature_names_in_"):
        FEATURES = model.feature_names_in_.tolist()
    elif hasattr(model, "named_steps") and hasattr(model.named_steps.get("model"), "feature_names_in_"):
        FEATURES = model.named_steps["model"].feature_names_in_.tolist()
    else:
        FEATURES = []
        print("⚠️ Could not auto-detect features. Please set FEATURES manually.")
    print(f" {len(FEATURES)} features detected.")
else:
    model = None
    FEATURES = []
    print("❌ model.joblib not found!")

# ---------- Routes ----------
@app.get("/")
async def home(request: Request):
    """Home page with navigation"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard")
async def dashboard(request: Request):
    """Dashboard with visualizations"""
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/predict")
async def predict_get(request: Request):
    """Prediction page - GET request (show form)"""
    return templates.TemplateResponse("predict.html", {
        "request": request,
        "features": FEATURES,
        "prediction": None,
        "error": None
    })

@app.post("/predict")
async def predict_post(
    request: Request,
    
):
    prediction = None
    error = None
    
    if model is None:
        error = "Model file not found! Please ensure model.joblib exists."
        return templates.TemplateResponse("predict.html", {
            "request": request,
            "features": FEATURES,
            "prediction": prediction,
            "error": error
        })
    
    try:
        #data of form read 
        form_data = await request.form()
        input_dict = {}
        
        for feature in FEATURES:
            val = form_data.get(feature)
            if val is None or val.strip() == "":
                raise ValueError(f"Please enter a value for {feature}")
            input_dict[feature] = [float(val)]
        
        input_df = pd.DataFrame(input_dict)
        prediction = model.predict(input_df)[0]
        prediction = round(prediction, 2)
        print(f"✅ Prediction: {prediction}")
        
    except Exception as e:
        error = str(e)
        print(f"❌ Error: {e}")
    
    return templates.TemplateResponse("predict.html", {
        "request": request,
        "features": FEATURES,
        "prediction": prediction,
        "error": error
    })

# ---------- Run (for development) ----------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)