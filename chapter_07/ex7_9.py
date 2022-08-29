# 7-9. No pastrami
sandwich_orders = ['tuna', 'bacon', 'pastrami', 'baked bean', 'barbecue', 'pastrami', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwich has been made.")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")
