# Captum: Google Image Downloader
Captum is a Flask-based web application that allows users to download images from Google Images based on a search query. This README provides instructions on how to set up and run the application.

<br>

## Prerequisites
Before you can run Captum, you need to ensure you have the following installed on your system:
Python 3.x
pip (Python package installer)

<br>

## Installation
To get started with Captum, follow these steps:

### Clone the repository:
Open a terminal or command prompt and clone the repository using the following command:
git clone https://github.com/teinlb/Captum.git

### Navigate to the project directory:
Change to the directory containing the cloned repository:
cd Captum

### Create a virtual environment (optional but recommended):
Create a virtual environment to keep your project dependencies isolated:
python -m venv venv

Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS and Linux:
source venv/bin/activate

### Install required libraries:
Install all the necessary Python libraries specified in the requirements.txt file:
pip install -r requirements.txt

<br>

## Dependencies
Captum relies on several Python libraries. If you don't use the requirements.txt file for installation, make sure to manually install the following libraries:

Flask
requests
BeautifulSoup4
selenium
Pillow
webdriver-manager

Install these dependencies using pip:
pip install Flask requests beautifulsoup4 selenium pillow webdriver-manager

<br>

## Running the Application

### Start the Flask server:
Run the Flask application using the following command:
python app.py

### Access the web application:
Open a web browser and go to http://127.0.0.1:5000/. You should see the Captum web interface.

<br>

## Using Captum

### Enter a search prompt and the number of images:
In the Captum web interface, enter the search prompt for the images you want to download and specify the number of images.

### Download images:
Click the "Download" button. The application will search Google Images, retrieve the URLs of the images, and download them to a folder named after your search prompt.

### View downloaded images:
After the images are downloaded, the web interface will display a message indicating the number of images downloaded and a preview of the first five images.

<br>

## Project Structure
app.py: The main Flask application file containing all the logic for image scraping and downloading.
templates/index.html: The HTML template for the web interface.

<br>

## Additional Information
Captum uses Selenium to automate the browser for retrieving images from Google Images.
The images are filtered to ensure they meet a minimum size requirement before downloading.
A unique folder is created for each search prompt to store the downloaded images.

<br>

## Troubleshooting
If you encounter any issues:

Ensure you have the latest version of Chrome installed, as Selenium uses the Chrome WebDriver.
Check that all required Python packages are installed correctly.
Verify that your internet connection is stable.

<br>

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

<br>

## License
This project is licensed under the MIT License.
