#!/usr/bin/env python3

import os

output_file = os.getenv("INPUT_FILE_PATH")

def main():
    if not output_file:
      print("Error: Environment variable 'file_path' is not set.")
      return
    else:
      print(f"Environment variables written to {output_file}")


if __name__ == "__main__":
    main()