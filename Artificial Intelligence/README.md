## AI challenge assignments for Wealth42

### Introduction
The goal of this challenge is to test your familiarity with concepts in  Artificial Intelligence (with Python). To read more about the recruitment process and open opportunities at Wealth42, click [here](http://bit.ly/w42-hiring)

*Note: This is a public submission. Any work on this assignment does not bring Wealth42 or its employees any moat; and by design, is made to assess skills we need. Stories provided are unrelated to Wealth42's core business.* 

### User Story for Assignment
A school administrator has to manage a Teacher's Schedule by balancing the number of lecture and the number of classes he/she has to teach in a week . For a school to run efficiently, it is necessary that the administrator carves out an optimised schedule for teachers as well as the students with the following constraints:
1.  There are 5 teachers who have specialization in 5 different subjects.
2. Teacher's have preferences for teaching on certain days over others: 
You can assume the preferences by yourself by creating a preference map like this (on a range from 0-10,
10 being the highest , this is absolute for every day and not relative to the other days):    

        "teacher1":{
            "Monday": 5,
            "Tuesday": 10,
            ....
        },...

3.  Students are divided into 3 batches.
4.  Every batch of students must get at least 5 lectures of each subject, every week.
5.  There are 5 lectures each day for all batches
6.  Teachers are not allowed to have more than 2 lectures in a day for a class.
   
Optimisation objective: For every lecture taken by any teacher, the 'preference score' is allocated as per the teacher's preference mapping to be taking a lecture in that day. The objective is to optimize the sum of this 'preference score' across the timetables of all teachers.

Using this optimisation objective, find the optimal weekly time table for all 3 batches of the students.
### Instructions
*   Create an Optimized solution using the [Pyomo](http://www.pyomo.org/) library for the school administrator to manage the teacher's schedule considering all constraints.
*   Document list of assumptions made, which are not covered in the [story](#user-story-for-assignment) but have been used in building the optimiser.
*   Ask us anything – hiring at wealth42 dot com.

### Assessment Criteria
1. Meeting ALL criteria (which are not explicitly marked as optional) in the [Instructions](#instructions)
2. Maintainability and organisation of code 
3. Balancing between speed and quality of code - we understand that candidates can only spend limited time on these challenges. If you do make any trade-offs in favour of saving time, do mention them in comments.  
4. Ownership - going beyond the exact job description to deliver a finished product. 
5. No submissions to be made with compressed/binary files - all source code should be version controlled and visible in plain text in github.
6. How much the candidate stays in touch with us during the process of the project.
7. Follow [best practices](https://github.community/t/best-practices-for-pull-requests/10195) for pull requests.
8. [Guidelines](https://gist.github.com/turbo/efb8d57c145e00dc38907f9526b60f17) for clean commit messages.
9. Ability to learn and use version control via Git

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
1. [Pyomo Documentation](http://www.pyomo.org/)
2. [Version control with git](https://try.github.io/)