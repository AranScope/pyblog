# ServiceNow Bootcamp
## Intro
ServiceNow is a enterprise IT system for managing of services, facilities and resources within corporate companies. From the 6th-10th June, 2016 I participated in ServiceNow's University of Birmingam bootcamp week.

## Getting Started
During Monday to Wednesday of the week we were taught the very basics of the platform. Starting with creating basic databases and tables and moving onto the creation of simple forms and applications to interact with these tables. This concluded in a session using Jellyscript which is near identical to Javascript but designed to be safer in terms of potentially dangerous modifications and changes. 

## G2G3 Challenge
Immediately following the taught sessions we participated in Polestar, A business simulation created by G2G3. In the simulation, we had a set of systems (servers, routers etc.) that we had to maintain, this was all to facilitate the running of 5 companies. At differnet stages our servers and networking equipment would encounter faults which would require technical manuals and solving mathematical and logical problems. The simulation consisted of 3 rounds:

> **Round 1 - Submarine**<br>
> In the first round we consistently experienced catastrophic failure of our network, this resulted in our technical team panicking and taking a long time to fix these problems. With the huge downtime for online sales we lost $5M over the course of the round.

> **Round 2 - Sinking Ship**<br>
> Here we started developing strategy between the sub-teams of the Company. We would pre-solve problems in case they came up and introduced redundancies for our servers to deal with the failure cases. This however, was not enough. 

> **Round 3 - Wait, it's actually working?**<br>
> This was where we were taught tangible business lessons that I'm sure will be useful in the future. Most evident was the idea of preventing problems from occuring as early in the heirarchy as possible. In this case, the service desk (front line) began keeping a log of all answered questions, eventually having a log of at least half of all inbound questions. This meant the technical team we're free to work on difficult, new problems instead of having to waste time with problems that had previously been sold.<br><br>We also introduced a role in the technical team of 'service desk liason', communication between the teams resulted in the mitigation of errors for both teams meaning we did not have to introduce time expensive changes at later stages.

## The Hackathon 
As has become evident over the last year, Hackathons are the staple of innovation in the academic Computer Science community. This has started leaking more into the corporate world and is fortunately being shared back with the community through collaborations such as the ServiceNow bootcamp at the University of Birmingham.<br><br>At the start of the hack we we're allocated into teams of 5 and given the option of ~4 briefs, one of which giving creative freedom to the team. We, of course, chose the creative freedom option. Our initial idea in a few words was 'Distribute incident updates only to those concerned', what this boils down to can be summed up with the following example.
> "Picture a Lecturer in the school of Computer Science, we know they are working Mon-Fri, 9-5pm. A typical work week. They teach in lecture theatres in the school of Biosciences and they conduct research in the school of Psychology. Clearly they don't need to be updated about a power cut in the Arts building or an overly enthusiastic student stealing from the music building canteen. Perhaps they would be more interested in internet downtime in floors 1-2 of the Computer Science building."

Our solution to this problem involved multiple systems:
> * A **NodeJS** server, featuring a login and interest selection page. Used to send personal data to ServiceNow and receive incident logs using a REST API. These incidents are then displayed using AngularJS as a single page web app.

> * The **ServiceNow** database, this is a relational database keeping records of users (staff and students), incidents etc. Essentially a profile of our users and logged incidents.

> * The **Bayesian classifier** script, also hosted on ServiceNow, this took in data regarding our user and returned the result of a query to the incidents table i.e. All of the important incidents for a given user.

## Conclusion
The ServiceNow bootcamp taught me an important lesson about where my interests lie, I am personally more interested in working on small, intimate projects. The projects I have talked about in the past, working in teams of 4, having full control over the project have been much more satisfying for me.

ServiceNow affords you a great deal of safety and speed with practice, it is difficult to deal any major damage to a project, quick to get something up and running but it is also difficult to feel a sense of full ownership over a project, as so much is abstracted away from the developer. 