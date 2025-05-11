"""Use lambda to filter users with a balance over a certain amount"""

# Users
users = {
    "1234": {"name": "Alice", "balance": 500},
    "5678": {"name": "Bob", "balance": 300},
    "2468": {"name": "Charlie", "balance": 750},
    "1357": {"name": "Diana", "balance": 620},
    "1122": {"name": "Ethan", "balance": 400},
    "3344": {"name": "Fiona", "balance": 1000},
    "5566": {"name": "George", "balance": 150},
    "7788": {"name": "Hannah", "balance": 920},
    "9900": {"name": "Ivan", "balance": 0},
    "2020": {"name": "Jade", "balance": 850},
}

rich_users = list(filter(lambda x: users[x]['balance'] >= 500, users))

print('User with balance > or == to 500')
for pin in rich_users:
    print(f"{users[pin]['name']} - {users[pin]['balance']}")

