from flask import Flask, request, render_template
import os
import time
import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

def create_unique_folder_name(base_name):
    """
    Create a unique folder name by appending a counter if the folder already exists.
    """
    folder_name = base_name
    counter = 1
    while os.path.exists(folder_name):
        folder_name = f"{base_name}({counter})"
        counter += 1
    os.makedirs(folder_name)
    return folder_name

def scroll_and_retrieve_html(query, num_images, driver):
    """
    Scroll through Google Image search results and return the HTML source.
    """
    search_url = f"https://www.google.com/search?q={query}&tbm=isch"
    driver.get(search_url)
    driver.maximize_window()

    try:
        possible_texts = ["Alles afwijzen", "Reject all"]
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if any(text in button.text for text in possible_texts):
                button.click()
                break
    except Exception as e:
        print(f"Cookie banner not found nor clicked: {e}")

    last_height = driver.execute_script("return document.body.scrollHeight")
    image_count = 0

    while image_count < num_images:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the page to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.rg_i")
        image_count = len(thumbnails)

    return driver.page_source

def extract_image_urls(html_source, num_images):
    """ 
    Extract image URLs from the HTML source.
    """
    soup = BeautifulSoup(html_source, "html.parser")
    image_urls = []
    for count, img in enumerate(soup.find_all("img", {"src": re.compile(r"^https?://")})):
        if count >= 2:  # Skip the first two images
            if len(image_urls) >= num_images:
                break
            image_urls.append(img["src"])
    return image_urls

def is_valid_image(url, min_width=100, min_height=100):
    """
    Check if an image is valid based on its dimensions.
    """
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        return width >= min_width and height >= min_height
    except Exception as e:
        print(f"Error checking image {url}: {e}")
        return False

def download_images(image_urls, folder_name, query):
    """
    Download images to the specified folder.
    """
    folder_name = create_unique_folder_name(folder_name)
    downloaded_urls = []
    valid_image_count = 0
    for url in image_urls:
        if is_valid_image(url):
            try:
                response = requests.get(url)
                file_path = os.path.join(folder_name, f"{folder_name}_{valid_image_count + 1}.jpg")
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    downloaded_urls.append(url)
                valid_image_count += 1
            except Exception as e:
                print(f"Error downloading {url}: {e}")
    return downloaded_urls

def main(query, num_images):
    """
    Main function to run the image scraping process.
    """
    options = Options()
    options.headless = False  # Set to True if you don't want to see the browser window
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    folder_name = query.split()[0] if query.split() else "images"

    try:
        html_source = scroll_and_retrieve_html(query, num_images, driver)
        image_urls = extract_image_urls(html_source, num_images)
        downloaded_urls = download_images(image_urls, folder_name, query)
        print(f"{len(downloaded_urls)} images downloaded in '{folder_name}'.")
    finally:
        driver.quit()

    return downloaded_urls

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Handle GET and POST requests for the home page.
    """
    if request.method == 'POST':
        query = request.form.get('query')
        num_images = int(request.form.get('num_images'))
        image_urls = main(query, num_images)
        num_downloaded_images = len(image_urls)
        return render_template("index.html", image_urls=image_urls, num_downloaded_images=num_downloaded_images)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
