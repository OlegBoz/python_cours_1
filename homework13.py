car_specifications = {
    "Petrol_2.5_171hp_4x2_CVT": {
        "price": 800000,
        "is_rear_led_lights_with_dynamic_turn_signals": True,
        "exterior_design_elements": [
            "Sleek headlights",
            "Stylish grille",
            "Dynamic bumper",
            "17-inch alloy wheels",
            "LED daytime running lights",
            "Fog lights",
            "Silver roof rails",
            "Chrome accents",
            "Sporty rear design",
            "Integrated turn signals"
        ],
        "panoramic_glass_roof": {
            "price": 20000
        },
        "engine_capacity": "2.5L",
        "horsepower": 171,
        "transmission": "CVT",
        "drive_type": "4x2"
    },
    "Petrol_2.5_171hp_4x4_CVT_INTENSE": {
        "price": 950000,
        "is_rear_led_lights_with_dynamic_turn_signals": False,
        "exterior_design_elements": [
            "Bold front lights",
            "Aggressive stance",
            "20-inch alloy wheels",
            "Luminous daytime lights",
            "Enhanced bumper design",
            "Sporty side skirts",
            "Rear spoiler",
            "LED fog lights",
            "Chrome front grille",
            "Metallic paint options"
        ],
        "panoramic_glass_roof": {},
        "engine_capacity": "2.5L",
        "horsepower": 171,
        "transmission": "CVT",
        "drive_type": "4x4"
    }
}


intense_roof_price = car_specifications["Petrol_2.5_171hp_4x4_CVT_INTENSE"]["panoramic_glass_roof"].get("price", "N/A")
print(f"price for glass roof for car 2,5 (171 hp) 4х4 АКП (CVT) (INTENSE) is: {intense_roof_price}")

print("\n Exterior design for car 2,5 (171 hp) 4х4 АКП (CVT) (INTENSE):")
for element in car_specifications["Petrol_2.5_171hp_4x4_CVT_INTENSE"]["exterior_design_elements"]:
    print(f"- {element}")
