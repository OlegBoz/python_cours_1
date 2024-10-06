car = {
    "car4x2": {
        "price": 800000,
        "led_lights": True,
        "exterior_design_elements": [
            "Sleek headlights",
            "Stylish grille",
            "Dynamic bumper",
            "17-inch alloy wheels",
            "LED daytime running lights"
        ],
        "panoramic_glass_roof": {
            "price": 20000
        }
    },
    "car4x4": {
        "price": 950000,
        "led_lights": False,
        "design": [
            "Bold front lights",
            "Aggressive stance",
            "20-inch alloy wheels",
            "Luminous daytime lights",
            "Enhanced bumper design"
        ],
        "panoramic_glass_roof": {}
    }
}

intense_roof_price = car["car4x4"]["panoramic_glass_roof"].get("price","N/A")
print(f"price for glass roof for car4x4: {intense_roof_price}")

for element in car["car4x4"]["design"]:
    print(f"design: {element}")


