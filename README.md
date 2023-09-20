### SoftwareEngineering-Agile_Assignment-QAC020N227S-

This application is uses the Flask environment with the python language and a SqlLite database to create a simple ticket system which features Logging in, signing up,ticket creation, ticket editting, ticket deletion, Admin upgrading, logout, and user deletion.

There are two types of users, normal and admin.

With an empty database, the first user registered will be an admin. From there, any further users created will not have the admin privileges.

# Normal users have the ability to:
    - Create a new ticket which will be assigned to that user,
    - Read all of their tickets on their home screen,
    - Update any of their tickets,
    - Delete their tickets.

# Admin users have the ability to:
    - Create a new ticket which will be assigned to that user,
    - Read all of their tickets on their home screen,
    - Update any of their tickets,
    - Delete their tickets,
    - Read all of the tickets that are in the database,
    - Read all of the users,
    - Update any ticket,
    - Delete any ticket,
    - Delete any non-admin user,
    - Update admin privileges to a non-admin user,
