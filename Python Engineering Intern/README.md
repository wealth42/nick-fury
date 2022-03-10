# Python Engineering Intern challenge assignments for Wealth42 SOLUTION

## Introduction
The goal of this challenge is to test your familiarity with concepts in *Python and Data Extraction*. To read more about the recruitment process and open opportunities at Wealth42, click [here](https://bit.ly/w42-careers)

*Note: This is a public submission. Any work on this assignment does not bring Wealth42 or its employees any moat; and by design, is made to assess skills we need. Stories provided are unrelated to Wealth42's core business.* 

## Assignment
*   **User Story**:
    *   We tend to read a lot of documents daily, be it email attachments or your bank statements or your university results. The most preferred way of sharing documents are PDF. Each of these type of PDFs maintain a specific structure. If a system were to be designed to perform some analysis on these PDFs, then the system would expect a structured format for the data that is present in the PDF.
*   Follow [Instructions](#instructions) and [Submission Process](#submission-process) to complete the assignment.
*   For success, ensure you get as many checks as in our [Assessment Criteria](#assessment-criteria)
*   We typically take 5 days to evaluate this submission.


## Instructions
* Explore the [PDFs](https://github.com/wealth42/nick-fury/tree/master/Python%20Engineering%20Intern/Resources/) provided.
* Select **any one** of the two PDFs to work on.
* Write a script in Python to parse the selected PDF. The script extracts the data in the PDF and saves the output in a JSON file.
* Sample JSON output file is provided for your reference for each PDF. Bonus points for enhancement of the JSON output with reasoning. Keep in mind, the output is just a sample and not the entire json that is expected. You need to parse the entire document and return the complete JSON.
* Try to generalize the logic as much as possible -
    * try not to use excessively large number of _if statements_
    * write generalized regex to parse similar type of lines
    * json output should have appropriate data points
* Document list of assumptions made, which are not covered in the stories but have been used in building the script.
* Ask us anything – hiring at wealth42 dot com.


## Assessment Criteria
1. Meeting ALL criteria (which are not explicitly marked as optional) in the [Instructions](#instructions)
2. Maintainability and organisation of code
3. Balancing between speed and quality of code - we understand that candidates can only spend limited time on these challenges. If you do make any trade-offs in favour of saving time, do mention them in comments.  
4. Ownership - going beyond the exact job description to deliver a finished product. For a dev, this could potentially translate to: 
    1. Writing descriptive variable names
    2. Writing comments for complicated logics
    3. Providing sample text which a particular regex would parse
    4. [Optional] Creating a Pandas DataFrame from the parsed json
5. No submissions to be made with compressed/binary files - all source code should be version controlled and visible in plain text in github.
6. How much the candidate stays in touch with us during the process of the project.
7. Follow [best practices](https://github.community/t/best-practices-for-pull-requests/10195) for pull requests.
8. [Guidelines](https://gist.github.com/turbo/efb8d57c145e00dc38907f9526b60f17) for clean commit messages.
9. Ability to learn and use version control via Git

## Submission Process
1. Fork this repository to your personal Github profile
2. Remove all files and folders in the forked repository and start developing your project in it
3. Add a readme to the root location of your repository that details on exactly how to run the code
4. Fill the [Pull Request template](https://github.com/wealth42/nick-fury/blob/master/.github/pull_request_template.md) while you are raising a [Pull Request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
    *   Check all the boxes that your Pull Request fulfills.
    *   Answer ALL questions in the template

## Code of Ethics
Please be original, all your submissions are public via GitHub.
Cite any external piece of code you're using, preferably with a link to the source.

## Learning Resources
1. [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
2. [Data Extraction from Unstructured PDFs](https://www.analyticsvidhya.com/blog/2021/06/data-extraction-from-unstructured-pdfs/)
3. [Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
4. [Version control with git](https://try.github.io/)

## Approach to the problem statement
1. I used PyPDF2 and camelot to convert the pdf table to csv file.
2. Then I converted .csv file to dataframes using pandas library.
3. Finally using json dumps converted to .json file.

## Detailed explaination
Using PyPDF2 and camelot converted the pdf image table to .csv file, through **to_csv** method then the generated csv file is appled to pandas to convert it to dataframe, once the dataframe is created creating a empty json file to store the converted data now its easy to convert the data to **.json** file using loads() and dumps() methods and writing the data in json format.