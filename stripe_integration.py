
import stripe
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace with your actual secret key
stripe.api_key = "your_stripe_secret_key"

# Set your Stripe webhook secret if using one
# STRIPE_WEBHOOK_SECRET = "your_webhook_secret"

# === Create Checkout Session ===
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        data = request.get_json()
        promo_code = data.get("promo_code", "").strip().upper()
        lookup_key = "annual_subscription"

        # Fetch your actual price ID from Stripe
        price_id = "price_XXXXXXXXXXXXXX"

        # Optionally validate the promo code using Stripe API (coupon or promotion_code list)
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription",
            line_items=[{
                "price": price_id,
                "quantity": 1,
            }],
            discounts=[{"promotion_code": promo_code}] if promo_code else [],
            success_url="https://trueratetexas.com/success",
            cancel_url="https://trueratetexas.com/cancel",
        )

        return jsonify({'checkout_url': session.url})
    except Exception as e:
        return jsonify(error=str(e)), 400
