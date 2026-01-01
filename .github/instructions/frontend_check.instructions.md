Check that the following instructions are followed for setting up and updating the octofit-tracker frontend React application. if not, make the necessary changes.

Let's setup the octofit-tracker frontend React  framework and
ensure everything is created in the `octofit-tracker/frontend` directory by using `--prefix`

1. Make sure the the octofit-tracker/frontend directory exists.
2. create the react app
3. Install react, bootstrap, and react-router-dom
4. Import bootstrap css in the src/index.js file.
5. Don't change .gitignore file

Let's update the octofit-tracker frontend React components.

- Update the following components to include the React framework to point to the backend REST API:
  - src/App.js
  - src/index.js
  - src/components/Activities.js
  - src/components/Leaderboard.js
  - src/components/Teams.js
  - src/components/Users.js
  - src/components/Workouts.js
- In each component replace the fetch url with the codespace url
  https://$REACT_APP_CODESPACE_NAME-8000.app.github.dev/api/[component]/
  for the Django rest framework backend.
  make sure all components are pulling data from the REST api endpoint
  for display in the REACT frontend
- Make sure to use the correct port and protocol http or https.
- Update src/App.js to include the main navigation for all components.
- Make sure react-router-dom is used for the navigation menu.
- The react app should show the navigation menu and the components.
- Update all components to log the fetched data and make them compatible with both paginated (.results) and plain array responses.
- Add console.log statements to each component to log the fetched data and the REST API endpoints.

Let's style this like App.css and make it look nice.

- Let's make the App.js and all components javascript files in the app are consistent with the following:
  - Use bootstrap tables for the data in all javascript components.
  - Use bootstrap buttons for the buttons.
  - Use bootstrap headings for the headings.
  - Use bootstrap links for the links.
  - Use bootstrap navigation for the navigation menu.
  - Use bootstrap forms for the forms.
  - Use bootstrap cards for the cards.
  - Use bootstrap modals for the modals.
  - Consistent table layouts for all components data.

  Let's style this like App.css and make it look nice.

-  Edit the App.css file to do the following:
  - Add some color to the background.
  - Add some color to the text.
  - Add some color to the tables.
  - Add some color to the buttons.
  - Add some color to the headings.
  - Add some color to the links.
  - Add some color to the navigation menu.
- Add the octofitapp-small logo justified to the left to the app and make it look nice.
- Add a favicon to the app and make it look nice.

---
