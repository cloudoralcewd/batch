python --version
python -m venv myenv

myenv\Scripts\activate
pip install requests
pip install -r requirements.txt
pip freeze > requirements.txt

deactivate