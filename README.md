# Aviation MCQ Web Application

A full-stack, purely frontend React application designed for easy deployment to Netlify.

## Features
- **Subject Navigation**: 8 subjects with card-based UI.
- **Interactive Questions**: Next/Prev navigation, green highlights for correct answers, red for incorrect.
- **Search & Jump**: Search questions by keyword or jump to a specific question number.
- **Shuffle**: Randomize the order of questions.
- **Modern UI**: Responsive, glassmorphism design with sleek animations.

## How to Run Locally

1. Make sure you have Node.js installed.
2. Open a terminal in this directory (`mcq-app`).
3. Run `npm install` to install dependencies.
4. Run `npm run dev` to start the development server.

## How to Deploy to Netlify (Fastest Method)

Since this project uses static JSON data instead of a backend, it's incredibly easy to host on Netlify for free.

1. Open your terminal in this directory (`mcq-app`).
2. Run `npm run build`. This will create a `dist` folder containing the optimized production files.
3. Go to [Netlify Drop](https://app.netlify.com/drop).
4. Drag and drop the `dist` folder into the Netlify Drop area.
5. Your site will be live instantly!

## How to Extract Real Questions from PDFs

Due to the massive size of your PDFs, we have provided a Python script outside this folder named `extract_mcq.py`. 

### Prerequisites for OCR:
You will need to install the following on your machine:
- Python 3.x
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) (Add to system PATH)
- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases) (Add the `bin/` folder to your system PATH)

### Steps to Extract:
1. Open a terminal in the parent directory containing the PDFs and `extract_mcq.py`.
2. Run `pip install pdf2image pytesseract opencv-python numpy`.
3. Run `python extract_mcq.py`.
4. The script will process your PDFs and create an `extracted_questions.json` file.
5. Replace the file `mcq-app/src/data/questions.json` with your newly `extracted_questions.json`.
6. Run `npm run build` again and deploy to Netlify!
