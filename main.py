import argparse
from utils.data_to_csv import npy_to_csv
from utils.sonification import sonify_data

def main():
    parser = argparse.ArgumentParser(description="Image Sonification Tool")
    parser.add_argument("--file", required=True, help="Path to the .npy file")
    parser.add_argument("--mode", choices=["brightness", "color"], default="brightness", help="Sonification mode")
    parser.add_argument("--output_dir", required=True, help="Directory to save outputs")
    parser.add_argument("--downsample_factor", type=int, default=10, help="Factor to downsample the data")
    parser.add_argument("--max_pixels", type=int, default=10000, help="Maximum number of pixels to process")

    args = parser.parse_args()

    # Paths for output files
    csv_path = f"{args.output_dir}/data.csv"
    sound_path = f"{args.output_dir}/sound.wav"

    # Convert npy to csv
    npy_to_csv(args.file, csv_path, downsample_factor=args.downsample_factor)

    # Sonify the CSV
    sonify_data(csv_path, sound_path, mode=args.mode, max_pixels=args.max_pixels)

if __name__ == "__main__":
    main()
