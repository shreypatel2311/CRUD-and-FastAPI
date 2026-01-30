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
The Order Management API is organized using a modular and layered project structure to ensure scalability, readability, and ease of maintenance. The application is divided into clearly defined layers, where each layer has a single responsibility. API routes handle client requests, service modules contain core business logic, and database models manage data persistence.

Authentication, orders, products, and payments are structured as independent modules, allowing features to evolve without impacting other parts of the system. Request and response schemas are used for data validation, ensuring consistent and secure data flow across the application. Common utilities manage error handling, validations, and reusable helpers, reducing code duplication. This structured approach reflects real-world SaaS and product-based backend standards, making the system easy to test, extend, and deploy. The clean separation of concerns improves code quality and supports future enhancements such as microservices, analytics, and third-party integrations.
