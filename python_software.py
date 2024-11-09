import cv2
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import os

class PDFGenerator:
    def __init__(self, title):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(200, 10, txt=title, ln=True, align='C')

    def add_text(self, text):
        self.pdf.multi_cell(0, 10, txt=text)

    def save(self, filename):
        self.pdf.output(filename)

def extract_video_content(video_path):
    content = []
    cap = cv2.VideoCapture(video_path)

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return content

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    for i in range(length):
        ret, frame = cap.read()
        if ret:
            # Here you could potentially add processing logic for each frame
            content.append(f"Frame {i+1} extracted and processed.")
        else:
            break

    cap.release()
    return content

def scrape_website(url):
    content = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        # Collecting paragraphs as an example
        for p in soup.find_all('p'):
            content.append(p.get_text())
    except requests.RequestException as e:
        print(f"Error while scraping website: {e}")
    return content

def main():
    video_path = 'path_to_your_video.mp4'  # Substitute with the path to your video
    url = 'http://example.com'  # Substitute with the target URL for scraping

    # Generate content from video
    video_content = extract_video_content(video_path)

    # Scrape content from a website
    website_content = scrape_website(url)

    # Setup PDF generation
    pdf = PDFGenerator(title="Extracted Content")

    # Add content from video to PDF
    pdf.add_text("Video Content:")
    for item in video_content:
        pdf.add_text(item)

    # Add content from website to PDF
    pdf.add_text("\nWeb Scraped Content:")
    for item in website_content:
        pdf.add_text(item)

    # Save PDF file
    pdf.save("Extracted_Content.pdf")
    print("PDF generated successfully!")

if __name__ == '__main__':
    main()