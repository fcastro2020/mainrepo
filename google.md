# Instructions for Setting Up Jupyter Notebooks To Output to Google Docs 

This document describes the process of setting up the capability to generate output in the form of Google Docs by the Ultraviolet Jupyter Notebooks application, including the generation of authorization credentials by two types: (1) Service Account Credentials Key, or (2) OAuth 2.0 Credentials. The process described in these instructions starts with the creation of a new Google Cloud Project where you will enable the necessary APIs, Google Drive and Google Docs APIs. Once the proper APIs have been enabled, you can decide on the authorization method type (Service Account / OAuth), depending on your company's security policies.
<br>

## Table of Contents

[Create a Project in the Google Cloud Console and Enable APIs](#create-a-project-in-the-google-cloud-console-and-enable-apis)

* [Step 1: Access Google Cloud Platform](#step-1-access-google-cloud-platform)
* [Step 2: Create a New Project](#step-2-create-a-new-project)
* [Step 3: Set up the New Project](#step-3-set-up-the-new-project)
* [Step 4: Enable APIs](#step-4-enable-apis)

[Instructions for Creating a Service Account and Its Associated Key Credentials File](#instructions-for-creating-a-service-account-and-its-associated-key-credentials-file)

* [Step 1: Create a Service Account](#step-1-create-a-service-account)
* [Step 2: Create Credentials](#step-2-create-credentials)

[Instructions for Creating Credentials Using OAuth 2.0 Authentication Method](#instructions-for-creating-credentials-using-oauth-20-authentication-method)

* [Step 1: Create the Consent Screen](#step-1-create-the-consent-screen)
* [Step 2: Create the OAuth 2.0 Credentials](#step-2-create-the-oauth-20-credentials)
* [Step 3: Download OAuth 2.0 JSON Credentials File](#step-3-download-oauth-20-json-credentials-file)
<br>
<br>
<br>

# Create a Project in the Google Cloud Console and Enable APIs

## Step 1: Access Google Cloud Platform[<div style="text-align: right; font-size: 9px">Go to Table of Contents</div>](#table-of-contents)
Access your Google Cloud Platform (GCP) [console dashboard](https://console.cloud.google.com/home/dashboard). 
<br>


![Access the Google Cloud Platform Console](/img/google_01_access_gcp_console.png)
<br>
<br>

## Step 2: Create a New Project [<div style="text-align: right; font-size: 9px">Go to Table of Contents</div>](#table-of-contents)

After navigating to the cloud platform, you will need to create a new project. Click on the project box next to the Google Cloud Logo and select the resource (organization) the project will be associated with, then click on "NEW PROJECT".


![Create a New Project](/img/google_02__create_new_project.png)
<br>
<br>

## Step 3: Set up the New Project[<div style="text-align: right; font-size: 9px">Go to Table of Contents</div>](#table-of-contents)

Set up the name of the new project and the location, if different from default. This will probably depend on internal information security rules, so you can configure this by your internal data security policies.

![Create a New Project Screen 2](/img/google_02_01_create_new_project.png)
<br>
<br>

## Step 4: Enable APIs[<div style="text-align: right; font-size: 9px">Go to Table of Contents</div>](#table-of-contents)

Now that the project has been created and from the project "DASHBOARD" you will need to enable the following APIs:

- Google Docs API 
- Google Drive API 

In the "DASHBOARD" look for the "Getting Started" section and click on  "Explore and enable APIs"

![Enable APIs](/img/google_03__enable_apis.png)

In the "APIs & Services" screen select "Library"

![Enable APIs](/img/google_03_01_enable_apis.png)

Once you are in the API Library, type "Google Docs" in the search box and press enter. 

![Enable APIs](/img/google_03_02_enable_apis.png)

A list of matching APIs will be presented. You need to click on the first one called "Google Docs API".

![Enable APIs](/img/google_03_03_enable_apis.png)

Click on the "ENABLE" button and the Google Docs API will be enabled for the current project. In the example: "Ultraviolet Project"

![Enable APIs](/img/google_03_04_enable_apis.png)

The Google Docs API has now been enabled. Please, repeat the same process for the "Google Drive" API to enable the Google Drive API as well.
<br>
<br>
<br>

# Instructions for Creating a Service Account and Its Associated Key Credentials File

The following instructions assume that you have completed steps 1 to 4 of the "Instructions for Setting Up Jupyter Notebooks To Output to Google Docs" in the previous section. Please, remember that using a Service Account for creating Credentials is optional and you can use the alternative method proposed in this document, the OAuth 2.0 authorization method.

## Step 1: Create a Service Account[<div style="text-align: right; font-size: 9px">Go to Table of Contents</div>](#table-of-contents)

**Note:** We cover the creation of credentials on a machine-to-machine account basis, storing the credentials on the hard drive of the local computer that is executing the Ultraviolet Jupyter Notebooks (Clients may opt for a different form of managing Service Account Credentials).

To create a machine-only account, go to the Project's homepage on Google Cloud Platform. Then click on "Go to APIs overview":

![Create a Service Account and Credentials](/img/google_04_create_service_account_and_credentials.png)

After clicking on the "Go to APIs overview" link, you will be redirected to the "APIs & Services" page. Right there click on "Credentials" in the left pane menu:

![Create a Machine Account](/img/google_05_create_a_machine_account.png)

In the Credentials Page click on the "Manage service accounts" link in the Service Accounts section.

![Manage the Service Account](/img/google_06__manage_the_service_account.png)

After landing in the "Service accounts" page, click on the "CREATE SERVICE ACCOUNT" option.

![Create the Service Account](/img/google_06_01_create_service_account.png)

In this step you need to provide a "Service account name" and a "Service account description", the "Service account ID" will be auto-generated. In this section, you need to click on the "CREATE AND CONTINUE" button and do not click on the "DONE" button because you need to make sure you grant this service account access to the project.

![Create the Service Account](/img/google_06_02_create_service_account.png)

You need to specify the "Role" = "Editor" to the service account so it can access the project. After you have set the "Editor" role, please click on the "DONE" button. It is optional to define now who are going to be the users to have access to this specific service account.

![Create the Service Account](/img/google_06_03_create_service_account.png)

After clicking the "DONE" button in the "Create service account" section you will be redirected to the "Service accounts" page where you will be able to see the service account just created. At this step, you need to click on the service account's Email link to start the process of creating a Credentials Key File.

![Create the Service Account](/img/google_06_04_create_service_account.png)
<br>
<br>

## Step 2: Create Credentials[<div style="text-align: right; font-size: 9px">Go to Table of Contents</div>](#table-of-contents)

After creating a service account, click on the account to see its properties. At the top of the service account landing page, click on "KEYS" and select the "ADD KEY" drop-down menu.

![Create the Key](/img/google_07__create_key.png)

Now click on the "Create new key" menu option.

![Create the Key](/img/google_07_01_create_key.png)

Select the "Key type" JSON and click on the "CREATE" button. You need a JSON Key file to use Ultraviolet and its associated Google services.

![Create New Key](/img/google_07_02_create_key.png)

Now, your JSON Key Service Account file has been downloaded to your local disk in your "Downloads" folder. This Key JSON file contains the credentials for setting the Ultraviolet Notebook access to your Google Drive and Google Docs. 

![Create the Key](/img/google_07_03_create_key.png)

Clients completing this process may either coordinate with [Luminos.Law](https://luminos.law) to bundle the authorization file with the notebook or include it in the `auth` folder for the Jupyter distribution. This will allow the notebook to write to Google Docs.
<br>
<br>
<br>

# Instructions for Creating Credentials Using OAuth 2.0 Authentication Method

This section of the document describes the process to set OAuth 2.0 credentials to access the necessary API services (Google Drive and Google Docs) that will allow you to output a Google Docs document to your Google Drive from the Ultraviolet Jupyter Notebooks. The following instructions assume that you have completed steps 1 to 4 of the "[Create a Project in the Google Cloud Console and Enable APIs](#CreateaProjectintheGoogleCloudConsoleandEnableAPIs)" in the first section of this document.

OAuth Credentials can only be obtained once you have created a Consent Screen. The Consent Screen will be presented to users either the first time they want to output a Google Docs document to their Google Drive or when the Credentials' token has expired. Once you have set Ultraviolet on your computer and you want to output a bias report to a Google Docs document, the app execution flow will control the need for obtaining client consent or not.

In the following step, you will be guided on how to create the Consent Screen for using the Ultraviolet application.
<br>

## Step 1: Create the Consent Screen[<div style="text-align: right; font-size: 9px">Go to Table of Contents</div>](#table-of-contents)

To create the Application Consent Screen, please access your project dashboard screen and click on the hamburger menu in the upper left corner next to the Google Cloud Logo, then select "APIs & Services" and click on "OAuth consent screen".

![Select OAuth consent screen](/img/google_08__create_oauth_consent.png)

Select "User Type" "internal" and then click on the "CREATE" button:

![Select User Type Internal](/img/google_08_01_create_oauth_consent.png)

You will be redirected to the "Edit app registration" screen.

![Specify App Name and email](/img/google_08_02_create_oauth_consent.png)

In the "Edit app registration" screen you need to specify an App name, in this case Ultraviolet, and a User support email from an internal contact who can answer questions about permissions and consent to end users. In this "App information" section you also can include an app Logo that will be displayed in the Consent Screen. This logo can be an image of your choice, and different from Luminos logo.

In this section, you do not need to set an "App domain" or "Authorized domains". In the "Developer contact information" please enter support@luminos.law (Check this)..

![App domain and Authorized domains](/img/google_08_03_create_oauth_consent.png)

Now you can click on "SAVE AND CONTINUE". 

After you save and continue you are going to be redirected to the "Scopes" page but you do not need to configure anything here because the application controls the Scopes.


![No Need to Define Scopes](/img/google_08_04_create_oauth_consent.png)

Now you can click on "SAVE AND CONTINUE" and you will see a summary of your app registration. No need for any further action here.

![Screen Consent Summary](/img/google_08_05_create_oauth_consent.png)

Now you can click on "BACK TO DASHBOARD".
<br>
<br>

## Step 2: Create the OAuth 2.0 Credentials
<p align="right"><a href="#table-of-contents"><small>My text here</small></a></p>

</p>

Once you have finished the consent screen definition, you can click on "BACK TO DASHBOARD" and select the "Credentials" option in the left menu. 

![Select Create Credentials](/img/google_09__create_oauth_credentials.png)

In the "Credentials" screen, click on the "+CREATE CREDENTIALS" button and select the "OAuth Client ID" option.

![Select Create Credentials](/img/google_09_01_create_oauth_credentials.png)

In the "Create OAuth Client ID" screen select "Application type" --> Desktop app.

![App Type Desktop](/img/google_09_02_create_oauth_credentials.png)

Name the application as Ultraviolet, and then click on the "CREATE" button.

![App Name](/img/google_09_03_create_oauth_credentials.png)
<br>
<br>

## Step 3: Download OAuth 2.0 JSON Credentials File[<div style="text-align: right; font-size: 9px">Go to Table of Contents</div>](#table-of-contents)

Once you have created the OAuth Client you can download the JSON file containing the OAuth 2.0 Credentials.

![App Name](/img/google_10__download_json_credentials.png)

Clients completing this process may either send the JSON credentials file to [Luminos](https://luminos.law) or include it in the `auth` folder for the Jupyter distribution. This will allow the notebook to write to Google Docs in the client's Google Drive.
