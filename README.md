# To run the project
*   install all the dependencies specified in ```requirements.txt``` file.
*   run following commands:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
*   then to run the server run the following:
    ```bash
    python manage.py runserver
    ```
    
## Stories Completed
*   A Client should be able to 
    *   Create a Client account and login using their email and password
    *   Search and map a Therapist to their account.
    *   View list of therapists who have access to emotions journal along with these actions –
        *   Remove a therapist mapped to account
        *   Remove a therapist’s access to the journal, but not mapping to account
        *   Send a message to a therapist and view the history of exchanges.
    *   Add record of an emotion felt. This should include the time of emotion, feeling and intensity
    *   Select therapists from a list of available therapists on the platform
*   A Therapist should be able to 
    *   Create a Therapist account and login using their email and password
    *   View list of clients along with actions like –
        *   Request a new client to be mapped for therapy. This allows for associating session notes to client. By default, journal access is off.
        *   Send a message to a client and view the history of exchanges.
        *   Remove a client
    *   View client journals
    
## Following is the full list of APIs created
| API endpoint        | HTTP Method           | Required Parameters  | Description| Accessible By |
| ------------- |:-------------:| -----:| ---:| ----: |
| ```api/login/```      | POST | email, password | to log user in (client as well as therapist)| Anonymous |
| ```api/logout```      | GET      |    | To log out | Client or Therapist |
| ```api/register/``` | POST      |    email, password, type ("Client"/"Therapist") | to register user | Anonymous |
| ```api/chat/<id-of-other-user\>``` | GET      |    | To access chat history | Client or Therapist |
| ```api/chat/<id-of-other-user\>/``` | POST      |  message (message to send)  | To send message to someone having <id\> | Client or Therapist |
| ```api/search-therapists``` | GET      |    | to show available therapists to clients. | Client |
| ```api/map-therapist/<id-of-therapist\>``` | GET      |    | map a therapist that is not actively mapped to the requesting client. | Client |
| ```api/map-therapist/<id-of-therapist\>``` | DELETE      |    | remove the mapping of a therapist and a requesting client. | Client |
| ```api/mapped-therapists``` | GET      |    | show therapists that are actively mapped to the requesting client. | Client |
| ```api/therapists-with-journal``` | GET      |    | show therapists that are actively mapped and has journal access to the requesting client. | Client |
| ```api/remove-journal-access/<id-of-therapist\>``` | DELETE      |    | to remove the journal access of a therapist for a requesting client. | Client |
| ```api/record-emotion/``` | POST      |  emotion, intensity  | to store emotion felt by the client. | Client |
| ```api/therapist/journals``` | GET      |    | will return the list of journals that are allowed to be accessed by requesting therapist. | Therapist |
| ```api/therapist/journals/<id-of-client\>``` | GET      |    | will return a particular user's journal if requesting therapist has allowed access to it. | Therapist |
| ```api/therapist/clients``` | GET      |    | will show list of mapped clients to the therapist. | Therapist |
| ```api/therapist/clients/<id-of-client\>``` | GET      |    | will return a particular client if requesting therapist is mapped. | Therapist |
| ```api/therapist/clients/<id-of-client\>/``` | DELETE      |    | will allow therapists to remove the mapping to existing clients. | Therapist |
| ```api/therapist/new-clients``` | GET      |    | will return a list of active clients that are not actively mapped or have pending request from requesting therapist. | Therapist |
| ```api/therapist/new-clients/<id-of-client\>``` | GET      |    | will return a particular client if that client is available for requesting therapist. | Therapist |
| ```api/therapist/new-clients/``` | POST      |  client_id (id of the available client)  | will allow therapists to request clients for mapping. | Therapist |

For more details, refer to docstring of APIs.

#### Pending stories
*   A Client should be able to …   
    *   Approve or reject a therapist’s request for access to Client emotions journal.
    *   Client should be able to accept or reject mapping requests from therapists.
    *   Request for an appointment in an available slot
    *   Run keyword search across Therapists’ notes and emotions journals.
*   A Therapist should be able to …
    *   Approve or Reject session request from clients.
    *   Create a new session (therapy appointment). Each session with –
        *   Private notes, visible only to the therapist
        *   Shared notes with the client. For any assignments. 
    *   Request a new client for journal access. 
    *   Modify details of each session
    *   Run keyword search across customers, notes and emotions journals. 