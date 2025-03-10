group_details = []


for i in range(5):
    print("Enter details for Group:")
    groupname = input("Group Name: ")
    nummembers = int(input("Number of Members: "))
    competitiondate = input("Competition Date: ")
    venue = input("Venue: ")
    medaltype = input("Medal Type (Gold/Silver/Bronze): ")


    group_tuple = (groupname, nummembers, competitiondate, venue, medaltype)
    

    group_details.append(group_tuple)

print("Recorded Details:")
for i in group_details:
    print(i)
