📄 CSV Data Cleaning Tool

A **Streamlit-based web app** for uploading, cleaning, and merging CSV files. Designed for data analysts, engineers, and anyone who wants to quickly preprocess CSV datasets without coding.

**Live Demo:** [Streamlit Cloud link]


---

## 🚀 Features

* ✅ Upload one or multiple CSV files
* ✅ Merge multiple CSV files safely
* ✅ Keep only the header from the first file
* ✅ Remove duplicate rows
* ✅ Remove empty rows
* ✅ Download cleaned CSV files
* ✅ Interactive data preview
* ✅ Easy deployment via Docker

---

## 💻 Installation & Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/abioludipe/Data-Cleaning-tool.git
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

4. Open the app in your browser (usually `http://localhost:8501`).

---

## 🧹 Usage Instructions

1. **Upload CSV files**

   * Click *Choose CSV files*
   * Select one or multiple files

2. **Merge Files** (optional)

   * Tick *Merge uploaded CSV files*
   * Choose whether to keep only the first file’s header
   * Optionally remove duplicates or empty rows

3. **Preview DataFrames** (optional)

   * Tick *Show DataFrames* to see uploaded/merged data

4. **Download Cleaned CSV**

   * Click the *Download cleaned data* button
   * Each file will be downloaded as `cleaned_data_1.csv`, etc.

---

## ⚙️ Configuration Options

| Option                 | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| Keep first header only | Keep only the column headers from the first uploaded CSV             |
| Remove duplicate rows  | Remove duplicate rows after merging                                  |
| Remove empty rows      | Remove fully empty rows                                              |
| End line               | Choose line ending format (`\n` for Linux/macOS, `\r\n` for Windows) |

---

## 🐳 Docker Deployment

To run using Docker:

1. Build the Docker image:

```bash
docker build -t data-cleaning-tool .
```

2. Run the container:

```bash
docker run -p 8501:8501 data-cleaning-tool
```

3. Open in browser: `http://localhost:8501`

---

## 🌐 Deployment


* **Docker**: Portable and scalable deployment anywhere

---

## 📁 Project Structure

```
csv-data-cleaning-tool/
│
├── app.py   # Main Streamlit app
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── Dockerfile              # Optional: Docker deployment
```

---

## 👤 Author

* GitHub: [Abioludipe](https://github.com/abioludipe)

---

## 💡 Notes / Tips

* For large CSV files (>10MB), consider splitting files or upgrading hosting plan on HuggingFace/Streamlit Cloud.
* Always preview data before downloading to avoid missing columns or misaligned merges.
* This app is beginner-friendly and ideal for portfolio demonstrations.
