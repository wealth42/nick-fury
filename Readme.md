# Readme

1. Copy all the files to the local machine in any folder.
2. In that folder, use the following command to create a virtual environment based on your current interpreter: 
   * For macOS/Linux- 
     * sudo apt-get install python3-venv    #If needed
	 * python3 -m venv env
   * For Windows-
     * python -m venv env

3. Open the project folder in VS Code by running code ., or by running VS Code and using the **File > Open Folder command**.
4. In VS Code, open the Command Palette (View > Command Palette or (Ctrl+Shift+P)). Then select the **Python: Select Interpreter** command.
5. From the list, select the virtual environment in your project folder that starts with **./env** or **.\env**.
6. Run **Terminal: Create New Integrated Terminal (Ctrl+Shift+`)** from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.
7. Install **Django** in the virtual environment by running one of the following commands in the VS Code Terminal:
   * python -m pip install django
8. type **python manage.py runserver** in the terminal to run the server on your local computer.