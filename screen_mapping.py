import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def scrape_website_with_buttons(url, output_csv="elements_info.csv"):
    """
    Scrapes a website for all visible elements (buttons, inputs, links, divs, menus, etc.),
    along with their text/placeholder/alt attributes, position, and size.
    Also saves the full HTML and visible text content.
    """
    # Setup headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(2)  # wait for content to load

        # Save full HTML content
        with open("full_html_content.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        # Save visible text content
        with open("visible_text_content.txt", "w", encoding="utf-8") as f:
            f.write(driver.find_element(By.TAG_NAME, "body").text)

        # Find all elements on the page
        all_elements = driver.find_elements(By.XPATH, "//*")

        # Write element data to CSV
        with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Tag", "Text/Placeholder/Alt", "X Position", "Y Position", "Width", "Height"])

            for el in all_elements:
                try:
                    # Skip invisible elements
                    if not el.is_displayed():
                        continue

                    location = el.location
                    size = el.size

                    # Skip elements with no size
                    if size['width'] == 0 or size['height'] == 0:
                        continue

                    # Get meaningful text or attribute
                    label = el.text.strip() or el.get_attribute("placeholder") or el.get_attribute("alt") or "[No text]"

                    writer.writerow([
                        el.tag_name,
                        label,
                        location['x'],
                        location['y'],
                        size['width'],
                        size['height']
                    ])
                except Exception as e:
                    writer.writerow([el.tag_name, f"Error: {e}", "", "", "", ""])

        print(f" All visible element positions saved to {output_csv}")
        print(" Full HTML saved to full_html_content.html")
        print(" Visible text saved to visible_text_content.txt")

    finally:
        driver.quit()


# Example usage:
# scrape_website_with_buttons("https://www.dominos.co.in/")
