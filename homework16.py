import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class ZooHandler(BaseHTTPRequestHandler):
    animals = [
        {
            "name": "Кобра",
            "is_poisonous": True,
            "care_cost": 1200.50,
            "quantity": 3,
            "continent": "Азія"
        },
        {
            "name": "Слон",
            "is_poisonous": False,
            "care_cost": 3000.00,
            "quantity": 2,
            "continent": "Африка"
        },
        {
            "name": "Кенгуру",
            "is_poisonous": False,
            "care_cost": 1500.25,
            "quantity": 5,
            "continent": "Австралія"
        },
        {
            "name": "Жаба",
            "is_poisonous": True,
            "care_cost": 200.75,
            "quantity": 10,
            "continent": "Південна Америка"
        },
        {
            "name": "Лев",
            "is_poisonous": False,
            "care_cost": 2500.00,
            "quantity": 4,
            "continent": "Африка"
        }
    ]

    def do_GET(self):
        if self.path == '/animals':
            self._send_response(self.animals)
        elif self.path == '/poisonous-care-cost':
            total_cost = sum(animal['care_cost'] * animal['quantity'] for animal in self.animals if animal['is_poisonous'])
            self._send_response({"total_poisonous_care_cost": total_cost})
        elif self.path == '/african-animals-count':
            african_count = sum(animal['quantity'] for animal in self.animals if animal['continent'] == "Африка")
            self._send_response({"african_animals_count": african_count})
        elif self.path == '/most-expensive-animal':
            most_expensive = max(self.animals, key=lambda x: x['care_cost'])
            self._send_response(most_expensive)
        else:
            self.send_error(404, "Not Found")

    def _send_response(self, data):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=ZooHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущено на порту {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()


import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

BASE_URL = "http://127.0.0.1:8080"

def get_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    response.raise_for_status()
    return response.json()

poisonous_care_cost = get_data("poisonous-care-cost")["total_poisonous_care_cost"]
print("Загальна вартість догляду за отруйними тваринами:", poisonous_care_cost)

african_animals_count = get_data("african-animals-count")["african_animals_count"]
print("Кількість африканських тварин у зоопарку:", african_animals_count)

most_expensive_animal = get_data("most-expensive-animal")

EMAIL_ADDRESS = "test_hillel_api_mailing@ukr.net"
RECIPIENT_EMAIL = "test_hillel_api_mailing@ukr.net"

subject = "Інформація про найдорожчу тварину"
msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = RECIPIENT_EMAIL
msg["Subject"] = subject

animal_name = most_expensive_animal["name"]
care_cost = most_expensive_animal["care_cost"]
is_poisonous = most_expensive_animal["is_poisonous"]

body = f"Найдорожча тварина в догляді: {animal_name}\nВартість догляду: {care_cost} грн."

if is_poisonous:
    body = f"<h3>Обережно: Тварина є отруйною!</h3>\n" + body

msg.attach(MIMEText(body, "html" if is_poisonous else "plain"))

with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
    server.login(EMAIL_ADDRESS)
    server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, msg.as_string())

print("Лист надіслано успішно.")
