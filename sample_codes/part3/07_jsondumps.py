import json

menu={ 
    "breakfast": {
        "hours": "7-11",
        "items": {
            "burritos": "$60",
            "pancakes": "$40"
        }
    },
    "lunch" : {
        "hours": "11-3",
        "items": {
            "hamburger": "$50"
        }
    },
    "dinner": {
        "hours": "3-10",
        "items": {
            "spaghetti": "$80"
        }
    }
 }
menu_json=json.dumps(menu)
print(menu_json)
menu_json2=json.dumps(menu,indent=2)
print(menu_json2)