# 🧪 Selenium Python Automation

This project uses **Selenium WebDriver** with **Python** to automate web browser interactions for testing or data scraping purposes.

## 📁 Project Structure

```

selenium-python-project/
│
├── drivers/                  # Browser drivers (e.g., chromedriver)
├── tests/                    # Test scripts
│   └── test\_login.py         # Example test file
├── pages/                    # Page Object Models
│   └── login\_page.py
├── screenshots/              # Captured screenshots on test failure
├── utils/                    # Helper functions/utilities
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

````

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Google Chrome (or any other supported browser)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (or equivalent driver)

---

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/selenium-python-project.git
cd selenium-python-project

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

---

## 🧪 Running Tests

To run a sample test:

```bash
python tests/test_login.py
```

You can also use a test runner like `pytest`:

```bash
pytest tests/ --html=report.html
```

---

## ✅ Features

* ✅ Page Object Model (POM) structure
* ✅ Test reporting with `pytest-html`
* ✅ Screenshot capture on failure
* ✅ Custom logging and wait utilities

---

## 🛠️ Technologies Used

* [Selenium WebDriver](https://www.selenium.dev/)
* Python 3.x
* `pytest`
* `webdriver-manager` (optional for automatic driver handling)

---

## 📸 Screenshots

Screenshots of failed tests are saved in the `/screenshots/` directory automatically.

---

## 📄 License

This project is open-source under the MIT License.

---

## 🙋‍♂️ Author

Developed by **Baskaran**
📧 [baskarbala5185@gmail.com](baskarbala5185@gmail.com)
🌐 [https://github.com/BASKARAN5185](https://github.com/BASKARAN5185)
