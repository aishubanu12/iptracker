import tkinter as tk
import requests
import ipaddress
from tkintermapview import TkinterMapView

def ipFinder(outputMsg, inputValue, map_widget):
    try:
        # Get the IP address from the input field
        ipAddress = inputValue.get().strip()
        ipaddress.ip_address(ipAddress)  # Validate the IP address

        # API request to get IP information
        response = requests.get(f'https://ipapi.co/{ipAddress}/json/').json()

        # Extract required fields with fallback values
        ip_version = response.get("version", "N/A")
        city = response.get("city", "N/A")
        region = response.get("region", "N/A")
        country = response.get("country_name", "N/A")
        postalcode = response.get("postal", "N/A")
        continent = response.get("continent_code", "N/A")
        latitude = response.get("latitude", "N/A")
        longitude = response.get("longitude", "N/A")
        org = response.get("org", "N/A")

        # Update the output message
        outputMsg.config(
            text=f"Information for {ipAddress}:\n"
                 f"<---------------->\n"
                 f"IP Version: {ip_version}\n"
                 f"City: {city}\n"
                 f"Region: {region}\n"
                 f"Country: {country}\n"
                 f"Postal Code: {postalcode}\n"
                 f"Continent: {continent}\n"
                 f"Latitude: {latitude}\n"
                 f"Longitude: {longitude}\n"
                 f"Organization: {org}\n"
                 f"<---------------->"
        )

        # Update the map widget if latitude and longitude are valid
        if latitude != "N/A" and longitude != "N/A":
            map_widget.set_position(float(latitude), float(longitude))
            map_widget.set_marker(float(latitude), float(longitude), text=city)
        else:
            outputMsg.config(text="Valid IP, but no location data found.")
    except ValueError:
        outputMsg.config(text="Please Enter a Valid IP Address")
    except requests.exceptions.RequestException as e:
        outputMsg.config(text=f"Error fetching data from API: {e}")
    except Exception as e:
        outputMsg.config(text=f"Unexpected error: {e}")

def clearFields(inputEntry, outputMsg, map_widget):
    inputEntry.delete(0, tk.END)
    outputMsg.config(text="")
    map_widget.set_position(22.3511148, 78.6677428)  # Default position (center of India)
    map_widget.delete_all_marker()

# Main Tkinter Window
root = tk.Tk()
root.geometry("800x600")
root.title("Indian IP Address Tracker with Map")
root.configure(background="#28334A")

# Input Field
inputString = tk.StringVar()
ipLabel = tk.Label(root, text="Enter IP:", background="#28334A", foreground="#F65058", font=("Arial", 12))
ipLabel.grid(row=0, column=0, padx=10, pady=10, sticky="e")

inputEntry = tk.Entry(root, textvariable=inputString, width=30, font=("Arial", 12))
inputEntry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Output Message
outputMsg = tk.Label(root, text="", background="#28334A", foreground="white", justify="left", anchor="w", wraplength=400, font=("Arial", 10))
outputMsg.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

# Map Widget
map_widget = TkinterMapView(root, width=600, height=400, corner_radius=10)
map_widget.grid(row=1, column=2, rowspan=4, padx=10, pady=10, sticky="nsew")
map_widget.set_position(22.3511148, 78.6677428)  # Default position (center of India)

# Buttons
checkButton = tk.Button(root, text="Check IP", command=lambda: ipFinder(outputMsg, inputString, map_widget), font=("Arial", 12), bg="#4CAF50", fg="white")
checkButton.grid(row=2, column=0, padx=10, pady=10, sticky="w")

clearButton = tk.Button(root, text="Clear", command=lambda: clearFields(inputEntry, outputMsg, map_widget), font=("Arial", 12), bg="#F44336", fg="white")
clearButton.grid(row=2, column=1, padx=10, pady=10, sticky="e")

# Configure Grid
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Start the Tkinter loop
root.mainloop()







