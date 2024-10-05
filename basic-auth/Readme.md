# Basic Authentication with FastAPI and MySQL

This project demonstrates a simple authentication system using FastAPI, MySQL, and JWT (JSON Web Tokens) for secure user management. It provides user registration, login, and token verification functionalities.


## What is FastAPI?

FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. It allows developers to create RESTful APIs quickly and efficiently, providing automatic validation, serialization, and documentation generation through OpenAPI.


---


## Features

- **User Registration**: Create new users with a username, password, email, and name.
- **Token Generation**: Obtain a JWT after successful login for further authenticated requests.
- **Token Verification**: Check the validity of the JWT token.
- **Password Hashing**: Securely store user passwords using bcrypt hashing.

***Note*** : I have added an appendix about [JWT Tokens](#json-web-tokens-jwt).

---

## File Structure
~~~
app/
├── auth.py          # Contains authentication routes and logic
├── database.py      # Handles database interactions
├── main.py          # Entry point of the application
└── models.py        # Defines data models using Pydantic
Dockerfile           # Dockerfile for containerizing the application
docker-compose.yml   # Docker Compose file for managing services
requirements.txt     # Python package dependencies
~~~
---

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python.
- **MySQL**: A relational database for storing user data.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **JWT**: Token-based authentication for secure communication.
- **Docker**: Containerization of the application for easy deployment. (future implementation)

---

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file


~~~
MYSQL_HOST=<your_mysql_host>
MYSQL_DATABASE=<your_database_name>
MYSQL_USER=<your_mysql_user>
MYSQL_PASSWORD=<your_mysql_password>
SECRET_KEY=<your_jwt_secret_key>
ALGORITHM=<your_jwt_algorithm>
~~~
---

## API Reference

#### **Get Server Status**

```http
  GET /
```
##### **Request sample** :
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `NULL`    | `None`   | Check if the server is up. |



#### **Say Hello!**

```http
  GET /hello/${name}
```
##### **Request sample** :
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`    | `string` | **Required**. Greet the user by name. |



#### **Create User**
This call is to Create a new user in the Server System.
```http
  POST /authenticate/register
```
##### **Request sample** :
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`| `string` | **Required**. Username which is to be created. |
| `password`| `string` | **Required**. Password which is to be set. |
| `email`   | `string` | **Required**. Email\-ID which is to be registered. |
| `name`    | `string` | **Required**. Name of the user to be registered. |


#### **Generate JWT Token**
This is to generate a JWT token for active session on the frontend side.

```http
  POST /authenticate/token
```
##### **Request sample** :
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|`grant_type`| `string \| NULL` | Not Implemented aptly. So, set blank. |
| `username` | `string` | **Required**. Username for login. |
| `password` | `string` | **Required**. Password registered with Username |
| `scope`    | `string \| NULL` | Not Implemented aptly. So, set blank. |
| `client_id`    | `string \| NULL` | Not Implemented aptly. So, set blank. |
| `client_secret`| `string \| NULL` | Not Implemented aptly. So, set blank. |


#### **Verify JWT Token**
This is to verify a JWT token for active session on the frontend side.
After registering a user, you can log in to obtain a JWT. Use this token for authenticated requests by including it in the Authorization header:

```http
  POST /authenticate/verify/token
  Authorization: Bearer <your_generated_token>
```
##### **Request sample** : None

---


## Modifying the Code

To adapt this code to your specific requirements:

1. ***Add Fields***: Modify the user model in `models.py` to include additional fields (e.g., phone number).
2. ***Change Authentication Logic***: Adjust the logic in `auth.py` for user roles, such as admin or regular user, by implementing role-based access control.
3. ***Customize Endpoints***: Add or modify API endpoints in `main.py` to suit additional functionalities like password recovery or user profile management.
4. ***Modify Database Structure***: Update the MySQL database schema to accommodate new data or relationships.
<br><br>
---
---
<br> 

# JSON Web Tokens (JWT)

**JSON Web Tokens (JWT)** are an open standard (RFC 7519) used for securely transmitting information between parties as a JSON object. They are compact, URL-safe, and can be used for various authentication and information exchange scenarios.
JWTs provide a simple and efficient way to manage authentication and securely transmit information in web applications. They are widely used in modern web services and APIs due to their versatility and ease of use.

## Key Concepts of JWT:

1. **Structure**: A JWT is composed of three parts, separated by dots (`.`):
   - **Header**: Contains metadata about the token, including the type of token (usually "JWT") and the signing algorithm (like HMAC SHA256 or RSA).
   - **Payload**: Contains the claims or statements about the entity (usually the user) and any additional data. Claims can be registered (like `sub` for subject, `iat` for issued at), public (defined by those using the token), or private (custom claims).
   - **Signature**: Created by taking the encoded header, encoded payload, a secret (for HMAC) or a private key (for RSA), and signing them. This ensures that the sender of the JWT is who it says it is and that the message wasn’t changed along the way.

The overall structure looks like this:
`<header>.<payload>.<signature> `

2. **Usage**:
    - **Authentication**: After a user logs in, a JWT is generated and sent back to the client. The client then sends this token in subsequent requests, allowing the server to verify the user’s identity without needing to keep session state.
    - **Information Exchange**: JWTs can be used to transmit information securely between parties. Since the content is signed, the recipient can verify that the sender is who they claim to be and that the message wasn't tampered with.

3. **Benefits**:
    - **Stateless**: JWTs are stateless and self-contained; they carry all the necessary information about the user, reducing the need for server-side sessions.
    - **Cross-Domain**: Since they are URL-safe, JWTs can be used across different domains and platforms.
    - **Scalability**: With no server-side storage required, scaling applications becomes easier as user sessions do not need to be stored in a central database.
## Example Use Case
1. User logs in with their credentials (username and password).
2. Server verifies the credentials and creates a JWT with user information and sends it back to the user.
3. The user stores the JWT (usually in local storage) and sends it in the Authorization header as a Bearer token in subsequent requests:
```http
Authorization: Bearer <JWT>
```
4. The server verifies the JWT and processes the request accordingly.
<br><br>
---
---
