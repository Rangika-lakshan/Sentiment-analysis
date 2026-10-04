import json
vehival_entity ={
    "motorvehicles": {
        "registration_nb":"cbb2432",
        "make":"Toyota",
        "model" :"premio"
    },"owner" :{
        "first_name": "amal",
        "last_name" : "perera",
        "nic" : "4324442v"
    }
}
serialized = json.dumps(vehival_entity)

print("-----------------START-----------------")
print("Serialized :", serialized )

print("--------------------------------------------")
deserialized = json.loads(serialized)
print("Deserialized :", deserialized)
print("--------------------------------------------")
print(deserialized["motorvehicles"]["registration_nb"],
      deserialized["motorvehicles"]["model"])
print("-------------------END-------------------")