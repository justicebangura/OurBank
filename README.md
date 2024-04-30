# OurBank(Fintech Neo Bank)

![Logo for OurBank](Images\logo2 (2).png)

## Project Duration: 2 weeks 

/OurBank/
│
├── /config
│   ├── app.py                # Flask app setup and configuration
│   ├── database.py           # Database configuration (e.g., SQLite)
│   └── .env                  # Environment variables (JWT secrets, DB connections)
│
├── /controllers
│   ├── authController.py     # User authentication and authorization
│   ├── bankingController.py  # Checking, savings, and transactions
│   ├── cryptoController.py   # Crypto wallet and blockchain interactions
│   └── mlController.py       # Portfolio recommendations (machine learning)
│
├── /models
│   ├── user.py               # User model (authentication and roles)
│   ├── account.py            # Account model (checking, savings)
│   ├── wallet.py             # Crypto wallet model
│   └── transaction.py        # Transaction model for banking and crypto
│
├── /routes
│   ├── authRoutes.py         # Routes for authentication-related API endpoints
│   ├── bankingRoutes.py      # Routes for banking operations
│   ├── cryptoRoutes.py       # Routes for crypto wallet operations
│   └── mlRoutes.py           # Routes for machine learning endpoints
│
├── /middlewares
│   ├── authMiddleware.py     # Middleware for authentication and authorization checks
│   └── errorHandler.py       # Middleware for handling errors and exceptions
│
├── /services
│   ├── authService.py        # Service for authentication (JWT creation, user verification)
│   ├── bankingService.py     # Service for banking operations (checking, savings, transactions)
│   ├── cryptoService.py      # Service for crypto wallet and blockchain connected to a deployed smart contract(Metamask,Genache,Remix)
│   └── mlService.py          # Service for machine learning (portfolio recommendations)
│
├── /api
│   ├── auth.py               # API endpoints for authentication
│   ├── banking.py            # API endpoints for banking operations
│   ├── crypto.py             # API endpoints for crypto wallet and blockchain
│   └── ml.py                 # API endpoints for machine learning operations
│
└── /static
    ├── css/                  # CSS files for frontend styling
    ├── js/                   # JavaScript files for frontend interactivity
    ├── img/                  # Images or icons used by the frontend
    └── index.html            # Main HTML file for frontend


## Task Mandate

Person 1:(SQL database) Work on SQL database and data model design. This person ensures the correct database setup and implementation of data models.

Tasks:
config/database.py: Configure the database and set up the initial structure.
models/user.py: Define the user model for authentication and user roles.
models/account.py: Define models for checking and savings accounts.
models/wallet.py: Create the crypto wallet model.
models/transaction.py: Create the transaction model for banking and crypto operations.

Person 2:(ACCOUNT logic) Handle account creation and authentication. This person focuses on user registration, login, and JWT-based authentication.

Tasks:
controllers/authController.py: Implement logic for user authentication (e.g., login, logout, registration).
routes/authRoutes.py: Define API endpoints for authentication.
services/authService.py: Core logic for authentication and JWT token handling.
middlewares/authMiddleware.py: Middleware for authentication checks and token validation.
config/.env: Set up environment variables, including JWT secret keys and other sensitive data.
models/user.py: Ensure the user model supports authentication fields like password hashes, roles, etc.

Person 3:(Banking function) Implement banking functionalities, including checking and savings accounts, transactions, and interest calculation.

Tasks:
controllers/bankingController.py: Implement logic for managing checking and savings accounts, and handling transactions.
routes/bankingRoutes.py: Define API endpoints for banking operations.
services/bankingService.py: Implement service logic for banking functions, including interest calculation.
models/account.py: Ensure account models support checking and savings accounts.
models/transaction.py: Handle transactions for banking operations (deposits, withdrawals, transfers).
middlewares/errorHandler.py: Middleware for error handling and graceful error responses.

Person 4:(Machine Learning/Blockchain) Develop machine learning functionality and integrate blockchain/smart contract support for the crypto wallet.

Tasks:
controllers/mlController.py: Implement controller logic for machine learning (e.g., portfolio recommendations).
routes/mlRoutes.py: Define API endpoints for machine learning operations.
services/mlService.py: Service logic for portfolio recommendations or other ML tasks.
controllers/cryptoController.py: Manage crypto wallet and smart contract interactions.
routes/cryptoRoutes.py: Define API endpoints for crypto wallet operations.
services/cryptoService.py: Service logic for crypto wallet and blockchain integration.
config/blockchain.py: Configure blockchain settings for smart contract interactions.
models/wallet.py: Ensure the crypto wallet model supports blockchain interactions, including smart contracts.


*Its a collective group effort so feel free to ask for clarification when necessary use classwork codes or online resources(slack,Youtube,Chatgpt to generate baseline codes) ----> 


Simplified Front End development

We will use a HTML frontend as its easier to connect for our group presentation

I have downloaded a prebuilt theme we can connect our backend functionalities to!

Happy Coding!!

