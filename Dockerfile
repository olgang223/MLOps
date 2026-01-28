FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn
ENV PYTHONPATH=/app
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "80"]
