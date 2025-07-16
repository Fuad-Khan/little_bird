from services.models import Category, Service, Area

# Optional: Add some dummy areas if not added yet
area_names = ['Dhaka', 'Chattogram', 'Khulna', 'Rajshahi', 'Sylhet']
for name in area_names:
    Area.objects.get_or_create(name=name)

areas = list(Area.objects.all())  # will assign to all services

data = {
    "Cleaning & Hygiene": {
        "icon": "fa-soap",
        "services": [
            "Home Deep Cleaning", "Bathroom Cleaning", "Kitchen Cleaning",
            "Sofa & Mattress Cleaning", "Carpet Cleaning", "Water Tank Cleaning",
            "Sanitization Services", "Pest Control"
        ]
    },
    "General Repair & Maintenance": {
        "icon": "fa-tools",
        "services": [
            "Electrician", "Plumber", "Carpenter", "Handyman",
            "AC Repair & Servicing", "Refrigerator Repair", "Washing Machine Repair",
            "TV/LED Repair", "Inverter/UPS Setup"
        ]
    },
    "Appliance Services": {
        "icon": "fa-cogs",
        "services": [
            "Microwave Oven Repair", "Geyser Repair & Installation",
            "Water Purifier Maintenance", "Fan/Exhaust Setup", "Doorbell/Intercom Repair"
        ]
    },
    "Home Improvement": {
        "icon": "fa-paint-roller",
        "services": [
            "Interior Painting", "Wallpaper Installation", "False Ceiling Work",
            "Modular Kitchen Setup", "Tile/Marble Polishing", "Furniture Assembly"
        ]
    },
    "Outdoor & Gardening": {
        "icon": "fa-seedling",
        "services": [
            "Gardening Services", "Lawn Mowing", "Roof Cleaning",
            "Gutter Maintenance", "Tree Trimming & Removal"
        ]
    },
    "Smart Home & Digital Services": {
        "icon": "fa-wifi",
        "services": [
            "CCTV Installation", "Wi-Fi Setup", "Smart Home Automation",
            "Door Lock & Security Systems", "PC/Laptop Repair", "Mobile Repair"
        ]
    },
    "Essentials & Decor": {
        "icon": "fa-couch",
        "services": [
            "Curtain & Rod Setup", "Mirror/Glass Fitting",
            "Wall Shelves & TV Mounting", "Baby Proofing Services"
        ]
    },
    "Movers & Logistics": {
        "icon": "fa-truck",
        "services": [
            "Furniture Shifting", "Home Shifting", "Packers & Movers", "Local Delivery Help"
        ]
    },
}

for cat_name, details in data.items():
    category, _ = Category.objects.get_or_create(name=cat_name, icon=details["icon"])
    for title in details["services"]:
        service, created = Service.objects.get_or_create(
            title=title,
            category=category,
            defaults={
                "description": f"{title} service provided by trusted professionals.",
                "price": 500.00,
                "is_available": True,
            }
        )
        if created:
            service.area.set(areas)
