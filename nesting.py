# Nesting List in a Dictionary


travel_log = {
    "France" : "Paris",
    "Germany" : "Berlin",
}
print("---------------------------------")
print ("+Nesting List in a Dictionary+\n")
print("---------------------------------")
print (travel_log)

# Nesting Dict in a Dict

travel_log1 = {
    "France" : {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany" : {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
print("----------------------------------------")
print("\n+Nesting a Dictionary in a Dictionary+\n")
print("----------------------------------------")
print (travel_log1)

# Nesting dictionary in a List

travel_log2 = [{
    
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits":12,
    
},
{
    "country": "Germany",
    "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
    "total_visits":5

},              
 ]
print("--------------------------------")
print("\n+Nesting Dictionary in a List+\n")
print("---------------------------------")
print (travel_log2)