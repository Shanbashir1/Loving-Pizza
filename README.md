# Project 3 - Loving Pizza - A Ordering system for a Pizza Shop to its users.

###  For my third project with Code Institue, I will a create a Pizza ordering system using PYTHON. 
[View link to my project 3](https://loving-pizzas.herokuapp.com/)

## Introduction
Loving Pizza is a small family run pizza shop located in the UK, London. 
The owners who have been operating the pizza shop for some time now, realise that something is missing and that technology play's a big part of the upcoming future. The owners would like the user/customer to order its pizza using its ordering system when visiting the shop or order online via an app. The owners have asked to see a online ordering system and how data will be reverted back to the kitchen staff so they are made aware of what and who has ordered. Ideally I have tried to keep a simple basic system where the pizza shop are made aware of the customer name and address and pizza requirements. The customer is then charged for his pizza. In future the owners could look at a more detailed and advance systems which offers more services and deals. 

<img src="/readme-images/main.png" alt = "Main Page" style="height: 500px; width: 800px;">

## Design and Planning
+ Initially I was try to plan for a quiz game but I felt as I had done this with Javascript, I had to broaden my skills and my then plan was a ordering system. 
+ At the time of my plan I was actually in receipt of a Pizza menu and so decided I could create a simple ordering system, which allows the user to order a pizza. 
+ My intial design was to start off with a login screen. However I started created a format for data to be transferred from a CSV, just like the Love Sandwich project. 
+ As I continued creating my design on the worksheets, i linked all my data sheets to my program. 
+ In the process I started to code which diverted me off the login design. I had to make alot of changes, the coding did not always give me the outcome i expected, and I had to go searching for answers via tutor support and the internet. 
+ After linking my design I decided to create a chart on Lucida chart to get a overall structure of my project. 
<img src="/readme-images/lucida.pdf" alt = "Lucida Chart" style="height: 500px; width: 700px;">

 
## User Stories
+ As a first time user I will need to know how and when to answer the prompt request 
+ As a user I would need know what options I have for ordering, i.e Pizza Type, Pizza, Additonal Toppings, etc 
+ As a user I would need to be made aware of how many slices each size pizza contains. 
+ As a user I would need to be introduced using my name and have a welcome message 
+ As a user I would need to have a easy user interface and a responsive process 
+ As a user I would like to know what I have ordered and be shown a receipt of my selected items 

## Admin Stories 
+ As a admin I will need to give the user options as to what they would like to order. 
+ As a admin I would need to have a full data of customer order details 
+ As a admin I would need to have customer delivery address 
+ As a admin I would need to be able to check cost with pizza ordered. 
+ As a admin I would need to manage the data which has been reverted back to the worksheet.


## Features 
### API - Worksheet CSV
+ Linking my worksheet to my program 
+ Data to be added and tranferred from the worksheet, once the user has selected its choice. 
+ User information stored into the worksheet 
#### Information collected from the worksheet
<img src="/readme-images/love-pizza.png" alt = "Loving Pizza Data sheet" style="height: 500px; width: 700px;">

#### Data sent back to the worksheet and stored a customer order sheet
<img src="/readme-images/order-info1.png" alt = "Customer order info" style="height: 500px; width: 700px;">
<img src="/readme-images/order-info2.png" alt = "Customer order info" style="height: 500px; width: 700px;">

### Art - Header 
+ The user is introduced to the ordering system with the text "Welcome to Loving Pizza"
+ The text is a feature of art, which has been imported into Python. 
+ The art feature makes the header pretty to view and gives the user a warm welcome. 
+ The art feature gives the header a professional look. 

### Customer Name options 
+ The user will need to add his firstname and surname to commence the ordering process
+ The user is greeted with the a Welcome message and furthermore is greeted with the customer name
+ The customer name is then repeated in the print order and a thank mesage is also displayed 
+ The customer name feature assures the user of a safe ordering enviroment. 
+ The user is also felt warm and welcoming by having this feature. 
+ <img src="/readme-images/names-option.png" alt = "Enter Name Section" style="height: 500px; width: 600px;">

### Address
+ The user will be required to enter his/her address in so this information can be recorded to the data worksheet.
+ The address will be used for the Pizza shop to gather information for delivering the Pizza. 
+ The user will be displayed his/her address in the Print order feature. 
+ <img src="/readme-images/address-option.png" alt = "Enter Address Section" style="height: 300px; width: 600px;">


### Pizza Size Option Menu
+ The user is given 4 size options 
+ The user is prompted to select the option which are displayed on the screen. 
+ The user is displayed the options in a table format called PrettyTable. 
+ Pretty tables gives the table a professional and well organised look to the enclosed data. 
+ The user is asked to select a option using the correct numbers assigned 1,2,3,4.
+ Once the user has selected the size, the output message is displayed, i.e "You selected SMALL, approx 3-4 slices
+ if a value which is not between 1 & 4 has been selected then the user will be requested to re-enter the value. A error message in the color format red will be displayed. 
+ <img src="/readme-images/size-option.png" alt = "Enter Pizza Size" style="height: 500px; width: 600px;">

### Pizza Pan Option
+ The user is requested to select 3 options to determmine the type of Pan it requires its pizza to be cooked in. 
+ The user will be prompted to select either 1,2,3.
+ Once selected the user will be displayed the following "The pizza you chose: (answer)"
+ if a value which is not between 1 & 3 has been selected then the user will be requested to re-enter the value. A error message in the color format red will be displayed. 
+ <img src="/readme-images/pan-option.png" alt = "Enter Type of Pan" style="height: 500px; width: 600px;">

### Required Pizza Option Menu 
+ The pizza option menu gives the user a list of pizza they would like to order. 
+ The pizza are listed between 1 to 6 and the user is requested to select them based on their preference. 
+ Once selected the user will be displayed the following "The pizza you chose: (answer)"
+ if a value which is not between 1 & 6 has been selected then the user will be requested to re-enter the value. A error message in the color format red will be displayed.
+ <img src="/readme-images/pizza-option.png" alt = "Enter Pizza Type" style="height: 500px; width: 700px;">

### Additional Toppings 
+ The additional toppings gives the user a list of toppings they would like to add to their order. 
+ The toppings are listed between 1 to 6 and the user is requested to select them based on their preference. 
+ Once selected the user will be displayed the following "Additonal Toppings added: (answer)"
+ if a value which is not between 1 & 6 has been selected then the user will be requested to re-enter the value. A error message in the color format red will be displayed.
+ <img src="/readme-images/topping.option.png" alt = "Enter any additional topping" style="height: 500px; width: 700px;">

### Calculate Price 
+ The user will be displayed a calculating price, the price will be from the pizza sizes. 
+ The user will be made aware of the pizza cost. 
+ <img src="/readme-images/calculate-option.png" alt = "Calculating Price" style="height: 200px; width: 400px;">

### Printing Receipt 
+ The user will be in receipt of a order confirmation 
+ Date, Time, Customer Name, address, Pizza details and cost will all be displayed on the receipt
+ A transaction id number is entered randomly with every order, this order can be checked with each order and is a unique feature for the user.
+ A "Thank you" message will be displayed on the receipt. 
+ <img src="/readme-images/receipt-option.png" alt = "Prints receiept" style="height: 500px; width: 700px;">

### Exiting Option 
+ System prints receipt, gives a user a thank you message and exits terminal 
+ <img src="/readme-images/exit-option.png" alt = "Calculating Price" style="height: 200px; width: 400px;">

## Future Features 
The project could benefit from a vast ranage of features which could be implemented for future use. I have highlighted some of the proposed features below;
+ Login & Register, a option which I was intrested in adapting into my project. However I felt I spent to much time in actually creating the ordering system that I overlooked this facility. Obviously with more time and better organising this facility was a must. The user also gets a secure and better security when ordering. 
+ Card payment facility - a must option with any type of ordering process. However a facility which have not covered yet, so hence I did not add any payment facility. 
+ A order tracking facility would be good for the shop to introduce so the user can determine the progress of its order. 
+ Uploaded to HTML & CSS - for a better design and look. 

 ## Color Scheme
+ As my design was not imported to any HTML and CSS, the only color facility which was used was  the color of text display, this was mainly blue or white, with error messages being displayed in red. 
+ The color format was imported from coloroma and then used using the Fore: (BLUE) option depending on what color feature was required. 
+ I tried to keep the text color consistent throughout the project. 
+ The question text color was Blue.
+ The input data text color was White.
+ Error and unvalid commands was Red.
+ Information text were in Green.

## Font Display
+ Standard fonts were used throughout the project. 
+ Art was used to display the headers 

## Technology Used
For my thrid project Python I the following technologies were used to complete my 
### Languages Used 
1. **Python** was used the main programming language used for my project. It was widley used throughout my project. 
### Hosting Service
**GITHUB** was used to create, host the web design on to the platform. The benefit of github was to create repositories, branches, commits, and pull requests. Github was also a great way to share your design to mentors and other colleagues and tutors to help view your code and seek further input and support.
### IDE
**GITPOD** allows you to define your project's configuration in code so you can launch a prebuilt development environment with one click.(Source Google) Gitpod was used to code all my Python coding.
### 
**Heroku**  was used to load my project and deploy it, This was my first time deploying a on Heroku and I found it quite simple. 

### Others 
+ Pep8 Online check - used to check oevr my codes for faults and issues. 
+ Stack overflow - for help with issues. 
+ W3Schools - assits with coding issues.
+ Slack - support from colleagues 
+ Code Institue Tutor Support -Programming help and support. 


## Testing - Python
+ PEP8 online check - A online free aplication which check python code for errors and warnings. 
+ So with my initial checks I had quite a few errors, mainly the E501 error code, prompting me that the line lenght was too big, I had to do lots of research to determine how I could break down these lines without effecting my code. I managed to find out and used the \ to break down the code. I was discovered I could use () parenthesis to wrap the code. 
+ The errors and warning were rectified before deploying my projects  
+ My final online check code returned back with no errors or warnings. 
<img src="/readme-images/pep_8.png" alt = "Pep8 Online Check" style="height: 600px; width: 800px;">


## Test Cases
1. **Introduction Header to the Loving Pizza** The user starts the program with a "Welcome to Loving Pizza" message, which is displayed using a special art format. 


2. **Customer Names** The user is prompted to enter his firstname and then once entered (considering no errors or invalid inputs) the user is prompted to enter his surname, again with the same error message if input entered is invalid 
3. **Address** The user will be asked to enter his address, 

4. **Progress through the ordering system** 
+ The user will be asked to select the pizza size he/her requires. Once selected the message will return as the selected item. 
+ The user will be asked to select the pan type he/her requires. Once selected the message will return as the selected item.
+ The user will be asked to select the pizza he/her requires. Once selected the message will return as the selected item. 
+ The user will be asked to select any additional toppings he/her requires. Once selected the message will return as the selected item.

5. **Calculating Prices** 
+ The system will calculate the price, The prices were defined according to the Pizza sizes and return the value of the customer choice.

6. **Printing Recipt** 
+ The customer is displayed with a receipt, Every order placed a order number is present, using the random feature which calculates random numbers. 
+ Date and Time are also displayed on the receipt. 
+ Customer First and Surname
+ Address 
+ Order details, information extracted from the customer choice inputs. 
+ Price 
+ Thank you message 

7. Exiting system, Thank you message and see you back soon. 

## Fixed Bugs
+ After doing my initial check via Pep 8 online checker I had quite a few errors and warnings. All of minor nature and could easily be fixed, i.e spacing and sentences too long errors. Once these had been ammended my code had no faults and errors. 
<img src = "/readme>

## Unfixed Bugs
There was no unfixed bugs by the time this was written.

## Deployment
### GITHUB
+ To deploy pages to Github the following steps were taken.

+ Login into your GITHUB account if you do not have one, you will need to create one
+ Find Repository button and open page
+ Locate the setting button and then locate the pages button.
+ You will then need to click the source button, on the tab labelled "none" select "main"
+ Once "main" has been selected the page will start to deploy, this will take a few minutes to deploy.
+ Once the link turns green, your link will be deployed.

### GITPOD
+ Some useful feature and pathways to note for Gitpod are as follows open pre-design of webpage(browser) "python3 -m http.server".
+ To save work git add .
+ To commit git commit -m TYPE MESSAGE i.e "added image to front page"
push your work to GITHUB repositories git push.

## Credits
A list of my credits are below

+ Code Institue Learning guide and past coding examples
+ Love Sandwich Tutorial
+ Bro Code = youtube video "Python"
+ Web Dev Simplified - tips on creating apps using JavaScript 
+ Coding with Nick - Help on creating workable functions. 
+ W3schools.com - Help with CSS coding
+ stackoverflow.com - help with coding, by visiting past forums.
+ Slack - support from colleagues and mentors 


## Acknowledgement

+ My mentor Rohit Sharma @rohit_mentor - Great advice and support throughout my project journey, I was guided well with plenty of advise and support.
+ Tutor Suport - So much help from a wide diversity of tutors. They were able to support me in good time and made me realise when things became difficult.
+ Slack - Always so much help from colleagues, the level of support is undoubtedly amazing.