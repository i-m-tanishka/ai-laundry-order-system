# 🧺 Laundry Order Management System (AI-First)

## 📌 Overview

This is a simple backend system for managing laundry/dry-cleaning orders.
It allows store owners to create orders, track their status, calculate billing, and view business insights through a dashboard.

The project was built with an **AI-first approach**, using tools like ChatGPT to accelerate development and improve productivity.

---

## 🚀 Features Implemented

### 1. Create Order

* Add customer name and phone number
* Add garments with quantity
* Automatic price calculation using predefined price list
* Generates unique Order ID
* Returns total bill amount

---

### 2. Order Status Management

Each order follows a lifecycle:

* RECEIVED
* PROCESSING
* READY
* DELIVERED

✔ Ability to update order status via API

---

### 3. View Orders

* View all orders
* Filter orders by:

  * Status
  * Phone number
  * Customer name

---

### 4. Dashboard

Provides business insights:

* Total number of orders
* Total revenue
* Number of orders per status

---

## 🛠️ Tech Stack

* Python
* Flask (Backend framework)
* In-memory storage (dictionary)

---

## ⚙️ Setup Instructions

### Step 1: Install dependencies

```bash
pip install flask
```

### Step 2: Run the server

```bash
python app.py
```

### Step 3: Access the API

```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### Create Order

```
POST /order
```

### Update Order Status

```
PUT /order/<order_id>/status
```

### Get Orders

```
GET /orders
GET /orders?status=READY
GET /orders?phone=9876543210
```

### Dashboard

```
GET /dashboard
```

---

## 🤖 AI Usage Report (Very Important)

### 🔹 Tools Used

* ChatGPT (primary development assistant)
* (Optional) GitHub Copilot

---

### 🔹 How AI Was Used

AI was heavily used to:

* Generate initial Flask API structure
* Suggest endpoint design
* Help implement business logic (billing, filtering)
* Debug runtime errors
* Improve code readability

---

### 🔹 Sample Prompts Used

```
Create a simple Flask API for laundry order system with CRUD operations
```

```
Add filtering functionality by status and phone number in Flask API
```

```
Create a dashboard API returning total orders, revenue, and status count
```

```
Fix error in Flask API (paste error log)
```

---

### 🔹 Where AI Helped the Most

* Quickly generating boilerplate backend code
* Designing API endpoints
* Writing reusable logic for billing and filtering
* Debugging errors efficiently

---

### 🔹 Where AI Fell Short

* Did not include proper input validation initially
* Some responses had logical gaps (e.g., incorrect status handling)
* Needed manual correction for edge cases
* Did not optimize structure for clarity

---

### 🔹 Improvements Made Manually

* Added input validation (phone number, quantity)
* Fixed incorrect logic in total calculation
* Standardized status values
* Improved code readability and structure
* Added filtering by name/phone/status

---

## ⚖️ Trade-offs

* Used in-memory storage instead of database (data is lost on restart)
* No authentication system implemented
* No frontend UI included

---

## 🚧 Future Improvements

* Integrate database (MongoDB / MySQL)
* Add authentication system
* Build frontend dashboard (React or HTML)
* Add order history and search by garment type
* Add estimated delivery date
* Deploy application (Render / Railway)

---

## 🎯 Conclusion

This project demonstrates the ability to:

* Quickly build a working backend system
* Effectively leverage AI tools for development
* Identify and fix gaps in AI-generated code
* Deliver a practical and functional solution under time constraints

---
