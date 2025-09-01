# 📊 Sales Dashboard (SQL + Streamlit)

An interactive **Sales Dashboard** built with **Streamlit** and **SQLite** to visualize and analyze sales data.  
This project helps explore sales by category, revenue, and more with a simple and clean UI.

---

## 🚀 Features
- Load data directly from an **SQLite database**.
- Interactive **category filter** to view sales by product category.
- Display all sales data in a table.
- Future-ready: add charts, KPIs, and filters.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Streamlit** – for building interactive dashboards.
- **Pandas** – for data manipulation.
- **SQLite** – for storing and querying sales data.

---

## 📂 Project Structure
📦 Sales-analysis-project
┣ 📜 sales.db # SQLite database file
┣ 📜 app.py # Main Streamlit app
┣ 📜 README.md # Project documentation
┗ 📜 requirements.txt # Dependencies

## ▶️ How to Run the Project

1. **Clone the repository**  
   ```bash
   git clone https://github.com/dalinaveen/Sales-analysis-project.git
   cd Sales-analysis-project

python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate   # On Mac/Linux
pip install -r requirements.txt

streamlit run app.py
