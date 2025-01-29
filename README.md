# Disease Prediction AI

## 1. Setup Conda Environment

To create and activate a Conda environment with Python **3.8.10**, run:

```sh
conda create --name env1 python=3.8.10 -y
conda activate env1
```

## 2. Install Dependencies

Once the environment is activated, install the required libraries:

```sh
pip install -r requirements.txt
```

### Sample `requirements.txt` file:

```txt
fastapi
uvicorn
streamlit
sentence-transformers
chromadb
langchain-groq
speechrecognition
pydantic
```

---

## 3. Running FastAPI Backend

Navigate to the backend folder (if applicable) and start the FastAPI server:

```sh
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
```

This will start the FastAPI server on **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

### Test API Endpoints

Once FastAPI is running, you can test the API by opening:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

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
   uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
   ```
3. In the second terminal, start Streamlit:
   ```sh
   streamlit run frontend.py
   ```

Now, your **FastAPI backend** will handle API requests, and the **Streamlit frontend** will serve the UI.

---

## 6. Deployment Notes

- Ensure ports **8000 (FastAPI)** and **8501 (Streamlit)** are open if running on a cloud server.
- Use **ngrok** or a reverse proxy like **Nginx** for external access.

---

## 7. Troubleshooting

### Conda Environment Issues

- If the `env1` environment is not found, activate it using:
  ```sh
  conda activate env1
  ```
- If `python 3.8.10` is not available, update Conda:
  ```sh
  conda update conda
  ```

### Streamlit Not Found

- Ensure the environment is active:
  ```sh
  conda activate env1
  ```
- Then reinstall Streamlit:
  ```sh
  pip install streamlit
  ```

---

Now you're ready to use the **Disease Prediction AI** project! 🚀

give me complete code to writr in readme file


 
