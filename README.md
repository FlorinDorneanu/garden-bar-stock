# Garden Bar Stock
## Project Portofolio Three
At the Garden Bar the stock was made using the classic pen and paper tool. The bar's popularity increased so it became very unhandy and a waste of time to continue like that. The stuff couldn't handle making the stock anymore and so this command-line aplication was created for helping staff to save time and to be more precise with the bar's inventory.

The live project can be viewed here - [Garden Bar Stock](https://garden-bar-stock.herokuapp.com/)

The GitHub repository can be viewed here - [FlorinDorneanu/garden-bar-stock](https://github.com/FlorinDorneanu/garden-bar-stock)
***

## User Experience (UX)

### Strategy
* The application will provide a easier way to calculate the stock and revenue data.
* When created the application the initial stock will be already stored in google spreadsheet.
* The application will request the user to input entries data.
* Adding initial stock to entries data, the total stock will be calculated.
* The application will request the user to input sales data.
* Substract sales from total stock data, the final stock will be calculated.
* The data from final stock will be imported to initial stock data so it can be used for the next day calculation.
* The prices for each drink will be provided in the spreadsheet.
* Multiplying sales with drinks prices the revenue for the day will be calculated.
***

### User Stories
As an employee I expect to:
* Easily access the application.
* Enter the data without any difficulties.
* Be informed if my data is not valid.
* To re-enter data until is provided correctly without having to restart the application.
* Retrieve data from google spreadsheet.
* Be able to calculate the total and final stock with ease.
* Access the drinks prices from google spreadsheet in case of a possible price change.
* Be able to calculate the daily revenue.

As the employer I expect to:
* Be able to access all the data that my employees enter.
* Have all the data stored for monthly income calculation.
* To be easily informed about the daily revenue.
***

### Structure
* The user is beeing welcomed to the Garden Bar Stock calculation.
* The aplication request the user to enter the number of bottles per each drink that was introduced in the bar.
* The user is beeing informed on how to enter a valid input.
* The aplication request data from user until the data is valid.
* The user is beeing informed that the data is valid.
* The user is beeing informed that the entries worksheet has been succesfully updated.
* The user is beeing informed that the total stock worksheet has been successfully updated.
* The aplication request the user to enter the current day sales data.
* The user is beeing informed about how to enter a valid input.
* The aplication request data from user until the data is valid.
* The user is beeing informed that the data is valid.
* The user is beeing informed that the sales worksheet has been succesfully updated.
* The user is beeing informed that the final stock worksheet has been successfully updated.
* The user is beeing informed that the initial stock has been updated with the final stock for the current day.
* The user is beeing informed that the revenue is being calculated.
* The user is beeing informed that the revenue worksheet has been succesfully updated.
***

### Sceleton
* The aplication consists of a simple interface that requests only two inputs from the user to calcuate the daily stock and revenue for the bar.

If the user enters an invaid input data, an error will apear informing the user about the mistake that was made and will continue requesting the user to input data until the data is valid.
***

## Features
### Existing Features
* The user is being welcome to Garden Bar Stock calculation.
* The application requests the user to enter the number of bottles for each drink introduced in the bar and informs the user on how to enter a valid data.
![f1](documentation/images/f1.png)
* The user has to enter five digits numbers that are dibisible by 6, separated by commas.
* The application provide an exaple of valid data.
* If the user's input data is invalid then an error message will appear.
![f2](documentation/images/f2.jpg)
* The aplication request the user to re-enter data until the data is valid.
![f3](documentation/images/f3.jpg)
* The user is beeing informed:
  * That the entries are valid.
  * The entries are going to be updated to worksheet.
  * The entries worksheet is successfully updated to worksheet.
  * The total stock is calculated.
  * The total stock is going to be updated to worksheet.
  * The total stock is successfully updated to worksheet.
* The aplication request the user to introduce the current day sales data.
* The input has to be 5 digit numbers separated by commas.
* The application provide an exaple of valid data.
![f4](documentation/images/f4.jpg)
* If the user's input data is invalid then an error message will appear.
* The aplication request the user to re-enter data until the data is valid.
![f5](documentation/images/f5.jpg)
* The user is beeing informed:
  * That the sales are valid.
  * The sales are going to be updated to worksheet.
  * The sales worksheet is successfully updated to worksheet.
  * The final stock is calculated.
  * The final stock is going to be updated to worksheet.
  * The final stock is successfully updated to worksheet.
  * The initial stock is goinng to be updated to worksheet with the final stock data.
  * The revenue is going to be calculated.
  * The revenue is going to be updated to worksheet.
  * The revenue is successfully updated to worksheet.

### Future Features
* Allow the aplication to calculate the monthly and annual total stock and revenue.
* Allow the aplication to calculate the inventory based on the the data provided.
* Allow the aplication to calculate the average of the bottles saled daily.
* Allow the aplication to store the loses products.
***

## Technologies Used
### Languages
[Python v2023.4.0](https://www.python.org/)

### Frameworks, Libraries and Programs
* [Google Spreadsheets](https://en.wikipedia.org/wiki/Google_Sheets): used as the external data store for the Orders and Menu data used by the project.
* [Google Drive API](https://developers.google.com/drive/api/guides/about-sdk): used to generate credentials used in the project to securely access the Google Spreadsheet.
* [Google Sheets API](https://developers.google.com/sheets/api/guides/concepts): used to support interactions (e.g. read/write functionality) between the code and data stored in the Google Spreadsheet.
* [gspread](https://docs.gspread.org/en/latest/): Python API for Google Sheets
* [Google Auth](https://google-auth.readthedocs.io/en/master/): Google authentication library for Python required to use the credentials generated for Google Drive API
* [Git](https://git-scm.com/): was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/): is used as the repository for the project's code after being pushed from Git.
* [Heroku](https://dashboard.heroku.com/): is used to deploy the application and provide an enviroment in which the code can execute.
***

## Testing
### Testing User Stories
| Reference  | Description  |
|---|---|
| 01  | Easily access the application.  |
| Validation  | The user can easily access the application from the link provided.  |
| 02  | Enter the data without any difficulties.  |
| Validation  | The user can enter data with ease due to the example provided. |
| 03  | Be informed if my data is not valid  |
| Validation  | The application shows to the user error messages when data is invalid.  |
| 04  | To re-enter data until is provided correctly without having to restart the application.  |
| Validation  | The user doesn't need to restart the application if the data provided is not valid.  |
| 05  | Retrieve data from google spreadsheet.  |
| Validation  | The user can retrieve data from google spreadsheet without any error.  |
| 06  | Be able to calculate the total and final stock with ease.  |
| Validation  | The user is able to calculate the total and final stock using the application without any error.  |
| 07  | Access the drinks prices from google spreadsheet in case of a possible price change.  |
| Validation  | The user can access the drinks prices from google spreadsheets at any time.  |
| 08  | Be able to calculate the daily revenue.  |
| Validation  | The user is able to calculate the revenue using the application without any error.  |
| 09  | Be able to access all the data that my employees enter.  |
| Validation  | The user is abble to access all the data proided in the Garden Bar Stock spreadsheet.  |
| 10  | Have all the data stored for monthly income calculation.  |
| Validation  | All the data is stored in the Garden Bar Stock spreadsheet.  |
| 11  | To be easily informed about the daily revenue.  |
| Validation  | The user can acces the daily revenue from the Garden Bar Stock spreadsheet.  |
***

### Test Cases and Results
| Test Category  | Steps  | Expected Outcome  | Result  |
|---|---|---|---|
| Run Program  | Run the application  | Welcome message appears. System asks the user to enter the number of bottles entered in the bar. Example is provided.  | Pass  |
| Entries - data checks  | Enter invalid inputs, e.g. bear, empty string, 11.   | Error message apears and ask the user to re-enter a valid input.  | Pass  |
| Entries  | Enter a valid input containing 5 numbers divisible by 6 and separated by commas.  | Confirmation message for valid data appears. Entries worksheet successfull updated, calculating total stock and updated successfully to worksheet. System asks the user to enter the current day sales data. Example of valid data is provided.  | Pass  |
| Entries - update worksheet  | Access google spreadsheet and check the entries worksheet.  | Entries data has been updated to the entries worksheet.  | Pass  |
| Total stock - update worksheet  | Access google spreadsheet and check the total stock worksheet.  | Total stock worksheet has been updated with the data resulted adding entries to initial stock.  | Pass  |
| Sales - data checks  | Enter invalid inputs, e.g. bear, empty string.  | Error message apears and ask the user to re-enter a valid input.  | Pass  |
| Sales  | Enter a valid input containing 5 numbers separated by commas.  | Confirmation message for valid data appears. Sales worksheet successfull updated, calculating final stock and updated successfully to worksheet. Update initial stock with final stock values. Calculate revenue and update to google worksheet. Confirmation message for successfully updated worksheets appears.   | Pass  |
| Sales - update worksheet  | Access google spreadsheet and check the sales worksheet.  | Sales data has been updated to the sales worksheet.  | Pass  |
| Final stock - update worksheet  | Access google spreadsheet and check the final stock worksheet.  | Final stock worksheet has been updated with the result of substracting sales from total stock.  | Pass  |
| Initial stock - update worksheet  | Access google spreadsheet and check the initial stock worksheet.  | Initial stock has been updated with the final stock data provided in the worksheet.  | Pass  |
| Revenue - update worksheet  | Access google spreadsheet and check the revenue worksheet.   | Revenue worksheet has been updated with the data resulted from multiplying sales with drinks prices.  | Pass  |
***

### Validator Testing
* [Python Validator](https://pep8ci.herokuapp.com)
![Python Validator](documentation/images/validator.png)
***

## Bugs
* The first bug showed up when trying to check if the user input for entries data can be divided by 6. When iterating through ```entries``` values, the modulo operation didn’t work. I fixed it by changing the ```bottles``` parameter within the validate_entries function to ```entries``` and by converting ```entry``` strings to integers.
  * Initial code:
  ```
  def validate_entries(bottles):
    """
    Convert all string values into integers,
    Raises ValueError if strings cannot be
    converted into integers, if there aren't
    exactly 5 values, or if the values entered
    cannot be divided by 6.
    """
    try:
        [int(bottle) for bottle in bottles]
        if len(bottles) != 5:
            raise ValueError(
                f"The user must enter exactly 5 values,"
                f" you provided {len(bottles)}"
            )
    except ValueError as e: 
        print(f"Invalid entries: {e}, please try again.\n")

    for bottle in bottles:
        if bottle % 6 != 0:
            print(f"{bottle} is not divisible by 6")
  ```
    * Final code:
    ``` 
    def validate_entries(entries):
    """
    Convert all string values into integers,
    Raises ValueError if strings cannot be
    converted into integers, if there aren't
    exactly 5 values, or if the values entered
    cannot be divided by 6.
    Function return True if the user insert correct values.
    """
    # Convert list of string into integers and raise VallueError
    # if entries are not integers or more or less then 5 numbers.
    try:
        entries = [int(entry) for entry in entries]
        if len(entries) != 5:
            raise ValueError(
                f"The user must enter exactly 5 values,"
                f" you provided {len(entries)}"
            )
    except ValueError as err:
        print(f"Invalid entries: {err}, please try again.\n")
        return False
    # Use modulo operator to check if the integers can
    # be devided by 6.
    for entry in entries:
        if int(entry) % 6 != 0:
            print(f"{int(entry)} is not divisible by 6.\n")
            return False
    return True
    ```
* Another bug showed up when trying to update ```final_stock``` values to the initial_stock rows worksheet. An Error rised when I tried to create a function and import ```final_stock``` data, then assigned it to initial_stock variable. I solved it by updating the initial_stock worksheet data with the ```final_stock``` data variable within ```main``` function.
    * The initial code was:
    ```
    def new_initial_stock(final_stock):
    """
    Import final stock data to initial stock worksheet rows.
    """
    initial_stock = SHEET.worksheet("total_stock").get_all_values()
    initial_stock_row = total_stock[-1]
    ```
    * Final code:
    ```
    update_worksheet_data(final_stock_data, "initial_stock")
    ```
* Within except statement, when trying to raise ValueError as e, this probolem showed up “Variable name ‘e’ doesn’t conform to snake_naming style”. I solved it changing the “e” to “err”.
* Trying to convert strings into integers  within try statement a problem was raised that says “[int(entry) for entry in entries] is assigned to nothing”. I solve this problem assigning the expression to entries variable.

## Known Bugs
* There are no known bugs within the aplication.
***

## Deployment

### Delpoying to GitHub Pages
<details>
<summary>The project was deployed with the following steps</summary>

* Log into GitHub;
* Click the "Settings" button in the menu above the Repository;
* Scroll down the Settings page to the "GitHub Pages" Section;
* Under "Source", click the dropdown called "None" and then select "Master Branch";
* The page will automatically refresh, and a link displaced. It may take some time for the link to show the website.
* If the page will not load go down to "template" under the "source" and select a template.
* Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.
</details>

### Forking
<details>
<summary>Forking the GitHub Repository</summary>

By forking the GitHub Repository, you can make a copy of the original repository in your own GitHub account. This means we can view or make changes without making the changes affecting the original.

* Log into GitHub and locate the GitHub Repository;
* At the top of the Repository there is a "Fork" button about the "Settings" button on the menu;
* You should now have a new copy of the original repository in your own GitHub account.
</details>

### Cloning
 <details>
 <summary>Steps on cloning</summary>

Taken from GitHub's documentation on cloning, which can be found [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)
 
* Once logged into GitHub, navigate to the repository you wish to clone.
* Next to the green Gitpod button there's a button that reads code, click this.
* To clone the repository using HTTPS, copy the link whilst HTTPS is selected.
* Open your local IDE of choice and open the terminal.
* Navigate to the working directory of where you want the cloned directory to be.
* Type ```git clone``` in the terminal and then paste the link that you selected in step 3. Press enter.
* The clone is created in your current working directory (```cwd```).
</details>

### Adding and commiting files
<details>
<summary>Steps to adding and commiting files</summary>
I’ve been using Gitpod to write my code and using the terminal within to add, commit and push code from my workspace to GitHub where it is stored remotely as shown in the course content.

* When I have made a couple of minor additions / changes or one large change or addition I add the file in question to the staging area by typing in the terminal git add . the full stop will add all new files.
* I now want to save my changes to the local repository by typing git commit –m “ ” into the terminal. Between the “ ” I'll write a concise message detailing what this commit has done.
* When I either want to upload all my changes for the day or view on GitHub Pages I push all the commits I’ve previously done to GitHub using the git push command. When GitHub Pages is set up for the repository in question it will automatically pick up these changes and display the most up to date version that has been pushed.
</details>

## Deploying to Heroku
<details>
<summary>Steps on how to deploy to Heroku</summary>
* The requirements.txt file in the project was updated to include details on the project dependencies. Steps to do this are : 
     * Enter the following command at the terminal prompt : 'pip3 freeze > requirements.txt'
     * Commit resulting changes to requirements.txt and push to github
     * Log in to [Heroku](https://id.heroku.com/), create an account if necessary.

* From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.

* On the Create New App page, enter a unique name for the application and select region. Then click Create app.

* You will then be brought to the Application Configuration page for your new app. Changes are needed here on the Settings and Deploy tabs.

* Click on the Settings tab and then scroll down to the Config Vars section to set up the private Environment Variables for the application - i.e. the credentials used by the application to access the spreadsheet data.

* Click on Reveal Config Vars. In the field for key enter 'CREDS' and paste the entire contents of the creds.json file into the VALUE field and click ADD.

* Next, scroll down the Settings page to Buildpacks. Click Add buildpack, select Python from the pop up window and click on Save changes. Click Add buildpack again, select Node.js from the pop up window and click on Save changes. It is important that the buildpacks are listed Python first, then Node.js beneath.

* Click on the Deploy tab on the Application Configuration page.

* Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is https://github.com/FlorinDorneanu/garden-bar-stock) and click on Connect to link up the Heroku app to the GitHub repository code.

* Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Automatic Deploy was selected.

* The application can be run from the Application Configuration page by clicking on the Open App button.

* The live link for this project is (https://garden-bar-stock.herokuapp.com/)
</details>

## How to create and configure the Google spreadsheet and APIs
<details>
<summary>Steps to setup and configure access to data</summary>
* Create the Google Spreadsheet : 
    * Log in to your Google account (create one if necessary)
    * Create a Google Spreadsheet
***

* Set up APIs using the Google Cloud Platform
    * Access the [Google Cloud Platform](https://console.cloud.google.com/)
    * Create a new project and give it a unique name, then select the project to go to the project dashboard
    * Setup Google Drive credentials
       * Click on the hamburger menu in the top left of the screen to access the navigation menu
       * On the left hand menu select 'APIs and Services' and then 'Library'
       * Search for Google Drive API
       * Select Google Drive API and click on 'enable' to get to the API and Services Overview page
       * Click on the Create Credentials button near the top left of the screen
       * Select 'Google Drive' API from the dropdown for 'Credential Type'
       * Select the 'Application Data' radio button in the 'What data will you be accessing' area
       * Select the 'No, I'm not using them' for the 'Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?' area
       * Cick Next
       * On the Create Service Account page, step 1 is to enter a service account name in the first text box. Any value can be entered here.
       * Click on 'Create and Continue'
       * On step 2, 'Grant this service account access to project', select Basic -> Editor from the 'Select a Role' dropdown.
       * Click on Continue
       * On step 3, 'Grant users access to this service account', simply press Done, no input is necessary
       * On the next page, click on the service account name created (listed under the Service Accounts area) to go to the configuration page for the new service account.
       * Click on the KEYS tab at the top middle of the screen.
       * Click on the Add Key dropdown and select Create New Key.
       * Select the JSON radio button then click Create. The json file with the new API credentials will download your machine.
       * Rename the downloaded file to creds.json. This filename is already listed in the project .gitignore file and so no further action will be needed to prevent it being accidentally uploaded to github
       * Copy the new creds.json file into the local clone
       * In the creds.json file, copy the value for "client email" and then on Google Drive, share the spreadsheet created above with this email address assigning a role of Editor.

    * Enable Google Sheets API
    * Go back to the dashboard for the project on Google Cloud Platform and access the navigation menu as before
    * On the left hand menu select 'APIs and Services' and then 'Library'
    * Search for Google Sheets API
    * Select Google Sheets API and click on 'enable'

* Install gspread and google-auth libraries in the development environment using the command 'pip3 install gspread google-auth'
</details>

***

## Credits
### Code 
* The project was inspired by the [Love Sandwiches](https://github.com/FlorinDorneanu/love-sandwiches) project.
* Information on how to use the modulo operator came from [this website](https://realpython.com/python-modulo-operator/)

### Content
* This is the [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1_bFxiOYLpyKdjkEknhJHXb5UEMYlK5KvaoMXk-SH768/edit?usp=sharing)

### Acknowledgements
* Tutor support and Code Institute for being helpful answering my questions.

  
  
