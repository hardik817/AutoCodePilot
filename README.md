# CodeAutoPilot

# 🧠 EngineeringTeam: CrewAI-Powered Account Management System

This project demonstrates a multi-agent engineering team powered by [CrewAI](https://github.com/joaomdmoura/crewAI), collaborating to design, build, and test an account management system for a trading simulation platform.

## 🚀 Project Objective

To build a robust **account management system** that supports:
- User account creation
- Deposits and withdrawals
- Buying and selling of stocks
- Real-time portfolio valuation
- Profit/loss calculation
- Transaction history
- Basic constraints like no overdrafts or overselling

It leverages a function `get_share_price(symbol)` to retrieve stock prices and simulate trading behavior.

## 🧩 Crew Structure

This project defines a Crew using the `CrewBase` class with the following agents and tasks:

### 👥 Agents
| Role               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `engineering_lead` | Coordinates the project and oversees implementation                         |
| `backend_engineer` | Implements logic for account handling, trading, and fund management         |
| `frontend_engineer`| Designs and outlines the interface or user interaction logic                |
| `test_engineer`    | Writes test cases to validate logic and constraints                         |

### 🧠 Tasks
| Task Name       | Description                                        |
|------------------|----------------------------------------------------|
| `design_task`    | Converts requirements into a design plan           |
| `code_task`      | Implements the core backend system logic           |
| `frontend_task`  | (Optional) Implements interaction logic/UI sketch  |
| `test_task`      | Writes tests to validate functional requirements   |

## 📁 Project Structure

.
├── config/
│ ├── agents.yaml # Agent definitions
│ └── tasks.yaml # Task configurations
├── new/
│ └── crew.py # CrewBase implementation
├── output/ # Output folder for generated code
├── main.py # Entrypoint for the project
└── README.md # This file


## 🧠 Inputs

The `main.py` file initializes the system with:
- Natural language `requirements`
- A `module_name` (`accounts.py`)
- A `class_name` (`Account`)

These are passed as inputs to the CrewAI agents to begin collaborative development.


