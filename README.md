# AI-Powered-Medical-Assistant

## 1. Setup Conda Environment

To create and activate a Conda environment with Python **3.8.10**, run:

```sh
conda create --name env python=3.8.10 -y
conda activate env
```

## 2. Install Dependencies

Once the environment is activated, install the required libraries:

```sh
pip install -r requirements.txt
```

## 3. Running FastAPI Backend

Navigate to the backend folder (if applicable) and start the FastAPI server:

```sh
uvicorn backend:app --reload

## 4. Running Streamlit Frontend

To start the **Streamlit UI**, run:

```sh
streamlit run frontend.py
```

This will launch the web application in your default browser.

---

## 5. Running Both Backend & Frontend Together

To run both services simultaneously:

1. Open **two terminal windows**.
2. In the first terminal, start FastAPI:
   ```sh
   uvicorn backend:app --reload
   ```
3. In the second terminal, start Streamlit:
   ```sh
   streamlit run frontend.py
   ```

Now, your **FastAPI backend** will handle API requests, and the **Streamlit frontend** will serve the UI.

---


 
