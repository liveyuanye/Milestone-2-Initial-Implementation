## WARNING: This is the file with our project requirements. If you're looking for the virtual environment dependencies, go to requirements.txt instead!

## Functional Requirements
1. A Sign Up form must collect and save the user's username, password, and email.
2. A Log In form must authenticate users using their email and password.
3. Users must have the option to Log Out, removing their authenticated access.
4. Users must be able to create a New Recipe by entering a title, description, ingredients, and instructions.
5. The system must assign sequential numeric IDs to recipes upon creation, making them accessible via a structured URL (e.g., http://127.0.0.1:5000/recipe/[id]).
6. Users must have the ability to permanently delete their recipes.
7. Users must be able to view all details (title, description, ingredients, instructions) of a specific recipe.
8. Users must be able to browse all available recipes in the database.
9. Users must have the option to share recipe details through social media platforms (X, Instagram, Facebook, WhatsApp).
10. Users must have the option to display a randomly selected recipe from the database.


## Non-functional Requirements
1. Sign Up must enforce secure password complexity and notify the user of non-compliance immediately.
2. Passwords must be securely hashed before storage to ensure user data protection.
3. Log Out must revoke all authenticated sessions instantly to prevent unauthorized access.
4. New recipes must be saved to the database and accessible via their URL within 1 second after submission.
5. Recipe ID assignment must reliably generate unique, sequential numeric IDs without errors.
6. Deleting a recipe must prompt the user for confirmation and execute deletion within 1 second after confirmation.
7. The selected recipe details must load and display within 1 second of user selection.
8. The full list of recipes must be retrieved and displayed to users within 2 seconds of navigation.
9. Social media sharing options must reliably open in a new window immediately upon selection.
10. The Random Recipe function must select and display recipe details within 1 second of the user's request.


## Use Cases
Welson (1-5)

1. User Registration
- **Actor(s):** User and system.
- **Pre-condition:** User has unused username, password, and email.
- **Trigger:** User selects Sign Up option.
- **Primary Sequence:**
  1. User enters username, password, and email.
  2. System saves the user's registration information.
  3. The user is notified of their account creation.
  4. The user is sent to the main page.
- **Primary Postconditions:** The user has authenticated access to the rest of the website.
- **Alternate Sequence:**
  1. User enters username, password, and email.
  2. The password does not meet complexity requirement(s).
  3. The system prompts the user to enter a different password.
---
2.  User Login
- **Actor(s):** User and system.
- **Pre-condition:** User knows their email and password.
- **Trigger:** User selects Log In option.
- **Primary Sequence:**
  1. User enters email and password.
  2. The system validates the user's email and password.
  3. The system gives the user access and notifies the user that they are logged in.
  4. The user is sent to the main page.
- **Primary Postconditions:** The user has authenticated access to the rest of the website.
- **Alternate Sequence:**
  1. User enters email and password.
  2. The system doesn't recognize the entered email/password combination.
  3. The system prompts the user to retry a different email/password.
---
3. User Logout
- **Actor(s):** User and system.
- **Pre-condition:** User wants to log out.
- **Trigger:** User selects Log Out option.
- **Primary Sequence:**
  1. The system asks the user if they are sure they want to log out.
  2. The user selects "Yes".
  3. The system removes the user's authenticated access.
  4. The user is redirected back to the login page.
- **Primary Postconditions:** The user's authenticated access is removed and has to login for it again.
- **Alternate Sequence:**
  1. The user appears to still be logged in.
  2. The system fails due to a network issue.
  3. The system notifies the user and is asked to try again.
---
4. Create Recipe
- **Actor(s):** User and system.
- **Pre-condition:** User has a recipe.
- **Trigger:** User selects Create Recipe option.
- **Primary Sequence:**
  1. The system prompts the user to enter their recipe with a form.
  2. User enters their recipe's title, description, ingredients, and instructions.
  3. The user clicks Save.
  4. The system saves the new recipe information.
- **Primary Postconditions:** The newly created recipe can be seen by all authenticated users.
- **Alternate Sequence:**
  1. The system prompts the user to enter their recipe with a form.
  2. The user fills out the form unfinished.
  3. The user clicks Save.
  4. The system prompts the user to properly fill out the form.
---
5. Sequential Recipe ID Generation
- **Actor(s):** User and system.
- **Pre-condition:** User creates a new recipe via the "Create Recipe" form.
- **Trigger:** User submits the new recipe form.
- **Primary Sequence:**
  1. User submits the recipe details (title, description, ingredients, and instructions).
  2. System generates the next available sequential ID number.
  3. System stores the recipe with the generated ID.
  4. Recipe becomes available at URL http://127.0.0.1:5000/recipe/[generated_id].
- **Primary Postconditions:** The newly created recipe has a sequential numeric URL identifier accessible directly by the user.
- **Alternate Sequence:**
  1. User submits the recipe details.
  2. System encounters an internal error while generating the sequential ID.
  3. System informs the user to retry submitting the recipe.
---
Ye (6-10)

6. Delete Recipe
- **Actor(s):** User and system.
- **Pre-condition:** User has an existing recipe they want to delete. 
- **Trigger:** User selects the Delete Recipe option.
- **Primary Sequence:**
  1. The system shows the user the selected recipe with a confirmation prompt.
  2. The user selects "Delete".
  3. The system permanently deletes the recipe information.
  4. The user is redirected back to the main page.
- **Primary Postconditions:**  The recipe is permanently removed and can no longer be viewed by authenticated users.
- **Alternate Sequence:**
  1. The system shows the user the selected recipe with a confirmation prompt.
  2. The user selects "Delete".
  3. The system fails to user has not loggin in.
  4. The system notifies the user to loggin in and prompts them to try again.
---
7. View Recipe
- **Actor(s):** User and system.
- **Pre-condition:** At least one recipe is available on the website.
- **Trigger:** User selects a recipe to view its details.
- **Primary Sequence:**
  1. User selects a recipe from the list on the homepage or search results.
  2. System retrieves the selected recipe details.
  3. System displays the recipe title and description.
- **Primary Postconditions:** The user can see all details of the selected recipe.
- **Alternate Sequence:**
  1. The user selects a recipe to view its details.
  2. The system fails to retrieve the recipe details due to an internal or network issue.
  3. The system notifies the user of the error and prompts them to try again later.
---
8. View All Recipes
- **Actor(s):** User and system.
- **Pre-condition:** Recipes have been created and are available on the website.
- **Trigger:** User navigates to the homepage or selects the "View All Recipes" option.
- **Primary Sequence:**
  1. User navigates to the homepage or selects the "View All Recipes" button.
  2. System retrieves all available recipes.
  3. System displays a list showing the title for each recipe.
- **Primary Postconditions:** The user can browse all available recipes on the website.
- **Alternate Sequence:**
  1. The user navigates to the homepage or selects the "View All Recipes" option.
  2. The system fails to retrieve recipes due to a network issue.
  3. The system notifies the user of the error and prompts them to try again later.
---
9. Share Recipe
- **Actor(s):** User and system.
- **Pre-condition:** User is viewing a specific recipe's detail page.
- **Trigger:** User selects a share option for the currently viewed recipe.
- **Primary Sequence:**
  1. User clicks on the share icons for social media platforms (X, Instagram, Facebook, WhatsApp).
  2. System open a new window for social media platforms.
  3. User confirms sharing social media platform.
- **Primary Postconditions:** Recipe details can be successfully shared on selected social media platforms or messaging services.
- **Alternate Sequence:**
  1. User clicks on the share icon.
  2. System opens a new window for the selected social media platform.
  3. User decides not to share and closes the new window.
  4. System returns the user to the recipe detail page without any changes.
 ---
10. Random Recipe
- **Actor(s):** Random Recipe Display
- **Pre-condition:** At least one recipe exists in the system.
- **Trigger:** User selects the "Random Recipe" button.
- **Primary Sequence:**
  1. User clicks on the "Random Recipe" button.
  2. System selects a recipe at random from the existing recipes stored in the system.
  3. System navigates the user to the detailed view of the randomly selected recipe.
- **Primary Postconditions:** User sees a randomly selected recipe's detailed view, including title, description, ingredients, instructions, and creation details.
- **Alternate Sequence:**
  1. User clicks on the "Random Recipe" button.
  2. System fails to retrieve a random recipe due to a network issue.
  3. System informs user of the issue and requests the user to try again later.
 
  
