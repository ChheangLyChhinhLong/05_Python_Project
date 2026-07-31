# Python Dictionaries | ពាក្យសម្ងាត់ Python
product_dic = {
    "pro_id": 1,
    "pro_name": "iPhone 17",
    "brand": "Apple",
    "category": "Smart Phone",
    "color": "Orange",
    "storage": "1000",
    "model": "Pro max",
    "price": 1500
}

# Get is method use to get value by key | Get ជា method ដែលប្រើសម្រាប់ទាញយកតម្លៃតាម key
def get(key: str):
    return product_dic[key] # Return value by key | ត្រឡប់តម្លៃតាម key

# Update is method use to update value by key | Update ជា method ដែលប្រើសម្រាប់ធ្វើបច្ចុប្បន្នភាពតម្លៃតាម key
def update(key: str, value: str | float | int):
    product_dic[key] = value # Update value by key | បច្ចុប្បន្នភាពតម្លៃតាម key
update("pro_name", "iPhone 18") # Update product name | បច្ចុប្បន្នភាពឈ្មោះផលិតផល
update("price", 1450) # Update product price | បច្ចុប្បន្នភាពតម្លៃផលិតផល

# Result | លទ្ធផល
print(f"Product ID: {get('pro_id')}")
print(f"Product Name: {get('pro_name')}")
print(f"Product Brand: {get('brand')}")
print(f"Product Category: {get('category')}")
print(f"Product Color: {get('color')}")
print(f"Product Storage: {get('storage')}")
print(f"Product Model: {get('model')}")
print(f"Product Price: {get('price')}")