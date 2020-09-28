## Data Engineering challenge assignments for Wealth42

### Introduction
The goal of this challenge is to test your familiarity with concepts in *Python and Data Engineering*.
To read more about the recruitment process and open opportunities at Wealth42, click [here](http://bit.ly/w42-hiring)


### Pick an evaluation mode

1.   **Wealth42's drafted assignment**: 
     *   **User Story**:
         *   Once the COVID-19 lock-down is lifted in many parts of the world, it would still be absolutely crucial to follow social distancing
             to avoid re-flaring the infection rates of the virus. Wherever possible, users who currently use public transport should
             be able to switch to alternate commute (like rental bikes). Specifically for the residents of London, you
             can utilize a feed provided by Transport For London, available [here](https://api-portal.tfl.gov.uk/docs).
     *   Follow [Instructions](#instructions) and [Submission Process](#submission-process) to complete the assignment.
     *   For success, ensure you get as many checks as in our [Assessment Criteria](#assessment-criteria)
     *   We typically take 5 days to evaluate this submission.

2.   **Project of your choice**: You are free to submit a project of your own with *some* conditions.
     *   Qualifying criteria for submission:
         *   MUST exhibit everything covered in the [Assessment Criteria](#assessment-criteria) and [Instructions](#instructions).
         *   You are authorised to publish the code as a public pull request via GitHub.
     *   Follow instructions as in the [Submission Process](#submission-process) to submit your work
     *   We typically take 15 days to evaluate this submission.       



### Instructions
* Explore the [API documentation](https://api-portal.tfl.gov.uk/docs)
* Use the bikepoint API to extract information on bike availability on various bike stands
* Design DDLs for - 
    * storing the real-time bike availability data across London
    * storing the bike availability across London across different time snapshots
* Implement these DDLs and create table(s) in MySQL for the schemas.
* Write script in Python to query this data source and update both databases accordingly
* Schedule this script to run every 5 minutes
* Include all of the DDL statements, python scripts and cron files in the repository
* Document list of assumptions made, which are not covered in the stories but have been used in building the app.
* Ask us anything – hiring at wealth42 dot com.


### Assessment Criteria
1. Maintainability and organisation of code
2. Correctly choosing normalisation or denormalisation where applicable 
3. Balancing between speed and quality of code - we understand that candidates can only spend limited time on these challenges.
If you do make any trade-offs in favour of saving time, do mention them in comments.  
4. Ownership - going beyond the exact job description to deliver a finished product.
For a Python/Data Engineer dev, this could potentially translate to: 
    1. Ensuring safety of API keys (if any are used)
    2. Creating a query utility that lets a user query the number of free bikes currently available by giving a subset of the 'commonName' string
5. No submissions to be made with compressed/binary files - all source code should be version controlled and visible in plain text in github.
6. How much the candidate stays in touch with us during the process of the project.
7. Follow [best practices](https://github.community/t/best-practices-for-pull-requests/10195) for pull requests.
7. [Guidelines](https://gist.github.com/turbo/efb8d57c145e00dc38907f9526b60f17) for clean commit messages.

### Submission Process
1. Clone this repository
2. Remove the assignment README’s (and all folders) and start developing your project in it
3. Add a readme that details on exactly how to run the code
4. If you are submitting a project of your choice, follow these steps –
    *   Attach the story of your project in a file named stories.md at root location. For reference, do checkout [stories](../stories/)
        >   *Since the project is something we'll need to understand purpose of before evaluating, this file should clearly explain the purpose of the application you are publishing.*
5. Fill the Pull Request template
    *   Check all the boxes that your Pull Request fulfills.
    *   Add the description/assumptions for your project 
    *   The time you spent on the project
    *   Your motivation behind choosing the project.
6. Raise a Pull Request


### Learning Resources
1. [Requests Library Official Documentation](https://requests.readthedocs.io/en/master/)
2. [RealPython guide to using python requests](https://realpython.com/python-requests/)
3. [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
4. [SQLAlchemy Tutorial](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
5. [Crontab Tutorial](https://stackabuse.com/scheduling-jobs-with-python-crontab/)