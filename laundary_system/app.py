from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
orders = {}
order_counter = 1

# Price list (hardcoded)
PRICE_LIST = {
    "Shirt": 10,
    "Pants": 15,
    "Saree": 20
}

VALID_STATUSES = ["RECEIVED", "PROCESSING", "READY", "DELIVERED"]


# 1️⃣ Create Order
@app.route('/order', methods=['POST'])
def create_order():
    global order_counter

    data = request.get_json()

    # Basic validation
    if not data or 'customer_name' not in data or 'phone' not in data or 'items' not in data:
        return jsonify({"error": "Invalid input"}), 400

    if len(data['phone']) != 10:
        return jsonify({"error": "Phone must be 10 digits"}), 400

    total = 0
    items = []

    for item in data['items']:
        item_type = item.get('type')
        qty = item.get('qty', 0)

        if item_type not in PRICE_LIST or qty <= 0:
            return jsonify({"error": "Invalid item or quantity"}), 400

        price = PRICE_LIST[item_type]
        total += price * qty

        items.append({
            "type": item_type,
            "qty": qty,
            "price": price
        })

    order_id = f"ORD{order_counter:03}"
    order_counter += 1

    order = {
        "order_id": order_id,
        "customer_name": data['customer_name'],
        "phone": data['phone'],
        "items": items,
        "total": total,
        "status": "RECEIVED"
    }

    orders[order_id] = order

    return jsonify({
        "message": "Order created",
        "order_id": order_id,
        "total": total
    })


# 2️⃣ Update Order Status
@app.route('/order/<order_id>/status', methods=['PUT'])
def update_status(order_id):
    data = request.get_json()
    new_status = data.get('status')

    if new_status not in VALID_STATUSES:
        return jsonify({"error": "Invalid status"}), 400

    if order_id not in orders:
        return jsonify({"error": "Order not found"}), 404

    orders[order_id]['status'] = new_status

    return jsonify({
        "message": "Status updated",
        "order": orders[order_id]
    })


# 3️⃣ View Orders (with filters)
@app.route('/orders', methods=['GET'])
def get_orders():
    status = request.args.get('status')
    phone = request.args.get('phone')
    name = request.args.get('name')

    result = list(orders.values())

    if status:
        result = [o for o in result if o['status'] == status]

    if phone:
        result = [o for o in result if o['phone'] == phone]

    if name:
        result = [o for o in result if name.lower() in o['customer_name'].lower()]

    return jsonify(result)


# 4️⃣ Dashboard
@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Total orders
    total_orders = len(orders)

    # Total revenue
    total_revenue = 0
    for order in orders.values():
        total_revenue += order['total']

    # Status count
    status_count = {
        "RECEIVED": 0,
        "PROCESSING": 0,
        "READY": 0,
        "DELIVERED": 0
    }

    for order in orders.values():
        status = order['status']
        status_count[status] += 1

    return jsonify({
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "orders_per_status": status_count
    })


# Run server
if __name__ == '__main__':
    app.run(debug=True)