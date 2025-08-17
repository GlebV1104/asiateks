import os
from flask import Flask, render_template, send_from_directory , request , redirect, url_for, flash
import html
import requests
from dotenv import load_dotenv
import json


application = Flask(__name__)
load_dotenv()
application.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-me-in-prod")
# Sample product data for testing – a single product reused everywhere



TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()  # for private channel use -100... id
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage" if TELEGRAM_BOT_TOKEN else None


def load_products():
    data_path = os.path.join(application.root_path, "data", "products.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

products_data = load_products()


def _send_to_telegram(name: str, contact: str, message: str) -> bool:
    """
    Send a formatted message to a Telegram channel/chat.
    For private channels, TELEGRAM_CHAT_ID must be the numeric -100... id
    and the bot must be an admin in that channel.
    """
    if not TELEGRAM_API_URL or not TELEGRAM_CHAT_ID:
        return False

    # Escape user input for HTML parse_mode
    safe_name = html.escape(name) or "—"
    safe_contact = html.escape(contact) or "—"
    safe_message = html.escape(message) or "—"

    text = (
        "<b>ASIATEKS: новое сообщение</b>\n"
        f"<b>Имя:</b> {safe_name}\n"
        f"<b>Контакт:</b> {safe_contact}\n"
        f"<b>Сообщение:</b>\n{safe_message}"
    )
    if len(text) > 4096:
        text = text[:4093] + "…"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,     # e.g. -1001234567890 for private channel
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }

    try:
        r = requests.post(TELEGRAM_API_URL, json=payload, timeout=6)
        return r.ok
    except requests.RequestException:
        return False


# --- replace your /contact route with this version ---
@application.route("/contact", methods=["POST"])
def contact():
    name = (request.form.get("name", "") or "").strip()
    contact_value = (request.form.get("contact", "") or "").strip()
    message = (request.form.get("message", "") or "").strip()

    # Optional guardrail for very long messages
    if len(message) > 4000:
        message = message[:4000] + "…"

    sent = _send_to_telegram(name, contact_value, message)

    if sent:
        flash("Спасибо! Мы получили ваше сообщение и свяжемся с вами в ближайшее время.")
    else:
        # Keep user-facing message friendly; you can also log the failure
        flash("Спасибо! Мы получили ваше сообщение. (Заметка: уведомление в Telegram временно не отправилось.)")

    # Return back to the same page, scrolled to the contact section
    return redirect(url_for("home") + "#contact")


@application.route('/products')
def products():
    query = request.args.get('search', '').lower()
    tag_filter = request.args.get('tag', '').lower()

    filtered_products = [
        product for product in products_data
        if (query in product["title"].lower() or query in product["description"].lower())
        and (tag_filter in [t.lower() for t in product.get("tags", [])] if tag_filter else True)
    ]
    
    return render_template('products.html', products=filtered_products, query=query, tag_filter=tag_filter)
@application.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in products_data if item["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product, products=products_data)
    else:
        return "Product not found", 404
# Render the homepage using home.html
@application.route('/')
def home():
    return render_template('home.html')

# Serve static files from the 'static' folder
@application.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(application.root_path, 'static'), filename)

# Download files from the 'static/files' folder
@application.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(os.path.join(application.root_path, 'static', 'files'), filename, as_attachment=True)

@application.template_filter('intersect')
def intersect(a, b):
    return list(set(a) & set(b))

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5002 , debug=True)