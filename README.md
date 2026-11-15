# 💰 Personal Expense Tracker with CSV

A simple and user-friendly Python-based console application designed to manage daily expenses, organize spending by category, and track total expenditure using CSV file storage.

This project was developed as **Project 03 – Python Programming** under the InternCircle Internship Program.

## 📌 Project Overview

The Personal Expense Tracker helps users record, view, and analyze their daily expenses. It allows users to categorize expenses, filter records by category or month, and generate spending summaries.

All expense records are stored in a CSV file, ensuring that data remains available even after the application is closed or restarted.

## ✨ Features

- **Add Expenses:** Record expenses with date, category, description, and amount.
- **View All Expenses:** Display all saved expense records in a structured table.
- **Filter Expenses:** Search expenses by category or month.
- **Category-wise Summary:** Calculate total spending for each category.
- **Grand Total:** Display the total amount spent across all categories.
- **Biggest Expense:** Identify the highest individual expense.
- **Input Validation:** Validate dates and amounts and prevent negative values.
- **CSV Data Storage:** Automatically save and retrieve expense records.
- **Persistent Storage:** Retain expense data even after restarting the application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| CSV Module | Reading and writing expense records |
| Datetime Module | Date validation |
| Collections Module | Category-wise expense calculations |
| VS Code | Development environment |

## 📂 Project Structure

```text
Personal-Expense-Tracker/
│
├── main.py          # Main Python application
├── expenses.csv     # Expense data storage
└── README.md        # Project documentation
```

*Note: The application automatically creates `expenses.csv` if the file does not exist.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the Project Folder

```bash
cd Personal-Expense-Tracker
```

### 3. Run the Application

```bash
python main.py
```

### Requirements

- Python 3.10 or newer
- Visual Studio Code or any Python-supported IDE

**No external Python packages are required.** The project uses built-in Python modules.

## 🖥️ Application Menu

```text
=============================================
          PERSONAL EXPENSE TRACKER
=============================================

1. Add Expense
2. View All Expenses
3. Filter Expenses
4. Expense Summary
5. Quit

=============================================
Enter your choice (1-5):
```

## 📊 Sample Expense Data

The application stores expense records in `expenses.csv`.

| Date | Category | Description | Amount |
|---|---|---|---:|
| 2026-11-01 | Food | Lunch | 120.00 |
| 2026-11-02 | Travel | Bus | 50.00 |
| 2026-11-03 | Study | Books | 300.00 |
| 2026-11-04 | Food | Dinner | 150.00 |

### CSV Format

```csv
date,category,description,amount
2026-11-01,Food,Lunch,120.00
2026-11-02,Travel,Bus,50.00
2026-11-03,Study,Books,300.00
```

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Python file handling and CSV operations.
- Reading and writing structured data.
- Input validation using exception handling.
- Working with Python dictionaries and loops.
- Filtering and grouping records.
- Performing calculations and generating summaries.
- Developing menu-driven console applications.

## 🔮 Future Enhancements

- Graphical User Interface (GUI).
- Monthly expense visualization using charts.
- Budget planning and spending alerts.
- Export expense reports.
- Search and edit existing expense records.

## 👨‍💻 Author

**Thoufeek T**

Python Programming Intern  
InternCircle Internship Program

## 📄 License

This project is developed for educational and internship purposes.

---

**Project 03 – Personal Expense Tracker with CSV**  
*Developed using Python | InternCircle Python Programming Internship*
