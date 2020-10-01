## Data Engineering challenge assignments for Wealth42

### Introduction
The goal of this challenge is to test your familiarity with concepts in *Python and Data Engineering*. To read more about the recruitment process and open opportunities at Wealth42, click [here](http://bit.ly/w42-hiring)

*Note: This is a public submission. Any work on this assignment does not bring Wealth42 or its employees any moat; and by design, is made to assess skills we need. Stories provided are unrelated to Wealth42's core business.* 

### Assignment
*   **User Story**:
    *   Once the COVID-19 lock-down is lifted in many parts of the world, it would still be absolutely crucial to follow social distancing to avoid re-flaring the infection rates of the virus. Wherever possible, users who currently use public transport should be able to switch to alternate commute (like rental bikes). Specifically for the residents of London, you can utilize a feed provided by Transport For London, available [here](https://api-portal.tfl.gov.uk/docs).
*   Follow [Instructions](#instructions) and [Submission Process](#submission-process) to complete the assignment.
*   For success, ensure you get as many checks as in our [Assessment Criteria](#assessment-criteria)
*   We typically take 5 days to evaluate this submission.


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
1. Meeting ALL criteria (which are not explicitly marked as optional) in the [Instructions](#instructions)
2. Maintainability and organisation of code
3. Correctly choosing normalisation or denormalisation where applicable 
4. Balancing between speed and quality of code - we understand that candidates can only spend limited time on these challenges. If you do make any trade-offs in favour of saving time, do mention them in comments.  
5. Ownership - going beyond the exact job description to deliver a finished product. For a Python/Data Engineer dev, this could potentially translate to: 
    1. Ensuring safety of API keys (if any are used)
    2. Creating a query utility that lets a user query the number of free bikes currently available by giving a subset of the 'commonName' string
6. No submissions to be made with compressed/binary files - all source code should be version controlled and visible in plain text in github.
7. How much the candidate stays in touch with us during the process of the project.
8. Follow [best practices](https://github.community/t/best-practices-for-pull-requests/10195) for pull requests.
9. [Guidelines](https://gist.github.com/turbo/efb8d57c145e00dc38907f9526b60f17) for clean commit messages.
10. Ability to learn and use version control via Git

### Submission Process
1. Fork this repository to your personal Github profile
2. Remove all files and folders in the forked repository and start developing your project in it
3. Add a readme to the root location of your repository that details on exactly how to run the code
4. Fill the [Pull Request template](https://github.com/wealth42/nick-fury/blob/master/.github/pull_request_template.md) while you are raising a [Pull Request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
    *   Check all the boxes that your Pull Request fulfills.
    *   Answer ALL questions in the template

### Code of Ethics
Please be original, all your submissions are public via GitHub.
Cite any external piece of code you're using, preferably with a link to the source.

### Learning Resources
1. [Requests Library Official Documentation](https://requests.readthedocs.io/en/master/)
2. [RealPython guide to using python requests](https://realpython.com/python-requests/)
3. [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
4. [SQLAlchemy Tutorial](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
5. [Crontab Tutorial](https://stackabuse.com/scheduling-jobs-with-python-crontab/)
6. [Version control with git](https://try.github.io/)