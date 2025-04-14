# Expense Tracker – Single Page Web Application

This project is a **single page web application** built with [Django](https://www.djangoproject.com/) that helps users track their household finances.

![Screenshot of the Application](screenshot_of_the_app.png "Screenshot")


## Features

- **Expense & Income Management:**  
  - **Expenses:** Add, view, and delete expense entries with details like name, amount, category, and date.  
  - **Incomes:** Add, view, and delete income entries with details such as source, amount, and date.

- **Analytics Dashboard:**  
  Displays key metrics including:  
  - **Net Savings:** Total Income minus Total Expenses.  
  - **Total Income / Total Expenses:** Overall amounts aggregated from all records.  
  - **Savings Rate:** Calculated as a percentage of income that remains after expenses.  
  - **Expense Breakdown by Category:** Summary of spending per expense category.  
  - **Top Expenses:** A list of the highest expense entries to help identify cost drivers.

- **Single Page Experience:**  
  The entire application is rendered on a single page for a smooth user experience without multiple redirects or page reloads (except when the data is updated).

## Technology Stack

- **Backend:** Python, Django  
- **Database:** SQLite (or any other Django-supported database)  
- **Frontend:** HTML, CSS (Bootstrap), and JavaScript  

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   # or on Windows:
   venv\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run database migrations:**
   ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Start the development server:**
   ```bash
   python manage.py runserver

# Usage

## Adding Expenses:
Click the **"Add Expense"** button within the Expenses section to toggle the inline expense form. Fill out the form and submit it. The new expense will appear in the expenses list.
## Adding Incomes:
Similarly, click the **"Add Income"** button within the Incomes section to reveal the inline income form. Submit the form to update the incomes list.
## Analytics:
The analytics section (always visible below the expense and income lists) shows:
- Net Savings (Total Income minus Total Expenses)
- Total Income
- Total Expenses
- Savings Rate
- Expense Breakdown by Category
- Top Expenses




