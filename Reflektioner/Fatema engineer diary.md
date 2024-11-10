I started by setting up a virtual environment (venv) to avoid conflicts with my global environment.

I also created app.py. I found a free HTML template to visualize the homepage.

Then, I modified the header and footer (changed them to pink and black).

I began organizing my files based on my thought process to fill them in with code later, depending on what I needed.

I used some basic Git commands, such as git init, which created a new repository, git clone to clone my files and folders from GitHub to VSCode, and git status, which shows changes that have been made but not committed. I used push and pull frequently to send my commits.

One significant conflict in our project occurred when we tried to test a merge and realized that, for some strange reason, the project completely stopped working. The idea was to merge changes from one branch to another, but it ended in disaster, resulting in a lot of extra work, like restarting the project from scratch. However, this also turned out better because I could "clean up and discard" the unnecessary parts and organize everything nicely, so I knew what was in different folders.

The difficulties we encountered were mostly related to collaboration within the group. We all had little knowledge of programming and databases, making it quite a heavy task for the three of us. Given that we had to redo most of the database, burger order, and kitchen view due to issues with merges in the previous project, this became a significant lesson for us to always keep a backup of everything so that it doesn’t just vanish into thin air.

Now, this project turned out very poorly because it doesn't show much collaboration, and it looks like I did everything myself. However, if you look at the previous project, there are commits from all three members of the group. Next time, I will make sure to organize folders, files, and code so I don’t just write a lot of random stuff, and I will also read up before trying any commands or functions.

I encountered errors that said 'no module found' even though I had the module installed. I realized that my computer or the VS Code environment itself might need to be restarted.

I had trouble opening the webpage because I got an address to go to, but I realized that it’s not possible to open both webpages with the same address. So, I changed the Flask port for the kitchen view to 5001 to get a new address.

I created a new file named burger_test.py and test_kitchenview.py there I'll write my codes.

I used unittest and Flask's test client to sent request to my endpoints and controlled that it anwsered correctly.
 
 I checked if the application returned the correct  HTTP status codes.

My test did'n work because it returned "no module named flask", I checked burger_test.py file which URL is used in the test for the POST request. It should match the URL in the application that handles orders.

We tested run pip show flask and it says that flask is installed but wee tried to install again with pip install flask. 

We ran the code and now it returned HTTP-stauscode 404 (not found) instead of 200 (OK). 

In the test, a POST request is sent to /order. This route exists in app.py and wee have set up a POST method for /order. 

After running the code we got another error, we tried to import app from app_kitchen and python cannot perform this import.

I took the reponsibility of the third and fourth step of the debug-session...
To track data flow and ensure everything works correctly, I monitored the following vvariables:
- conn: ensures that the database connection opens correctly.
- items: this variable stores the menu items retrieved from database and I check that it has the expected values after the SQL query runs. At this point in the code, items shoukd contain five entries matching the manu items added to the database.

To monitor items I added it to the variable watch in the debugger. I can see when the value changes after the SQL query runs, ensuring that it retrieves the correct data.

Variable Monitoring Results
- Intial Value: items is None before the SQL query is executed.
- After SQL Query: items contains five items as expected: a bacon burger, a chicken burger, a veggie burger, fries and a drink. 

I observed when the value of items changed and verified that it fetched the correct data. If items had fewer that five items it would indicate an issue with the database query.

I t
