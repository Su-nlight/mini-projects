from __future__ import annotations  # Import future annotations for Python 3.7+ compatibility
import os
from datetime import timedelta, datetime  # Import timedelta and datetime to handle expiration times
from fastapi import APIRouter, Depends, HTTPException  # Import FastAPI tools for routing and exception handling
from starlette import status  # Import status codes for HTTP responses
from models import CreateUser, Token, CreateUserDatabase  # Import custom models for user and token data
from passlib.context import CryptContext  # Import PassLib for password hashing
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer  # Import OAuth2 tools for authentication
from jose import jwt, JWTError  # Import JWT and JWTError from jose to handle token creation and verification
from database import Database  # Import the Database class for user database operations
from dotenv import load_dotenv  # Import to load environment variables from .env file

# Initialize an API router for authentication-related routes
router = APIRouter(
    prefix='/authenticate',  # Prefix for all routes in this router
    tags=['authenticate']  # Tag for grouping routes in the FastAPI documentation
)

# Load environment variables from the .env file
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')  # Load secret key from environment variables for JWT
ALGORITHM = os.getenv('ALGORITHM')  # Load JWT algorithm from environment variables

# Initialize a password hashing context using bcrypt
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Initialize OAuth2PasswordBearer for token-based authentication
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="authenticate/token")


def generate_payload(username: str, expiration: timedelta | None = None):
    """
    Generate a JWT payload for a user.

    Args:
        username (str): Username to include in the token.
        expiration (timedelta | None): Optional expiration time for the token.

    Returns:
        str: The generated JWT token.
    """
    if expiration is None:
        expiration = timedelta(hours=1)  # Set default expiration time to 1 hour if not provided
    payload = {
        "username": username,  # Include the username in the payload
        "iat": datetime.utcnow(),  # Issued at time (current time)
        "exp": datetime.utcnow() + expiration  # Expiration time for the token
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')  # Encode the payload into a JWT token using HS256
    return token  # Return the generated token


def token_verifier(token: str = Depends(oauth2_bearer)):
    """
    Verify the validity of a JWT token.

    Args:
        token (str): The JWT token to verify.

    Returns:
        dict: The decoded payload if the token is valid.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    try:
        # Decode the token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('username')  # Extract the username from the token payload
        if username is None:
            # Raise an exception if the username is missing in the token
            raise HTTPException(status_code=403, detail="Token is Invalid or expired")
        return payload  # Return the token payload if valid
    except JWTError:
        # Raise an exception if there is an error in decoding or verifying the token
        raise HTTPException(status_code=403, detail="Token is Invalid or expired")
    finally:
        pass  # [Warning] The `finally` block is not necessary here since there's no resource cleanup needed


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(create_new_user: CreateUser):
    """
    Create a new user in the system.

    Args:
        create_new_user (CreateUser): The user data for creating a new user.

    Returns:
        dict: A success message confirming the user creation.
    """
    # Hash the password and prepare the new user request for the database
    new_user_request = CreateUserDatabase(
        username=create_new_user.username,
        hashed_password=bcrypt_context.hash(create_new_user.password),  # Hash the user's password
        email=create_new_user.email,
        name=create_new_user.name
    )

    # Store the new user in the database
    Database.create_user(user_data=new_user_request)
    # Return a success message after the user is created
    return {'message': f'User {new_user_request.username} created successfully'}


@router.post('/token', response_model=Token)
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Generate a JWT token for the user after validating credentials.

    Args:
        form_data (OAuth2PasswordRequestForm): The login form data with username and password.

    Returns:
        dict: A token response with access token and token type.

    Raises:
        HTTPException: If the username or password is incorrect.
    """
    # Retrieve the hashed password for the provided username from the database
    hashed_pass = Database.get_user_pass(username=form_data.username)

    # Verify if the password is correct using the hashed password
    if not hashed_pass or not bcrypt_context.verify(form_data.password, hashed_pass):
        # Raise an exception if the credentials are incorrect
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')

    # Generate a JWT token with a custom expiration time (1 hour 40 minutes)
    token = generate_payload(username=form_data.username, expiration=timedelta(hours=1, minutes=40))

    # Return the generated access token and token type
    return {"access_token": token, "token_type": "Bearer"}


@router.get("/verify/token")
async def verify_token(token: str = Depends(oauth2_bearer)):
    """
    Verify if the provided JWT token is valid.

    Args:
        token (str): The JWT token to verify (injected by OAuth2PasswordBearer).

    Returns:
        dict: A success message confirming token validity.
    """
    # Verify the token using the token verifier function
    token_verifier(token=token)

    # Return a message if the token is valid
    return {"message": "token is valid"}
