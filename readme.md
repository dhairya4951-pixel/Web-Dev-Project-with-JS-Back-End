# Backend - Web Dev Capstone with JS

This repository contains the backend of a full-stack product management web application built using **Flask**.

## Features

- GET API to fetch all products
- POST API to add a new product
- In-memory product storage using a Python list
- Basic server-side validation
- JSON-based API responses

## Project Structure

```text
backend/
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10+
- Flask
- flask-cors

## How to Install requirements.txt

Open a terminal in the backend folder and run:

```bash
pip install -r requirements.txt
```

If requirements.txt does not exist yet, create it with:

```bash
pip freeze > requirements.txt
```

## How to Run the Backend

Open a terminal in the backend folder.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

## API Endpoints

### GET /products

Returns the list of all products.

### POST /products

Adds a new product.

Example JSON body:

```json
{
  "name": "Keyboard",
  "price": 2500,
  "category": "Electronics",
  "description": "Mechanical keyboard",
  "stock": 10
}
```

## Notes

- Data is stored in memory, so it resets when the server restarts.
- The frontend connects to this backend using the Fetch API.
- Make sure this backend is running before opening the frontend.

## Frontend Repository

https://github.com/dhairya4951-pixel/Web-Dev-Project-with-JS-Front-End.git

## Author

Sarthak