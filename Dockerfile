FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install numpy pandas scikit-learn wandb opencv-python
CMD ["python", "distance_classification.py"]