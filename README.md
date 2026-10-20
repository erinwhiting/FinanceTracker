#Finance Tracker — Full‑Stack CRUD Web App
A full‑stack personal finance tracking application built with Python (Flask), SQLite, and HTML/CSS/JavaScript. Users can add, view, edit, and delete financial transactions through a clean, responsive interface. This project demonstrates backend API development, database integration, and dynamic frontend rendering.

#Features
- Add new financial transactions
- View all transactions in a dynamic table
- Edit existing transactions
- Delete transactions
- Persistent storage using SQLite
- Clean, modern UI
- Full separation of frontend and backend
- RESTful API built with Flask

##Tech Stack

###Backend
- Python
- Flask
- Flask-CORS
- SQLite

###Frontend
- HTML
- CSS
- JavaScript (Fetch API)

##Project Structure

finance-tracker/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── database.db
│
└── frontend/
    ├── index.html
    ├── styles.css
    ├── app.js

##How to Run the Project

###1. Clone the repository

git clone <your-repo-url>
cd finance-tracker

###2. Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate

###3. Install backend dependencies

pip install flask flask-cors

###4. Start the backend server

python backend/app.py

The API will run at:
http://127.0.0.1:5000/

###5. Open the frontend

Option A:
Open frontend/index.html directly in your browser.

Option B (recommended):
Use the VS Code Live Server extension.

##API Endpoints

###GET /transactions
Returns all transactions.

###POST /transactions
Adds a new transaction.

Example JSON body:
{
  "name": "Groceries",
  "amount": 50.00,
  "category": "Food",
  "date": "2027-04-15"
}

###PUT /transactions/<id>
Updates an existing transaction.

###DELETE /transactions/<id>
Deletes a transaction.

##Future Improvements
- Chart.js spending visualization
- User authentication
- Category filtering
- Monthly summaries

