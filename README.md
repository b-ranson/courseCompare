# COURSECOMPARE

### Problem To Solve

We want to implement a way for FSU Students to be able to view and compare their schedule to their peers. We also have included a review system for courses so students can view and prepare for future classes based on reviews. This project is a spin off of RateMyProfessor with a social media aspect and basing the site more on courses rather than professors.

### Extra UI Details to Know
- N/A. The site should be self-explanatory to browse and interact with. All input areas have guides/examples on expected input.
### Libraries Being Used
- Django framework
- MySQL
### Other Resources
- N/A
### Extra Features Implemented Beyond Proposal
- We added the professor rating option from our optional ideas in our proposal to our project, as it was relatively simple
to implement.
### Features From Proposal We Did Not Implement
-  We did not add any functionality to see aspects like grade weight or GPA for in-class assignments as this
varies too much from class to class and would be challenging to implement in a scalable way. We also elected to
make every account on our platorm be viewable by other users instead of implementing a graph-based friends list.
### Separation of Work
- Aiden - Front End
    - Implemented static HTML pages and styled them using CSS. Also implemented dynamic information passing using JINJA
      when interacting with the backend.
- Blaine - Distribution / Front End
    - Wrote static HTML pages and styled them using CSS. Also wrote the paper describing how we would implement
      distribution for our project.
- Branson - Back End / Security
    - Implemented the routing, input validation, and login/site-viewing security using the Django framework and expanding
      its built in functions to align with the project's needs. 
- Josh - Databases / RBAC
    - Implemented and populated a MySQL database that was accessed by the project server to display queried information.
      Also added Role-Based Access functionality to prevent "paid-user only" pages from being seen by basic users, along
      with preventing admin pages from being seen from anyone other than admins.