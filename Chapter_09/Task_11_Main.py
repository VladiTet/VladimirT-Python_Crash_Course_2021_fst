from Task_11 import Admin

vladi = Admin('Vladi', 'Tetevenski', 'vtet03', 'vtet@example.com', 'Bulgaria')
vladi.describe_user()

vladi_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
vladi.privileges.privileges = vladi_privileges

print(f"\nThe admin {vladi.username} has these privileges: ")
vladi.privileges.show_privileges()
