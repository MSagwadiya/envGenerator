#!/usr/bin/env python3

import os

output_file = os.environ.get("file_path")
env_vars = os.environ

def main():
    if not output_file:
      print("Error: Environment variable 'file_path' is not set.")
      return
    else:
      with open(output_file, "w") as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")

    print(f"Environment variables written to {output_file}")


if __name__ == "__main__":
    main()