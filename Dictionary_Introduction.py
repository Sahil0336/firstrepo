customer = {
    "name": "mohamed sahil ali",
    "email": "mohamedsahil0336@gmail.com",
    "phone": "987654321",
    "age": "20"
}
customer["birthday"]= "22nd july 2002"
customer["name"]= "Md sahil ali"       # It changes the key value
print(customer["name"])
print(customer.get("random", "nothing to show")) #[using get command for so the interpreter doesn't yell at you]