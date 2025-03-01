Stopwatch Application - Installation Guide  

This document provides step-by-step instructions to install and set up the Stopwatch application on your system.  

Prerequisites  
Before running the application, ensure that you have the following installed:  
- Python 3.8 or higher  
- pip (Python package manager)  
- Git (if you are cloning from GitHub)  

Step 1: Clone the Repository  
If you haven't already downloaded the project, you can clone it using Git:  

```sh
git clone https://github.com/kabilesh-c/Stopwatch-Project.git
cd Stopwatch-Project
```

Alternatively, you can download the ZIP file from GitHub and extract it manually.  

Step 2: Set Up a Virtual Environment (Recommended)  
Create and activate a virtual environment:  

```sh
python -m venv venv
venv\Scripts\activate  (Windows)
source venv/bin/activate  (macOS/Linux)
```

Step 3: Install Dependencies  
Install all required packages:  

```sh
pip install -r requirements.txt
```

If you encounter issues, ensure you are using the correct Python version:  

```sh
python --version
pip --version
```

Step 4: Run the Application  
Once the installation is complete, launch the stopwatch:  

```sh
python src/stopwatch.py
```

Troubleshooting  
If you experience issues:  
1. Ensure Python and pip are installed correctly:  
   ```sh
   python --version
   pip --version
   ```
2. Check installed dependencies:  
   ```sh
   pip list
   ```
3. Try updating pip:  
   ```sh
   python -m pip install --upgrade pip
   ```

For further assistance, open an issue on the [GitHub repository](https://github.com/kabilesh-c/Stopwatch-Project/issues).