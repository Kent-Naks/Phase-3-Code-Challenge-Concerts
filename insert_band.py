import sqlite3

def insert_band(name, genre, hometown):
    # Connect to the SQLite database
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Insert the band into the bands table
    cursor.execute("INSERT INTO bands (name, genre, hometown) VALUES (?, ?, ?)", (name, genre, hometown))
    
    # Commit the transaction and close the connection
    connection.commit()
    connection.close()
    print(f"Band '{name}' with genre '{genre}' from '{hometown}' has been added successfully.")

if __name__ == "__main__":
    # Get band details from the user
    band_name = input("Enter band name: ")
    band_genre = input("Enter band genre: ")
    band_hometown = input("Enter band hometown: ")  # New prompt for hometown

    insert_band(band_name, band_genre, band_hometown)
