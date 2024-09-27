from models import Session, Band, Venue, Concert

# Create a new database session to interact with the models
session = Session()

# Function to list all bands
def list_bands():
    # Query all band records from the database
    bands = session.query(Band).all()
    # Loop through each band and print its ID, name, and hometown
    for band in bands:
        print(f"{band.id}: {band.name} from {band.hometown}")

# Function to list all venues
def list_venues():
    # Query all venue records from the database
    venues = session.query(Venue).all()
    # Loop through each venue and print its ID, title, and city
    for venue in venues:
        print(f"{venue.id}: {venue.title} in {venue.city}")

# Function to create a new concert
def create_concert(band_id, venue_id, date):
    # Query the band by the provided ID
    band = session.query(Band).get(band_id)
    # Query the venue by the provided ID
    venue = session.query(Venue).get(venue_id)
    
    # If both the band and venue exist, create a new concert
    if band and venue:
        # Create a new Concert object with the provided date, band, and venue
        concert = Concert(date=date, band=band, venue=venue)
        # Add the new concert to the session (staging area)
        session.add(concert)
        # Commit the new concert to the database
        session.commit()
        # Print confirmation message with concert details
        print(f"Concert created: {band.name} at {venue.title} on {date}")
    else:
        # If either the band or venue is invalid, print an error message
        print("Invalid band or venue ID")

# Main function to run the CLI
def main():
    # Print a welcome message for the user
    print("Welcome to the Concert CLI!")
    
    # Infinite loop to keep the CLI running until the user decides to exit
    while True:
        # Display the menu options to the user
        print("\nOptions: 1) List Bands 2) List Venues 3) Create Concert 4) Exit")
        # Prompt the user to choose an option
        choice = input("Choose an option: ")
        
        # Execute the corresponding function based on user input
        if choice == '1':
            list_bands()  # List all bands
        elif choice == '2':
            list_venues()  # List all venues
        elif choice == '3':
            # Prompt for band ID, venue ID, and date to create a concert
            band_id = input("Enter band ID: ")
            venue_id = input("Enter venue ID: ")
            date = input("Enter concert date (YYYY-MM-DD): ")
            # Call the create_concert function with the provided inputs
            create_concert(band_id, venue_id, date)
        elif choice == '4':
            # Exit the program when user chooses option 4
            print("Goodbye!")
            break
        else:
            # Handle invalid input by displaying an error message
            print("Invalid option, please try again.")

# Check if this script is run directly, and if so, call the main() function
if __name__ == "__main__":
    main()
