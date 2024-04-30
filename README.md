# OurBank (Fintech Neo Bank)

![Logo for OurBank](Images/OurBank.png)

## Project Duration: 2 weeks

### Project Structure

```bash
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
│   ├── cryptoService.py      # Service for crypto wallet and blockchain (Metamask, Ganache, Remix)
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

### Project Overview
The following task mandate outlines the responsibilities for each team member involved in the OurBank project. The project is a simplified backend for a fintech neo bank with key features such as checking and savings accounts, crypto wallets, blockchain integration, and machine learning for portfolio recommendations.

### Work Assignments

#### Person 1: SQL Database and Data Model Design
Responsible for setting up the SQL database and creating data models to ensure proper structure and relationships.

- **Tasks:**
  - `config/database.py`: Configure the database and set up the initial structure.
  - `models/user.py`: Define the user model for authentication and user roles.
  - `models/account.py`: Define models for checking and savings accounts.
  - `models/wallet.py`: Create the crypto wallet model.
  - `models/transaction.py`: Create the transaction model for banking and crypto operations.

#### Person 2: Account Creation and Authentication
Focuses on user registration, login, and JWT-based authentication, ensuring secure user management.

- **Tasks:**
  - `controllers/authController.py`: Implement logic for user authentication (e.g., login, logout, registration).
  - `routes/authRoutes.py`: Define API endpoints for authentication.
  - `services/authService.py`: Core logic for authentication and JWT token handling.
  - `middlewares/authMiddleware.py`: Middleware for authentication checks and token validation.
  - `config/.env`: Set up environment variables, including JWT secret keys and other sensitive data.
  - `models/user.py`: Ensure the user model supports authentication fields like password hashes and roles.

#### Person 3: Banking Functionalities (Checking, Savings, Transactions, and Interest Calculation)
Responsible for implementing the core banking functionalities, including account management and transactions.

- **Tasks:**
  - `controllers/bankingController.py`: Implement logic for managing checking and savings accounts and handling transactions.
  - `routes/bankingRoutes.py`: Define API endpoints for banking operations.
  - `services/bankingService.py`: Implement service logic for banking functions, including interest calculation.
  - `models/account.py`: Ensure account models support checking and savings accounts.
  - `models/transaction.py`: Handle transactions for banking operations (deposits, withdrawals, transfers).
  - `middlewares/errorHandler.py`: Middleware for error handling and graceful error responses.

#### Person 4: Machine Learning and Blockchain/Smart Contract Support
Develops machine learning functionality and integrates blockchain/smart contract support for the crypto wallet.

- **Tasks:**
  - `controllers/mlController.py`: Implement controller logic for machine learning (e.g., portfolio recommendations).
  - `routes/mlRoutes.py`: Define API endpoints for machine learning operations.
  - `services/mlService.py`: Service logic for portfolio recommendations or other ML tasks.
  - `controllers/cryptoController.py`: Manage crypto wallet and smart contract interactions.
  - `routes/cryptoRoutes.py`: Define API endpoints for crypto wallet operations.
  - `services/cryptoService.py`: Service logic for crypto wallet and blockchain integration.
  - `config/blockchain.py`: Configure blockchain settings for smart contract interactions.
  - `models/wallet.py`: Ensure the crypto wallet model supports blockchain interactions, including smart contracts.

### Collective Effort
This project requires a collaborative effort, so don't hesitate to ask for clarification when needed. Use classwork codes or online resources (Slack, YouTube, ChatGPT) to generate baseline code for your tasks.

### Frontend Development
For this project, a simple HTML frontend will be used to connect with the backend for our group presentation. A prebuilt theme will be integrated with the backend functionalities.

### Final Notes
Happy coding! Let's work together to build a great project.
