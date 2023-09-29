This project is a RESTful API designed to manage a list of users.

Installation and Setup

Prerequisites
Docker
Docker Compose
Installation Steps
Clone the repository:
bash
Copy code
git clone https://github.com/AbuMuhammad92/miproject.git
cd miproject
Launch the services using Docker Compose:
bash
Copy code
docker-compose up
Once done, your application should be accessible at http://localhost:8000/.

API Usage

The application provides a Swagger UI for convenient API testing. To access the Swagger UI, navigate to:

http://localhost:8000/swagger/?format=openapi

Endpoints
Retrieve a list of all users
Method: GET
URL: /users/
Create a new user
Method: POST
URL: /users/
Retrieve details of a specific user
Method: GET
URL: /users/{id}/
Update a user's details
Method: PUT
URL: /users/{id}/
Partially update a user's details
Method: PATCH
URL: /users/{id}/
Delete a user
Method: DELETE
URL: /users/{id}/
Dependencies

All Python dependencies required for this project are listed in the requirements.txt file.
