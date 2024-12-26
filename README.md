# Image Sonification Tool

## **Overview**
This project provides a tool to convert astronomical images into sound using two sonification modes: 
1. **Brightness-based pitch modulation**
2. **Color-based sound effects**

Users can upload an `.npy` file (representing image data), process it to extract relevant pixel data, and generate corresponding sound files.

---

## **Features**
- Converts image data from `.npy` files into CSV for processing.
- Two modes of sonification:
  - Brightness Mode: Maps pixel brightness to pitch.
  - Color Mode: Maps RGB values to sound properties.
- Downsampling options for large images to reduce file sizes.
- Simple CLI for ease of use.

---

## **Installation**

### **Dependencies**
Ensure you have Python 3.9+ installed. Install the required packages:

```bash
pip install -r requirements.txt
