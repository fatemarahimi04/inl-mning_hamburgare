My Engineering Diary: "BurgerOrderer" Project

Team Members: Fatema, Rezvaneh, Masumeh

Objective:
The objective of the BurgerOrderer project was to develop a complete system for ordering burgers, integrating both a customer-facing web application for placing orders and a kitchen client for managing those orders. This setup aimed to streamline the ordering process while allowing kitchen staff to efficiently handle incoming requests.

Week 1: Initial Setup and Team Formation

During the first week, our focus was on setting up the project environment and dividing responsibilities among the team. We created a virtual environment (venv) to isolate dependencies, which helped ensure a smooth development process without conflicts. After discussing different tools, we decided to use Visual Studio Code as our integrated development environment (IDE) due to its simplicity and versatility.

We then created the core file, app.py, and found an HTML template for the homepage. Customizing the header and footer (pink and black) was an early step in defining our project's visual identity. Each team member also took ownership of a specific part of the menu:

Fatema: Hamburgers
Rezvaneh: Sides
Masumeh (my role): Drinks
Version control was handled using Git, where we created a repository to store our code and track changes. Basic Git commands like git init, git clone, and git status were used frequently to monitor updates and ensure all members stayed in sync.

Week 2: Database Structure and Implementation

The second week marked a shift to development. We worked on designing the database, creating an Entity-Relationship Diagram (ERD) to visualize relationships between entities like burgers, sides, drinks, and orders. This provided a clear structure for how the application would manage its data.

We also began implementing Docker to containerize our project, ensuring consistency across all development environments. Setting up Docker presented a steep learning curve for some of the team, but after organizing a few sessions to explain the concepts, we overcame the initial challenges. Communication was crucial in this phase, as we relied on Slack and Zoom for daily updates and solving issues as they arose.

Week 3: Drink Menu Development and Testing

My primary responsibility was developing the drinks menu. I aimed to create a user-friendly interface with HTML and CSS, ensuring customers could easily browse drink options. Each drink was displayed with a description and price, and I made sure the interface aligned with the broader design of the application.

On the backend, I worked to ensure dynamic updates, meaning that any changes to the drink offerings would automatically reflect on the user interface. This involved connecting the menu to the database, a process that required close collaboration with Rezvaneh, who was developing the sides menu. We focused on ensuring the menus worked smoothly together for a seamless customer experience.

Integrating the drinks menu with the backend brought several challenges, particularly in retrieving data accurately from the database. Debugging was a slow but ultimately successful process, and through teamwork, we resolved the issues to get the menu functioning correctly.

Reflections:

Collaboration:
One of the biggest lessons we learned was the importance of communication. While each team member had their own task, coordination between different parts of the system was key. Miscommunication caused delays and confusion, especially during merges, where code from different branches conflicted.

Version Control Challenges:
A significant obstacle arose when we tried to merge branches. Unfortunately, the project stopped working entirely. We made the difficult decision to restart the project, which allowed us to clean up the structure, but it also delayed progress. This experience reinforced the importance of regular backups and clear coordination during merges.

Technical Insights:
On a personal level, I found working with HTML and CSS to be one of the more enjoyable aspects of the project. However, despite the potential for a polished design, we didn’t have enough time to fine-tune the interface due to the merge issues.

Team Dynamics:
As the project moved forward, it became clear that there was a lack of strong collaboration. There were moments of frustration and misalignment in the team. I found myself stepping back at times to allow Fatema to handle critical parts of the project as the pressure mounted. This meant that, unfortunately, I didn’t contribute as much to commits toward the end. The setbacks caused anxiety within the team, and it became challenging to regain momentum.

Conclusion:

Despite the challenges, my work on the drinks menu provided valuable lessons in both technical skills and teamwork. The drinks menu is a key component of the BurgerOrderer project, offering a variety of drink options to complement our food offerings. Moving forward, I aim to focus more on fostering collaboration within the team and ensuring that everyone is equally engaged throughout the project.

We also encountered various technical problems, such as module installation errors and inconsistencies with the Flask application. To address issues with the kitchen view, we had to change the Flask port to 5001 to resolve the problem with displaying the webpage.

Though the project faced setbacks, the experience has taught us to better manage version control, communication, and backup processes for future group work.
