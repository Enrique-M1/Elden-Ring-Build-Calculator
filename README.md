# Elden-Ring-Build-Calculator
This is a calculator that allows a user to determine what kind of build they want to run during their 
time in Elden Ring. Gives you stats at level 150 based on starting class and armor depending on the 
build you choose.

# Installation 
    NOTE: It is assumed that you already have python installed.

1.) Install MariaDB from here

        Link: https://mariadb.org/download/
    
2.) Pip install the necessary packages:
    
        - pip install -r requirements.txt
        
        Note: This will install all necessary packages for the program to run.

# Running the program: 

1.) Run the database setup script:

    mariadb_database_setup.py
    
    NOTE: This is only necessary if you're running the program for the first time.
2.) Run the API service: 
    
    API_service.py

# Using the program:

### For a UI version of the program:
    Navigate to the resulting link in the terminal

### For a CLI version of the program:
    
    Run client.py instead
