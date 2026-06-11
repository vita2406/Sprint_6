# Sprint_6 - Автотесты для Яндекс.Самокат

## Как запустить тесты
```bash
pip install -r requirements.txt
pytest tests/ -v
pytest tests/ --alluredir=allure-results
allure serve allure-results

cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.pytest_cache/
allure-results/
allure-report/
debug_*.py
.DS_Store
