# 7-8. Deli
sandwich_orders = ['tuna', 'bacon', 'pastrami', 'baked bean', 'barbecue']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwich has been made.")
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")
