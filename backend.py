from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import  uvicorn
from functions import query_disease_symptoms, get_response_from_groq  # Import functions

app = FastAPI()

class SymptomInput(BaseModel):
    symptoms: str

@app.post("/predict")
async def predict_disease(input_data: SymptomInput):
    disease_info = query_disease_symptoms(input_data.symptoms)
    
    if not disease_info:
        raise HTTPException(status_code=404, detail="No matching disease found.")
    
    final_response = get_response_from_groq(input_data.symptoms, disease_info)
    return {"disease_info": disease_info, "response": final_response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)