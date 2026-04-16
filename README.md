# 📦 Cross-Border E-Commerce Inventory Management System

**COMP S209W / COMP 8090SEF Course Project**

This repository contains the implementation of a Cross-Border E-Commerce Inventory Management System, developed in Python. The project demonstrates the practical application of Object-Oriented Programming (OOP) principles and advanced data structures/algorithms.

## 🎥 Project Presentation Videos

* **Task 1 (OOP Architecture):** [Watch Task 1 Video Here](https://youtu.be/DgA7Kb2jUAo)
* **Task 2 (Data Structure & Algorithm):** [Watch Task 2 Video Here](https://youtu.be/Bp81om8-SfA)

---

## 🛠️ Project Structure

The system is designed with a strict modular architecture:

* `models.py`: Contains the data models (`Product` base class, `ElectronicProduct`, `OutdoorProduct`) implementing Abstraction, Inheritance, and Encapsulation.
* `algorithms.py`: Contains the custom `Trie` (Prefix Tree) for $O(M)$ SKU searching and `Heap Sort` for $O(N \log N)$ inventory sorting.
* `manager.py`: Handles the core business logic and inventory management.
* `main.py`: The entry point providing the interactive terminal user interface.

## 🚀 How to Run

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository to your local machine.
3. Open your terminal or command prompt.
4. Navigate to the project directory.
5. Run the following command:
   ```bash
   python main.py