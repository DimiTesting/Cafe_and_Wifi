list = {
  "cafe": [
    {
      "can_take_calls": "true",
      "coffee_price": "\u00a32.40",
      "has_sockets": "true",
      "has_toilet": "true",
      "has_wifi": "false",
      "id": 1,
      "location": "London Bridge",
      "map_url": "https://g.page/scigallerylon?share",
      "name": "Science Gallery London",
      "seats": "50+"
    },
    {
      "can_take_calls": "false",
      "coffee_price": "\u00a32.75",
      "has_sockets": "true",
      "has_toilet": "true",
      "has_wifi": "true",
      "id": 2,
      "location": "Peckham",
      "map_url": "https://g.page/CopelandSocial?share",
      "name": "Social - Copeland Road",
      "seats": "20-30"
    }]}

for item in list["cafe"]:
    print(item["location"])

