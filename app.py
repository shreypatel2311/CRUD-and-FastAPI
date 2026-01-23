from flask import Flask
# from flask_restx  import Api, Resource, fields
from flask_restx import Api, Resource, fields

from db import get_conn, release_conn

app = Flask(__name__)

api = Api(
    app,
    title="Order Management API",
    description="Flask API with PostgreSQL & psycopg2 pool",
    doc="/swagger/"
)

order_model = api.model("Order", {
    "customer_name": fields.String(required=True),
    "product_name": fields.String(required=True),
    "quantity": fields.Integer(required=True),
    "price": fields.Float(required=True)
})

# ---------------- CREATE ORDER ----------------
@api.route("/orders")
class OrderList(Resource):

    @api.expect(order_model)
    def post(self):
        data = api.payload
        conn = get_conn()
        try:
            cur = conn.cursor()

            cur.execute("""
                INSERT INTO orders (customer_name, product_name, quantity, price)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
            """, (
                data["customer_name"],
                data["product_name"],
                data["quantity"],
                data["price"]
            ))

            order_id = cur.fetchone()[0]
            conn.commit()
            return {"message": "Order placed", "order_id": order_id}, 201

        except Exception as e:
            conn.rollback()
            return {"error": str(e)}, 500

        finally:
            release_conn(conn)

    # ---------------- READ ALL ORDERS ----------------
    def get(self):
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM orders;")
            rows = cur.fetchall()

            orders = []
            for r in rows:
                orders.append({
                    "id": r[0],
                    "customer": r[1],
                    "product": r[2],
                    "quantity": r[3],
                    "price": float(r[4]),
                    "status": r[5]
                })

            return orders, 200

        finally:
            release_conn(conn)


# ---------------- UPDATE & DELETE ----------------
@api.route("/orders/<int:order_id>")
class Order(Resource):

    def put(self, order_id):
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute("""
                UPDATE orders
                SET status = %s
                WHERE id = %s;
            """, ("COMPLETED", order_id))

            conn.commit()
            return {"message": "Order updated"}, 200

        except Exception as e:
            conn.rollback()
            return {"error": str(e)}, 500

        finally:
            release_conn(conn)

    def delete(self, order_id):
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM orders WHERE id = %s;", (order_id,))
            conn.commit()
            return {"message": "Order cancelled"}, 200

        finally:
            release_conn(conn)


# ---------------- DB FUNCTION API ----------------
@api.route("/orders/<int:order_id>/total")
class OrderTotal(Resource):

    def get(self, order_id):
        conn = get_conn()
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT calculate_total_amount(quantity, price)
                FROM orders WHERE id = %s;
            """, (order_id,))

            total = cur.fetchone()
            if not total:
                return {"message": "Order not found"}, 404

            return {"total_amount": float(total[0])}, 200

        finally:
            release_conn(conn)


if __name__ == "__main__":
    app.run(debug=True)
