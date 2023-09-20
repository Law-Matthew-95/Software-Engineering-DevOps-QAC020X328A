SoftwareEngineering-Agile_Assignment-QAC020N227S-

This application is uses the Flask environment with the python language and a SqlLite database to create a simple ticket system which features Logging in, signing up,ticket creation, ticket editting, ticket deletion, Admin upgrading, logout, and user deletion.

There are two types of tiers of users, normal and admin.

With an empty database, the first user registered will be an admin. From there, any further users created will not have the admin privileges.

Normal users have the ability to:
    - Create a new ticket which will be assigned to that user,
    - View all of their tickets on their home screen,
    - Edit any of their tickets,
    - Delete their tickets.

Admin users have the ability to:
    - Create a new ticket which will be assigned to that user,
    - View all of their tickets on their home screen,
    - Edit any of their tickets,
    - Delete their tickets,
    - View all of the tickets that are in the database,
    - View all of the users,
    - Edit any ticket,
    - Delete any ticket,
    - Delete any non-admin user,
    - Assign admin privileges to a non-admin user,
