Names of everyone in the team:
Fatema, Masumeh, and Rezvaneh
Link to serve:
https://github.com/fatemarahimi04/inl-mning_hamburgare.git 

For testing and debugging, we focused on checking the functionality of the burger ordering system, ensuring customers could view burgers, prices, ingredients, and remove items from their orders. This involved testing the connection between the orderer and kitchen views to confirm orders were sent and received correctly. Additionally, we addressed issues with our database setup, fixing errors in the Dockerfiles to ensure smooth system operation.
Variable Monitoring in Debugger
To track changes in key variables, I added items to the variable watch in the debugger. This allowed me to see when its value changed after executing an SQL query, confirming that it retrieved accurate data. Here’s what I observed:
-Initial Value: items was None before the SQL query executed.
-After SQL Query: items correctly updated to contain five items: a bacon burger, a chicken burger, a veggie burger, fries, and a drink.
If items had contained fewer than five items, it would have pointed to a potential database query issue. I monitored the items variable to ensure it fetched the correct data.
Scenario Testing
I conducted several scenario tests to verify that the system behaved as expected:
1.	Ordering Different Menu Items: I tested different menu selections to ensure correct information retrieval.
2.	Cancelling an Order Mid-Way: I tested cancelling an order halfway through to check variable handling and database connection management.
In different scenarios, depending on the menu item selected, different objects were retrieved, updating items accordingly. If an order was cancelled, no information was saved, and the database connection was closed as expected. This validated that item updated correctly based on the selected item and the database connection persisted until the application exited.
Initial Approach and Adjustments
Originally, we aimed to implement a feature where customers could remove specific ingredients from their burgers through a dynamic menu. This approach required JavaScript, which we found too complex for our familiarity level. We revised our approach, listing ingredients next to each item with checkboxes, so customers could simply uncheck unwanted ingredients. This alternative was both simpler and more efficient.
The list of ingredients was retrieved from the database and submitted via the POST method to the kitchen view. We created a basic HTML setup for testing, prioritizing functionality over visualization as instructed in the assignment. To avoid port conflicts, we assigned port 5000 to the burger orderer and port 5001 to the kitchen view. This became necessary after attempting to run both applications on port 5000, which caused conflicts.
Application Testing
In the burger and kitchen applications, we ensured core functionality worked as expected, using modules like json to format data and app from both app and app_kitchen to initiate the Flask test clients. These test clients allowed us to simulate HTTP requests in a controlled environment, verifying system behaviour.
To structure our tests in the kitchen application, we used the unittest module, creating a KitchenViewTestCase test class. Within this class, the setUp () method initialized the test client before each test, isolating each function test.
We then used POST and GET requests to interact with various API endpoints:
For the burger application’s / endpoint:
o	In test_index_get, we tested the home page’s accessibility, verifying it responded with status code 200.
o	In test_order_post, we sent a JSON order with burger details (name, price, and excluded ingredients) and checked that the server returned a 200-status code and a confirmation message, "Order sent successfully!"
For the kitchen application’s /order endpoint:
-In test_receive_order, we sent a POST order and verified a 200-status code.
-In test_invalid_method, we confirmed that a GET request to /order returned a 405-status code (Method Not Allowed), ensuring it accepted only POST requests.
Through these tests, we confirmed the applications correctly handled orders and method restrictions. All requests returned expected responses, and the applications managed incorrect methods (like GET on /order), providing appropriate feedback. We also encountered minor issues, such as the terminal freezing or receiving “no module found” errors despite module installation. Restarting VS Code resolved these issues.
In summary, our testing and debugging confirmed that even small code changes in one file could significantly impact other files, emphasizing the importance of understanding interconnections within our setup.
