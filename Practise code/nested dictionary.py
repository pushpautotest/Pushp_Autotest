# Nested dictionary
#
# emp = {
#     "Pushpender" : {
#         "emp id" : 123,
#         "Designation" : "Qa"
#     },
#     "Bhupinder" : {
#         "emp id" : 124,
#         "Designation" : "Dev"
#     },
#     "Aditya" : {
#             "emp id" : 125,
#             "Designation" : "Dev"
#         }
# }
# print(emp)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
Pushpender= {
        "emp id" : 123,
        "Designation" : "Qa"
    }
Bhupinder = {
        "emp id" : 124,
        "Designation" : "Dev"
    }
Aditya = {
            "emp id" : 125,
            "Designation" : "Dev"
        }
print (Pushpender)
print (Bhupinder)
print (Aditya)
myteam = {
    "pushpender" : Pushpender,
    "Bhupinder" : Bhupinder,
    "Aditya" : Aditya
}
print(myteam)
