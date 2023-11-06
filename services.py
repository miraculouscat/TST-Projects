from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel

app = FastAPI()

class Service(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Membaca data dari file JSON
json_filename = "services.json"

with open(json_filename, "r") as read_file:
    data = json.load(read_file)
    services_data = data.get("services", [])

# Read (GET) - Membaca semua layanan
@app.get("/services/", response_model=list[Service])
def read_services():
    return services_data

# Read (GET) - Membaca layanan berdasarkan ID
@app.get("/services/{service_id}", response_model=Service)
def read_service(service_id: int):
    for service in services_data:
        if service["id"] == service_id:
            return service
    raise HTTPException(status_code=404, detail="Layanan tidak ditemukan")

# Create (POST) - Membuat layanan baru
@app.post("/services/", response_model=Service)
def create_service(service: Service):
    services_data.append(service.dict())
    return service

# Update (PUT) - Memperbarui layanan
@app.put("/services/{service_id}", response_model=Service)
def update_service(service_id: int, service: Service):
    for index, existing_service in enumerate(services_data):
        if existing_service["id"] == service_id:
            services_data[index] = service.dict()
            return service
    raise HTTPException(status_code=404, detail="Layanan tidak ditemukan")

# Delete (DELETE) - Menghapus layanan
@app.delete("/services/{service_id}", response_model=Service)
def delete_service(service_id: int):
    for index, service in enumerate(services_data):
        if service["id"] == service_id:
            deleted_service = services_data.pop(index)
            return deleted_service
    raise HTTPException(status_code=404, detail="Layanan tidak ditemukan")