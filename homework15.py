import requests
import json

url = 'https://dummyjson.com/products?limit=200'

response = requests.get(url)
response_json = response.json()

tech_products = [product['id'] for product in response_json['products'] if product.get('brand') == 'TechGear']
print("ID продуктів бренду TechGear:", tech_products)

product_id = 135
product = next((product for product in response_json['products'] if product['id'] == product_id), None)

if product:
    image_url = product['thumbnail']

    img_response = requests.get(image_url)

    if img_response.status_code == 200:
        with open('phone.png', 'wb') as img_file:
            img_file.write(img_response.content)

premium_products = [product for product in response_json['products'] if product['price'] > 800]
total_value = sum(product['price'] * product['stock'] for product in premium_products)
print(f"Загальна вартість преміальних товарів: {total_value}")

pass
