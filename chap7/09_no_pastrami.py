sandwich_orders = ['tuna', 'ham', 'turkey', 'veggie', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich} sandwich")