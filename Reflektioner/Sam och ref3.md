Names of everyone in the team:
Fatema, Masumeh, and Rezvaneh
Link to serve:
https://github.com/fatemarahimi04/inl-mning_hamburgare.git 

For testing and debugging, we focused on checking the functionality of the burger ordering system. This included verifying that the customer can view burgers, prices and ingredients as well as remove items from their order. We also tested the connection between the orderer and the kitchen view to ensure orders were properly sent and received. Additionally, we worked on debugging issues with our database setup and fixed errors in the Dockerfiles to ensure the system worked smoothly.
The first idea was to test opening a menu where the customer could choose to remove ingredients they didn´t want from the item. This was a bit too advanced for us because it required JavaScript and we weren´t very familiar with it. We changed our approach to something simpler and more efficient. The simpler idea was to list ingredients next to each item using checkboxes, allowing the customer to uncheck the ingredients they didn´t want. I retrieved the list of ingredients from my database. I sent the information in a form using the POST method to the kitchen view. For testing, I wrote a simple HTML code just to make it work, as the assignment mentioned that functionality was more important than visualization.
Flask uses port 5000 and to avoid conflicts, I assigned port 5000 to the burger orderer and port 5001 to the kitchen view. I did this to have two web pages I could work on. I realized this when I tried running both the burger orderer and kitchen view in port 5000, which didn´t work. Sometimes, when I ran too many things in the terminal it froze and stopped working and the easy solution was to restart VS code. An example is that I had the module installed in my environment, ye I still received a “no module found” error, even though it was installed. 
We learned a big lesson that even the smallest change in one file can have a significant impact on other parts of the code in different files. 