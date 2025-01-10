### Software Engineering & DevOps (QAC020X328A)

This application uses the Flask environment with the python language and a SQLite database to create a simple ticket system which features Logging in, signing up, ticket creation, ticket editing, ticket deletion, Admin upgrading, logout, and user deletion.

There are two types of users, normal and admin.

With an empty database, the first user registered will be an admin. From there, any further users created will not have the admin privileges.

Admin:
	Email: admin@test.com
	Password: password
User1:
	Email: user@test.com
	Password:password
User2:
	Email: user2@test.com
	Password:password


# Normal users have the ability to:
    - Create a new ticket which will be assigned to that user,
    - Read all their tickets on their home screen,
    - Update any of their tickets,
    - Delete their tickets.

# Admin users have the ability to:
    - Create a new ticket which will be assigned to that user,
    - Read all their tickets on their home screen,
    - Update any of their tickets,
    - Delete their tickets,
    - Read all the tickets that are in the database,
    - Read all the users in the database,
    - Update any ticket,
    - Delete any ticket,
    - Delete any non-admin user,
    - Update admin privileges to a non-admin user,
