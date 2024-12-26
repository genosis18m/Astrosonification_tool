### **Image Sonification Tool: User Guide**

---

#### **Overview**
This guide explains how to use the Image Sonification Tool, from setting up the environment to running the tool and understanding the outputs. Follow the instructions step-by-step to ensure smooth execution.

---

### **Project Structure**
Your project directory should look like this:
```
Tool./
│
├── main.py                  # Main script for running the tool
├── requirements.txt         # Python dependencies
├── README.md                # User guide (detailed instructions)
├── images.npy               # Your .npy file (optional)
├── output/                  # Output directory for generated files
│   ├── data.csv             # Generated CSV file (example)
│   ├── sound.wav            # Generated sound file (example)
│
├── utils/                   # Utility scripts
│   ├── image_utils.py          # incase of jpeg/png file
│   ├── data_to_csv.py       # Script to convert .npy to CSV
│   ├── sonification.py      # Script for sonifying CSV data
│
└── report.pdf               # Final report summarizing the project
```

---

### **Setup Instructions**

1. **Clone the Repository**
   If you have the repository URL:
   ```bash
   git clone <repository_url>
   cd Week_5
   ```

2. **Install Dependencies**
   Ensure Python 3.9+ is installed on your system. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up FFmpeg**
   - Download FFmpeg from [FFmpeg.org](https://ffmpeg.org/).
   - Extract the files to a folder (e.g., `C:\ffmpeg`).
   - Add the `bin` folder path (e.g., `C:\ffmpeg\bin`) to your system's PATH environment variable.

4. **Check the Setup**
   Confirm that Python and FFmpeg are correctly installed:
   ```bash
   python --version
   ffmpeg -version
   ```

---

### **Usage Instructions**

#### **Run the Tool**
Use the command-line interface (CLI) to run the tool. The basic command structure is:

```bash
python main.py --file <path_to_npy_file> --mode <brightness|color> --output_dir <output_directory> [--downsample_factor <value>] [--max_pixels <value>]
```

#### **Arguments**
| Argument            | Description                                                 | Example Value              |
|---------------------|-------------------------------------------------------------|----------------------------|
| `--file`            | Path to the `.npy` file containing image data.              | `images.npy`               |
| `--mode`            | Sonification mode (`brightness` or `color`).                | `brightness`               |
| `--output_dir`      | Directory to save output files.                             | `output`                   |
| `--downsample_factor` (optional) | Factor by which to downsample the image.         | `20`                       |
| `--max_pixels` (optional) | Maximum number of pixels to process.                       | `5000`                     |

#### **Example Commands**
- Generate sound using brightness mode:
  ```bash
  python main.py --file <your .npy file> --mode brightness --output_dir output
  ```
- Downsample image data and set max pixels: (when .npy file is big) //recommended
  ```bash
  python main.py --file <your .npy file> --mode color --output_dir output --downsample_factor 20 --max_pixels 5000
  ```

---

### **Expected Outputs**
After running the tool:
1. **CSV File**
   - Located in the output directory (`output/data.csv`).
   - Contains the downsampled and flattened pixel data.

2. **Sound File**
   - Located in the output directory (`output/sound.wav`).
   - Represents the sonification of the image.

---

### **Sample Run Explanation**

#### **Step-by-Step Execution**
1. Run the command:
   ```bash
   python main.py --file images.npy --mode brightness --output_dir output --downsample_factor 20 --max_pixels 5000
   ```
2. The tool will:
   - Load the `.npy` file.
   - Convert image data to a downsampled CSV file.
   - Use the selected mode (`brightness` or `color`) to map pixel data to sound properties.
   - Save the sound file in the specified output directory.

3. Check the `output` folder for:
   - `data.csv`: CSV representation of processed image data.
   - `sound.wav`: Sonified sound output.

---

### **Common Issues and Solutions**

1. **Error: FFmpeg Not Found**
   - Ensure FFmpeg's `bin` directory is added to your PATH variable.
   - Restart your terminal after making changes.

2. **Large File Sizes**
   - Use the `--downsample_factor` or `--max_pixels` arguments to reduce image size.

3. **Incompatible Python Version**
   - Ensure Python 3.9+ is installed.

---

### **Final Notes**
With this tool, users can transform `.npy` image data into sound, providing a unique way to interpret astronomical data. Customize the parameters for experimentation and refine the tool as needed.


