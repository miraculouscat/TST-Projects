FROM python:3.11.5
ADD main.py .
COPY . /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# Install any necessary dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Command to run the FastAPI server when the container starts
CMD ["uvicorn", "API.main:app", "--host", "0.0.0.0", "--port", "80"]