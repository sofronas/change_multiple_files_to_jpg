import os

print("Renaming process started.")

# Step 1: Specify the directory
directory = r'C:\Users\ksofronas\Desktop\Avatars'  # Use a raw string to avoid issues with backslashes

# Step 2: Loop through the files
for filename in os.listdir(directory):
    # Check if it's a file
    if os.path.isfile(os.path.join(directory, filename)):
        # Create a new filename with .jpg extension
        new_filename = os.path.splitext(filename)[0] + '.jpg'  # Change the extension to .jpg
        
        # Use try-except to catch potential errors
        try:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed: {filename} to {new_filename}")
        except FileExistsError:
            print(f"Error: {new_filename} already exists. Skipping rename for {filename}.")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

print("Renaming process completed.")
