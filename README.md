Captum: Google Image Downloader
Captum is a Flask-based web application that allows users to download images from Google Images based on a search query. This README provides instructions on how to set up and run the application.

Table of Contents
Installation
Usage
File Structure
Contributing
License
Installation
To run Captum locally, follow these steps:

Prerequisites
Ensure you have the following installed:

Python 3.6 or higher
pip (Python package installer)
Google Chrome browser
Step-by-Step Guide
Clone the Repository

bash
Code kopiëren
git clone https://github.com/your-username/Captum.git
cd Captum
Create a Virtual Environment

bash
Code kopiëren
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the Required Libraries

bash
Code kopiëren
pip install -r requirements.txt
Install ChromeDriver

ChromeDriver must be compatible with your Chrome browser version. Captum uses webdriver-manager to handle this.
bash
Code kopiëren
pip install webdriver-manager
Requirements File
Ensure the requirements.txt file contains the following:

Code kopiëren
Flask
beautifulsoup4
requests
selenium
Pillow
webdriver-manager
Usage
Start the Flask Application

bash
Code kopiëren
python app.py
Access the Web Interface
Open your web browser and navigate to http://127.0.0.1:5000.

Download Images

Enter your search query and the number of images you want to download.
Click the "Download" button.
The images will be downloaded into a uniquely named folder based on your query.
Tips for Best Use
Ensure you have a stable internet connection for downloading images.
The application will create a new folder if a folder with the same name already exists.
The Chrome browser window will open during the process. It is normal and required for Selenium to interact with the Google Images page.
File Structure
arduino
Code kopiëren
Captum/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── (static files if any)
├── requirements.txt
└── README.md
app.py: Main application file containing the Flask app and the image downloading logic.
templates/index.html: HTML template for the web interface.
requirements.txt: List of required Python packages.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please create an issue or submit a pull request.

Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature-branch)
Create a new Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.
