#!/bin/bash

# Combined list of male and female first names
names=("Noah" "Theo" "Luca" "Arthur" "Oliver" "Archie" "George" "Leo" "Freddie" "Arlo"
"Alfie" "Oscar" "Teddy" "Henry" "Albie" "Finley" "Jude" "Charlie" "Elijah" "Tommy"
"Harry" "Oakley" "Hudson" "Roman" "Rory" "Reuben" "Louie" "Jack" "Reggie" "Lucas"
"Theodore" "Ezra" "Isaac" "Thomas" "Jacob" "Max" "James" "Ethan" "Ronnie" "Frankie"
"Rowan" "Harrison" "Adam" "Riley" "William" "Jaxon" "Grayson" "Caleb" "Mason" "Hunter"
"Logan" "Hugo" "Sonny" "Jesse" "Vinnie" "Alexander" "Joshua" "Enzo" "Yusef" "Finn"
"Austin" "Louis" "Cody" "Ollie" "Kai" "Musa" "Carter" "Yahya" "Edward" "Muhammed"
"Bobby" "Stanley" "Joseph" "Milo" "Elliot" "Myles" "Dylan" "Eli" "Blake" "Alex"
"Elias" "Jasper" "Zachary" "Elliot" "Chester" "Ralph" "Gabriel" "Brody" "Rupert"
"Toby" "Albert" "Otis" "Ellis" "Daniel" "Liam" "Jenson" "Ruben" "David" "Jayden"
"Jackson" "Amelia" "Olivia" "Isla" "Ava" "Sophia" "Mia" "Harper" "Evelyn" "Ella"
"Abigail" "Scarlett" "Grace" "Chloe" "Lily" "Avery" "Sophie" "Hannah" "Aria"
"Layla" "Zoe" "Nora" "Charlotte" "Camila" "Penelope" "Riley" "Leah" "Hazel" "Lucy"
"Victoria" "Mila" "Ruby" "Luna" "Lila" "Ellie" "Nova" "Sadie" "Hannah" "Kinsley"
"Addison" "Stella" "Bella" "Brooklyn" "Skylar" "Mackenzie" "Naomi" "Autumn" "Savannah"
"Sadie" "Everly")

# Loop to create users and post tweets for 50 random users
for i in {1..100}; do
    # Randomly pick a first name from the updated list
    first_name=${names[$RANDOM % ${#names[@]}]}

    # Random letter to append to the username
    random_letter=$(echo {A..Z} | tr -s ' ' '\n' | shuf -n 1)

    # Combine the first name and random letter to create the username
    username="$first_name$random_letter"

    # Debug: Output the generated username for verification
    echo "Generated Username: $username"

    # Create a new user with the unique username
    curl -X POST http://localhost:5000/api/create_user -H "Content-Type: application/json" -d "{\"username\": \"$username\", \"email\": \"$username@example.com\", \"password\": \"SecurePassword123\"}"

    # Log in as the newly created user and store the session cookie
    curl -X POST http://localhost:5000/api/login -H "Content-Type: application/json" -d "{\"username\": \"$username\", \"password\": \"SecurePassword123\"}" -c cookie_"$i".txt

    # Post a sample tweet for each user
    #curl -X POST http://localhost:5000/api/create_tweet -H "Content-Type: application/json" -d "{\"tweet\": \"$username's first tweet!\"}" -b cookie_"$i".txt

    # Wait for a moment to ensure the post is successfully made
    sleep 2
done
