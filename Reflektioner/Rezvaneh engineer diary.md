Engineering Diary
Projeckt name: BurgerOrder 
Team : Masumeh, Fatema, Rezvanhe 

We began our first project on collaboration and configuration management. We chose Git as our version control system and decided to use GitHub as our server. Forming our development team, which includes Masumeh, Fatemeh, and Rezvan, helped us plan how to work together effectively.
For example, it was great with GitHub. which is a parallel version of our respository(repo). It is a copy where you can make changes without affecting the main project. This is when you want to develop new features or fix bugs without having to mess up the version of your project. 
When you are done with your changes in an industry, you can merge it back to the main industry, often called main/master.
we learned how to create a new repository. Pull requests: If you're working with others, you can use pull requests to suggest changes and discuss them before merging them with the main code.
Issues: You can also use GitHub Issues to track bugs or new features


Our team agreed to use VSCode for coding. While it’s not necessary for everyone to use the same tool, it helps us collaborate better. After creating our GitHub repository, we gave it a meaningful name to keep everything organized.

In the "Planning" folder, we brainstormed menu items like burgers, drinks, and sides. We divided the work, and I focused on the side deshe. I made my first commit by documenting my work on the side dishes. Each of us wrote in our own text files and then exchanged them to contribute to each other's sections.

We set up a virtual environment (venv) to keep our dependencies separate and avoid conflicts later. Additionally, we started working with Docker by creating a Dockerfile for our BurgerOrderer project. I documented the steps to build and run our Docker containers, which is crucial for our team's efficiency.

During our discussions, we focused on the MenuStore database, listing the information each menu item needs, such as name, ingredients, and price. We began coding the web interface to display our menu items. Although we faced challenges setting up Flask for our application, we managed to create a basic server that listens for connections and displays the homepage correctly.

Debugging was an important part of our process. We identified and fixed various bugs, which deepened our understanding of the code. We aimed to add a feature for customizable toppings on the burgers. Ensuring this feature was user-friendly proved to be a challenge, but we successfully created an interactive experience for users.

Throughout this journey, we encountered several challenges. Learning Git felt complicated at first. We struggled with understanding previous commits, which sometimes led us to make changes that caused issues. This taught us the importance of reviewing our commits carefully.

Working as a group was tough since we all had limited experience with programming and databases. As the project grew, it became harder to keep track of everything, highlighting the importance of communication and coordination among team members.

We learned to use Git add strategically, choosing files carefully with git add <filename> instead of git add .. This helps us include only relevant changes in each commit, minimizing unwanted modifications in our history.

Managing branches became essential. We worked in separate branches for different features and fixes, allowing us to experiment without affecting the stable version of our code. When we were satisfied with a feature, merging it back to the main branch was straightforward.

However, we ran into merge conflicts when trying to merge changes from different branches, which led to some frustration. We learned to use commands like git status and git diff to understand the conflicts better. This experience improved our problem-solving skills.

We continue to update our engineering diary with what we learn about configuration management. This practice helps us track our progress and reflect on our experiences.

Overall, this has been an intense but instructive period. We faced many challenges and learned important lessons about Git, collaboration, and problem-solving. I look forward to applying our insights and continuing to grow as a team!

Challenges
We ran into some merge conflict issues when trying to merge changes from different branches. This led to some frustration, but we learned to use git status and git diff to understand what was causing the conflicts. It was a good exercise in dealing with difficult situations. 

Difficulties in the Project
Complexity in Git and GitHub:

Many of us were new to Git, which made it difficult to understand how to handle commits, branches and merges. Sometimes misunderstandings about how to use the tool led us to make changes that caused conflicts in the code.
Difficulty with Group Communication:

Since we all had different levels of experience and knowledge, it was difficult to keep everyone informed of what was being done. This led to confusion about who was responsible for what and caused us to sometimes double work.
Unclear Planning:

Our initial planning was not detailed enough. Without a clear timeline and specific tasks, we often felt lost, which resulted in us falling behind schedule and having to rush solutions.
Problems with Troubleshooting:

When we encountered bugs in the code, it was sometimes difficult to trace back and understand why the problems occurred. This required a lot of time and patience, and we often felt that we were standing still in development.
Database and Backend Integration:

Connecting our database to the application was more complicated than we expected. We had problems retrieving and displaying data correctly, which made it difficult to get our application to work as we wanted.
Time management:

We had difficulty allocating enough time for each part of the project. It became a challenge to balance work with studies and other commitments, which affected our productivity.
Documentation:

We often forgot to document our progress and decisions. This made it difficult to keep track of what we had done and what solutions we had implemented, leading to unnecessary confusion later in the project.
Reflection
These difficulties were educational and helped us grow both individually and as a team. We learned the importance of communication, planning and being flexible in our way of working. Overcoming these challenges has made us more coordinated and knowledgeable, which we can take with us to future projects

To identify any issues with retrieving or displaying menu items from the database, I set breakpoints at key location in the code:
- At the database connection code to confirm that the database opens correctly.
- In the SQL query that retrieves menu items to ensure that correct data is fetched.
- At the part of the code where the menu items are displayed to the user to verify that the data from the database is passed to the application as expected.

These breakpoints are set in the file menyskapare.py as this file handles the database interactions and menu retrieval. 
