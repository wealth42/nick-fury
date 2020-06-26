This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

1. JSON-SERVER
 was establied with command " json-server --db.json -p 3001 -d 1500 "
 Json-sever folder is included. u just need to go into the folder and run this command.

2. After that you need to go into the main folder and run "yarn start", this will start the website at localhost:3000 while taking and storing all its data from localhost:3001. That's the fake REST API server.

images are included inn Json-sever public folder.

at the home page. user can click to login. the Modal will open. But I didn't run the user authentication and User authorization, cause that'll be the part of Node.js and Express.js that is server side. If we use the server side then we can also go into src/HeaderComponent.js and uncomment the line of code and make the single page application specifically for a particular user. That means when the client will login. He/She will have the option to Book Therapist but no Option of show Bookings.
Vice versa if a Therapist is logged in.
Right now there is no Login, so both the components are visible.

Register user is fully functional. when a new user register if its a therapist, it will be added in the "therapists" object of json-server file db.json. if not therapist then added to "users" object of db.json.

user can make bookings, give comment about the therapist.
all this data is succesfully stored in db.json file and succesfully displayed on the single page application.

I didn't used SASS, but I can do that, I just didn't like to do that.


I would like to add that it was a fun Assignment, I learned some new things and refreshed some concepts. It was fun, and I'm hoping forward to work in a fun and learning environment where everyone loves what they do. what can I say more, "talking is cheap, let's look at code".
