### Install
```
pip install -r requirements.txt
playwright install
```

### ▶️ Normal Run
```
pytest
```
### ⚡ Parallel Execution
```
pytest -n 3
```
### 📊 Allure Report 
```
allure serve reports/allure-results
```

### Playwright + PyTest framework with:
✅ Page Object Model  
✅ Data-driven testing (CSV)  
✅ Allure reporting  
✅ Parallel execution (xdist)  
✅ Integrate with Jenkins

# Project Structure

```
playwright_pytest_project
│
├── tests
│   └── test_example.py
│
├── pages
│   └── login_page.py
│
├── utils
│   └── helpers.py
│
├── reports
│
├── conftest.py
├── pytest.ini
└── requirements.txt
```

We’ll make a clean Playwright + Pytest framework structure using:
- tests/  → where test scripts go
- pages/  → for Page Object Model (optional but useful)
- conftest.py  → for setting up browser fixtures
- pytest.ini  → for config
- utils/  → for helpers (if needed)
- Reports/screenshots/logs (auto-generated)

## Integrate With Jenkins  
#### FreeStyle Job
**1️⃣ Create Jenkins Job**  
**2️⃣ Connect GitHub Repo**  
  Source Code Management:    
  Select Git   
  Add your repo URL  
**3️⃣ Build Steps**   
  Add Execute Windows batch command  
  ```
  # Create virtual environment
python -m venv venv

# Activate venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install playwright browsers
playwright install

# Run tests in parallel
pytest -n 2 --alluredir=reports/allure-results
```
**4️⃣ Post-build action:**  
  Select Allure Report   
  Path: ```reports/allure-results```  
**5️⃣ Run Job**  
  Click Build Now    
  
#### Pipeline
```
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'YOUR_REPO_URL'
            }
        }

        stage('Setup') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                pip install -r requirements.txt
                playwright install
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pytest -n 2 --alluredir=reports/allure-results
                '''
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'reports/allure-results']]
            ])
        }
    }
}
```
