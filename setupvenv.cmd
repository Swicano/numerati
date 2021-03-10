if not exist numer_dev_env\Scripts\activate.bat (
  py.exe -m venv numer_dev_env
)
call numer_dev_env\Scripts\activate.bat
pip.exe install -r requirements.txt
cmd /k