import numpy as np
import csv

def npy_to_csv(npy_file, csv_file, downsample_factor=10):
    """
    Convert an npy file to a flattened CSV file with optional downsampling.
    
    Args:
        npy_file (str): Path to the .npy file.
        csv_file (str): Path to save the .csv file.
        downsample_factor (int): Factor by which to downsample the data.
    """
    data = np.load(npy_file)
    # Downsample the data
    data = data[::downsample_factor, ::downsample_factor]
    # Flatten the data
    flattened_data = data.flatten()

    # Save to CSV
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for value in flattened_data:
            writer.writerow([value])  # Each value in its own row

    print(f"CSV file saved at: {csv_file}")
