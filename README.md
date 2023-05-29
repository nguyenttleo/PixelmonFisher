# PixelmonFisher: Automated Fishing in Pixelmon Minecraft

PixelmonFisher is a program designed to automate the process of fishing in Pixelmon, a popular Minecraft mod that adds Pokémon-themed elements to the game. With PixelmonFisher, you can sit back and let the program handle the repetitive task of fishing, saving you time and effort.

## Project Overview

The PixelmonFisher project consists of the following files:

- `collect.png`: This image file is used by the program to identify the "collect" button in the fishing GUI.
- `fished.png`: This image file is used by the program to determine whether the fishing process has completed successfully.
- `main.py`: This file contains all the functions and automation logic required for the PixelmonFisher program. It includes the GUI for the menu and handles the fishing automation.
- `maxTimer.txt`: This text file stores the maximum time (in seconds) that the user is willing to wait for a fish before the program stops.
- `run.png`: This image file is used to identify the "run" button in the fishing GUI, initiating the fishing process.
- `stopMessage.png`: This image file is used to identify the "stop message" that appears when the fishing process is interrupted.

## How to Use PixelmonFisher

To use PixelmonFisher and automate fishing in Pixelmon, follow these steps:

1. Install the required dependencies:

   - Python: Make sure you have Python installed on your computer. You can download it from the official Python website (https://www.python.org).

2. Clone or download the PixelmonFisher repository:

   - If you have Git installed, you can clone the repository using the following command:

     ```bash
     git clone https://github.com/nguyenttleo/PixelmonFisher.git
     ```

   - Alternatively, you can download the repository as a ZIP file and extract it to a local directory.

3. Prepare the environment:

   - Open a terminal or command prompt and navigate to the project directory.

   - Install the necessary Python dependencies by running the following command:

     ```bash
     pip install -r requirements.txt
     ```

4. Customize the settings:

   - Open the `main.py` file in a text editor.

   - Modify the `max_timer` variable in the file to set the maximum time (in seconds) you are willing to wait for a fish. This value is read from the `maxTimer.txt` file.

5. Compile the code into an executable (optional):

   - If you want to distribute the program as an executable file, you can use tools like PyInstaller, py2exe, or py2app to package the Python code into a standalone executable.

6. Run the program:

   - In the terminal or command prompt, navigate to the project directory.

   - Run the following command to start the PixelmonFisher program:

     ```bash
     python main.py
     ```

7. Follow the on-screen instructions:

   - The program will display a menu with options to start and stop the fishing automation.

   - Use the provided PNG files (`collect.png`, `fished.png`, `run.png`, `stopMessage.png`) to guide the program to the correct buttons in the Pixelmon fishing GUI.

   - The program will automatically fish in Pixelmon based on your settings until a fish is caught or the maximum time limit is reached.

   - You can stop the fishing process by clicking the "Stop Fishing" option in the program menu or by using the provided `stopMessage.png` image to automatically detect the stop message.

8. Enjoy automated fishing in Pixelmon Minecraft with PixelmonFisher!

## Compiling the Code into an Executable

To compile the PixelmonFisher code into an executable file, you can use tools like PyInstaller, py2exe, or py2app. These tools allow you to package the Python code along with its dependencies into a standalone executable that can be run on different systems without the need for Python installation.

Here is a general overview of the compilation process using PyInstaller:

1. Install PyInstaller:

   - Open a terminal or command prompt and run the following command:

     ```bash
     pip install pyinstaller
     ```

2. Compile the code:

   - In the terminal, navigate to the project directory containing `main.py` and the other required files.

   - Run the following command to compile the code into an executable:

     ```bash
     pyinstaller main.py --onefile
     ```

   - PyInstaller will analyze the code, resolve dependencies, and create a standalone executable file in the `dist` directory.

3. Distribute the executable:

   - The compiled executable file can be found in the `dist` directory.

   - Copy the executable file (`main.exe` on Windows or `main` on Linux/macOS) to the desired location or distribute it to others.

   - Users can run the executable without needing to install Python or the project dependencies.

Please refer to the documentation of the specific compilation tool you choose for more detailed instructions on how to compile the code into an executable.

Now you can enjoy automated fishing in Pixelmon Minecraft with the convenience of PixelmonFisher! Happy fishing!
