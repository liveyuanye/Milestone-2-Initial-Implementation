## WARNING: This is the file with our project requirements. If you're looking for the virtual environment dependencies, go to requirements.txt instead!

## Functional Requirements
1. A Sign Up form must be implemented to collect a user's username, password, and email. 
2. A Log In form will allow users to login using their email and password.
3. The system must provide the the user the option to Log Out.
4. A New Recipe form prompts the user for a recipe title, description, ingredients, and instructions.
5. The website should provide a feature to allow users to see and edit their own recipes.
6. A Delete Recipe option must be implemented to allow users to permanently remove their recipes from the database.
7. A View Recipe feature must enable users to view all details of a selected recipe, including title, description, ingredients, and instructions.
8. A View All Recipes feature must allow users to browse all recipes available in the database.
9. An Edit User Profile form must enable users to update their profile information, including display name, email, or password.
10. A Save Recipe (Favorites) feature must allow users to save recipes for quick access later.


## Non-functional Requirements
1. The system should notify the user if their Sign Up info doesn't follow security requirements.
2. Passwords must be hashed to ensure user security.
3. The Log Out option must ensure all authenticated access is taken back to prevent unauthorized access.
4. A New Recipe should save/publish to the database within 1 second.
5. Changes to an Existing Recipe should save/publish to the database within 1 second.
6. The Delete Recipe operation must confirm the user's intent to delete and execute the operation within 1 second.
7. The View Recipe feature should retrieve and display recipe details within 1 second after selection.
8. The View All Recipes feature should list all recipes from the database within 2 seconds.
9. The Edit User Profile operation should save changes to the database within 1 second.
10. The Save Recipe (Favorites) feature should notify the user of successful saving within 1 second.


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
5. Edit Recipe
- **Actor(s):** User and system.
- **Pre-condition:** User has an existing recipe they want to change.
- **Trigger:** User selects Change Recipe.
- **Primary Sequence:**
  1. The system shows the user the selected recipe in an editable form.
  2. The user makes changes to the recipe.
  3. The user selects Save.
  4. The system saves the updated recipe information.
  5. The user is sent back to the main page.
- **Primary Postconditions:** The changed recipe can now be viewed in replacement of the old recipe by all authenticated users.
- **Alternate Sequence:**
  1. The system shows the user the selected recipe in an editable form.
  2. The user deletes the title.
  3. The user selects Save.
  4. The system prompts the user to not leave any field blank.
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
9. Edit User Profile
- **Actor(s):** User and system.
- **Pre-condition:** User wants to update their profile information.
- **Trigger:** User selects the "Edit Profile" option.
- **Primary Sequence:**
  1. The system shows the user their current profile information in an editable form.
  2. The user updates their display name, email, or password.
  3. The user selects "Save".
  4. The system updates the existing recipe information.
- **Primary Postconditions:**  The user's updated profile information is saved and reflected across the website.
- **Alternate Sequence:**
  1. The system shows the user their current profile information in an editable form.
  2. The user leaves a required field (e.g., email or password) blank.
  3. The user selects "Save".
  4. The system prompts the user to fill out all required fields.
---
10. Save Recipe (Favorites)
- **Actor(s):** User and system.
- **Pre-condition:** User wants to save a recipe for quick access later.
- **Trigger:** User selects the "Save Recipe" or "Favorite" option.
- **Primary Sequence:**
  1. The user selects the recipe they want to save.
  2. The system adds the recipe to the user's list of saved recipes.
  3. The system notifies the user that the recipe has been saved.
- **Primary Postconditions:** The recipe is saved under the user's profile for quick access later.
- **Alternate Sequence:**
  1. The user selects the recipe they want to save.
  2. The system fails to save the recipe due to a network issue.
  3. The system notifies the user of the failure and prompts them to try again later.
---
11. Rate Recipe
- **Actor(s):** User and system.
- **Pre-condition:** User is logged in and viewing a specific recipe they wish to rate.
- **Trigger:** User selects a rating option (e.g., star rating) for the recipe.
- **Primary Sequence:**
  1. User selects their desired rating for the recipe.
  2. System saves the rating and updates the recipe's overall average rating.
  3. System notifies the user of successful submission and displays the updated rating on the recipe page.
- **Primary Postconditions:** The user's rating is recorded, and the recipe's average rating is updated and visible.
- **Alternate Sequence:**
  1. User attempts to select a rating.
  2. The system detects the user is not logged in.
  3. The system prompts the user to log in or register to rate recipes.
---
12. Comment on Recipe
- **Actor(s):** User and system.
- **Pre-condition:** User is logged in and viewing a specific recipe they wish to comment on.
- **Trigger:** User selects the "Add Comment" option for the recipe.
- **Primary Sequence:**
  1. User types and submits their comment.
  2. System validates and saves the comment, associating it with the user and the recipe.
  3. System notifies the user of successful posting and displays the new comment on the recipe page.
- **Primary Postconditions:** The user's comment is saved and is visible to other authenticated users viewing the recipe.
- **Alternate Sequence:**
  1. User attempts to access the comment input field or submit a comment.
  2. The system detects the user is not logged in.
  3. The system prompts the user to log in or register to comment on recipes.

