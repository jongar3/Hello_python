from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "machop"])
table.add_column("Type", ["Electric", "Water", "Fight"])
table.add_column("Attack", ["Special", "Special", "Physical"])
table.align = "l"
print(table)
print(table.align)