# 💰 Python Personal Expense Manager (GUI)

A professional **Personal Expense Manager** built using Python and Tkinter.

This desktop application allows you to track expenses, manage categories, search records instantly, and visualize spending through charts. All data is stored permanently in a local JSON file and loads automatically on startup.

The program uses only Python standard libraries plus matplotlib.

---

## ✨ Features

✅ Clean graphical interface using Tkinter  
✅ Add, edit, delete expenses safely  
✅ Scrollable multi-column expense list  
✅ Live search filter while typing  
✅ Automatic JSON data persistence  
✅ Auto-load saved expenses at startup  
✅ Immediate save after every change  

### Each Expense Stores
- Amount (positive numeric value)
- Category
- Date
- Optional note

---

## 📊 Analytics Panel

The dashboard shows:

- Total spending  
- Spending this month  
- Highest spending category  

---

## 📈 Visualization Window

Press **Show Analytics** to open charts:

- Bar chart of spending by category  
- Monthly spending chart  

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|--------|--------|
| Enter | Add expense |
| Delete | Delete selected expense |
| Ctrl + F | Focus search box |

---

## 🖥️ Requirements

- Python 3.x
- matplotlib

Install matplotlib with:

pip install matplotlib

---

## ▶️ How To Run

1. Download the project  
2. Open terminal in the project folder  
3. Run:

python expense_manager.py

---

## 📂 Data Storage

All expenses are saved in:

expenses.json

The file is created automatically if it does not exist.

---

## 🛡️ Safety Features

- Prevents invalid numeric input  
- Prevents empty categories  
- Prevents crashes when nothing selected  
- Confirmation before clearing all data  
- Safe JSON loading  

---

## 👨‍💻 Developer

Created by **Ayush Prabhakar**  
GitHub: https://github.com/ayushprabhakar38  

---

## 🛠️ Support

For support, feature requests, or bug reports:

- 📧 Email: ayushprabhakar38@gmail.com  
- 🐙 GitHub: https://github.com/ayushprabhakar38  
- 🌐 Website: https://ayushprabhakharpy.vercel.app/

---

## 📜 License

This project is licensed under the **MIT License**.  
See the LICENSE file for details.

---

## 🧾 Version History

### v1.0.0
- Initial release
