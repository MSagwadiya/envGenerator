#!/usr/bin/env python3

import os

env_all = os.environ
output_file = os.getenv("INPUT_FILE_PATH")

def main():
    if not output_file:
      print("Error: Environment variable 'file_path' is not set.")
      return
    else:
      for key, value in env_all.items():
        with open(output_file, "a") as f:
          f.write(f"{key}={value}\n")
      print(f"Environment variables written to {output_file}")


if __name__ == "__main__":
    main()