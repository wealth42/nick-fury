Introduction
-----------------
The goal of this challenge is to test your familiarity with concepts in Python and Data Engineering. To read more about the recruitment process and open opportunities at Wealth42, click here

User story
------------------
Once the COVID-19 lock-down is lifted in many parts of the world, it would still be absolutely crucial to follow social distancing to avoid re-flaring the infection rates of the virus. Wherever possible, users who currently use public transport should be able to switch to alternate commute (like rental bikes). Specifically for the residents of London, you can utilize a feed provided by Transport For London, available here.

Instructions
--------------------------------------
Explore the API documentation(https://api-portal.tfl.gov.uk/docs)
Use the bikepoint API to extract information on bike availability on various bike stands

Design DDLs for -
storing the real-time bike availability data across London
storing the bike availability across London across different time snapshots
Implement these DDLs and create table(s) in MySQL for the schemas.
Write script in Python to query this data source and update both databases accordingly
Schedule this script to run every 5 minutes
Include all of the DDL statements, python scripts and cron files in the repository
Document list of assumptions made, which are not covered in the stories but have been used in building the app.
Ask us anything – hiring at wealth42 dot com.


Assessment Criteria:
----------------------------------------
Maintainability and organisation of code
Correctly choosing normalisation or denormalisation where applicable
Balancing between speed and quality of code - we understand that candidates can only spend limited time on these challenges. If you do make any trade-offs in favour of saving time, do mention them in comments.
Ownership - going beyond the exact job description to deliver a finished product. For a Python/Data Engineer dev, this could potentially translate to:
Ensuring safety of API keys (if any are used)
Creating a query utility that lets a user query the number of free bikes currently available by giving a subset of the 'commonName' string
How much the candidate stays in touch with us during the process of the project
Guidelines for clean commit messages