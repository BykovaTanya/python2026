shipments = [
    {"city": "Москва", "items": 40, "delivered": 40},
    {"city": "Ярославль", "items": 18, "delivered": 10},
    {"city": "Пермь", "items": 25, "delivered": 12}
]
delivery_status = {
    shipment["city"]: ("готово" if shipment["delivered"] == shipment["items"] else "в пути")
    for shipment in shipments
    if shipment["items"] >= 20
}

        #if shipment["delivered"] == shipment["items"]
            #delivery_status[city] = "готово"
        #else:
            #delivery_status[city] = "в пути"
        
print(delivery_status)


