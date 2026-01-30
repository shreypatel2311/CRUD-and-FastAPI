# Order Management API

A Flask-based REST API for managing orders using PostgreSQL.  
This project demonstrates CRUD operations, database connection pooling, 
PostgreSQL functions, and Swagger API documentation.

---

## 🚀 Features

- Create, Read, Update, Delete (CRUD) orders
- PostgreSQL database integration
- psycopg2 connection pooling
- PostgreSQL stored function to calculate total order amount
- Swagger UI for API documentation
- Clean and simple project structure

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-RESTX (Swagger)
- PostgreSQL
- psycopg2
- VS Code

---

## 📂 Project Structure: “My project follows a modular layered architecture where routing, business logic, and data access are clearly separated, making the Order Management API scalable, secure, and production-ready.”

order-management-api/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── order.py
│   │   ├── order_item.py
│   │   └── payment.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── product_schema.py
│   │   ├── order_schema.py
│   │   └── payment_schema.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── order_service.py
│   │   ├── payment_service.py
│   │   └── product_service.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── order_routes.py
│   │   ├── product_routes.py
│   │   └── payment_routes.py
│   │
│   ├── utils/
│   │   ├── validators.py
│   │   ├── responses.py
│   │   └── exceptions.py
│
├── tests/
│   ├── test_orders.py
│   ├── test_payments.py
│   └── test_auth.py
│
├── .env
├── requirements.txt
├── README.md
└── run.sh
