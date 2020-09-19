## ReactJS challenge assignments for Wealth42

### Introduction
The goal of this challenge is to test your familiarity with concepts in ReactJS.
To read more about the recruitment process and open opportunities at Wealth42, click [here](http://bit.ly/w42-hiring)

### Pick an evaluation mode

1.   **Project of your choice**: You are free to submit a project of your own with *some* conditions.
     *   Qualifying criteria for submission:
         *   MUST exhibit everything covered in the [Assessment Criteria](#assessment-criteria) and [Instructions](#instructions).
         *   You are authorised to publish the code as a public pull request via GitHub, following the steps as covered in [Submission Process](#submission-process)
     *   Additional criteria for submission:
         *   Attach the story of your project in a file named stories.md at root location. For reference, do checkout [stories](../stories/)
                >   *Since the project is something we'll need to understand purpose of before evaluating, this file should clearly explain the purpose of the application you are publishing.*

2.   **Wealth42's drafted assignment**: 
     *   You can select any one of the stories mentioned in the [stories](../stories/) folder, and develop a ReactJS webapp for it. 
     *   Follow [Instructions](#instructions) and [Submission Process](#submission-process) to complete the assignment.
     *   For success, ensure you get as many checks as in our [Assessment Criteria](#assessment-criteria)


### Instructions

*   API: 
    *   Create an API design for all integrations required for the selected user story (this can be a simple JSON request/response structure)
    *   Create dummy data for all APIs designed
    *   Create mock server stubs from this dummy data (an easy way to do this is to use [Postman](https://www.postman.com))
    *   Integrate with the mock stubs
*   View: 
    *   Design reusable components that are used across all the screens relevant
    *   Include any collateral/stock images (make sure these are okay for public use)
    *   Include icons/vector art wherever relevant
*   State Management: 
    *   Use redux for state management
    *   thunk/saga for middleware
*   Routing: Use React-router
*   Styling: SASS 

### Assessment Criteria
1. Maintainability and organisation of code 
2. Usage of
    1. Redux for state management
    2. Saga/Thunk for middleware
    3. UI Component libraries
3. Balancing between speed and quality of code - we understand that candidates can only spend limited time on these challenges.
If you do make any trade-offs in favour of saving time, do mention them in comments.  
4. Ownership - going beyond the exact job description to deliver a finished product.
For a ReactJS dev, this could translate to: 
    1. creating mocks from the API documentation
    2. adding icons/collateral 
5. How much the candidate stays in touch with us during the process of the project
6. [Guidelines](https://gist.github.com/turbo/efb8d57c145e00dc38907f9526b60f17) for clean commit messages

### Submission Process
1. Clone this repository
2. Remove the assignment README’s (and all folders) and start developing your project in it
3. Add a readme that details on exactly how to run the code
4. Raise a Pull Request


### Learning Resources

* ReactJS
    * [The official ReactJS Tutorial](https://reactjs.org/tutorial/tutorial.html)

* Redux 
    * [Basics](https://redux.js.org/basics/actions)
    * [Redux Toolkit (Advanced)](https://www.valentinog.com/blog/redux/)
* Saga/Thunk
    * [Hackernoon Saga tutorial](https://hackernoon.com/redux-saga-tutorial-for-beginners-and-dog-lovers-aa69a17db645)
    * [Digital Ocean Thunk tutorial](https://www.digitalocean.com/community/tutorials/redux-redux-thunk)
    * [Codeburst Thunk blog](https://codeburst.io/understanding-redux-thunk-6dbae0241817) 
* UI Component Libraries
    * [Material UI](https://material-ui.com)
    * [ANT Design](https://ant.design)