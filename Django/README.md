## Django challenge assignments for Wealth42

### Introduction
The goal of this challenge is to test your familiarity with concepts in Django.
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
     *   You can select any one of the stories mentioned in the [stories](../stories/) folder, and develop an API service using Django for it. 
     *   Follow [Instructions](#instructions) and [Submission Process](#submission-process) to complete the assignment.
     *   For success, ensure you get as many checks as in our [Assessment Criteria](#assessment-criteria)


### Instructions

*   Model: Design database schema and implement using Django ORM with validations
*   View: API Design
    *   The app is supposed to be API driven.
    *   Written with Django Rest Framework
    *   Documentation (as a Postman collection)
    *   All stories should be executable over this API
*   View: UI Design (Optional, for brownie points, in addition to API Design)
    *   An HTML frontend with ANY framework of choice
    *   This can be API driven or rendered from Django templates.
*   Include docstrings for all functions and classes
*   Use either SQLite or MySQL for the prototype
*   Document list of assumptions made, which are not covered in the stories but have been used in building the app.
*   Ask us anything – hiring at wealth42 dot com.


### Assessment Criteria
1. Maintainability and organisation of code 
2. Balancing between speed and quality of code - we understand that candidates can only spend limited time on these challenges.
If you do make any trade-offs in favour of saving time, do mention them in comments.  
3. Ownership - going beyond the exact job description to deliver a finished product.
For a Django dev, this could translate to: 
    1. Creating a sample API-driven UI that also communicates with this API
4. How much the candidate stays in touch with us during the process of the project
6. [Guidelines](https://gist.github.com/turbo/efb8d57c145e00dc38907f9526b60f17) for clean commit messages

### Submission Process
1. Clone this repository
2. Remove the assignment README’s (and all folders) and start developing your project in it
3. Add a readme that details on exactly how to run the code
4. Raise a Pull Request

### Learning Resources
[The Official Django Tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)