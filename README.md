# Helloworld Chat

> This project is based on [OtakuTotipotent/my_flask_app](https://github.com/OtakuTotipotent/my_flask_app)

## Structure of website: Application Blueprint

``` Markdown

'/'
├── The homepage of the website
|   └── Available for all with limited features and access
|   └── Without account, user can only view public content
|   └── With account, user can access private content and features
|
└── If user is not logged in
|   └── A Welcome message
|   └── A "Login" button
|   └── A "Sign Up" button
|
|── If user is logged in
|   └── "Helloworld Chat" heading at top left
|   └── Search bar at top right
|   └── An "+ Add" button at bottom right inside the contact list container
|   └── Contains user contacts as bubble buttons
|   |   └── On hovering over them, shows a delete icon (🗑️ with red color)
|   |   └── On clicking the delete icon, prompts a confirmation dialog
|   |   └── On confirming, deletes the contact from the list
|   |   └── On clicking the contact bubble, opens that user's profile page '/<username>'
|   |   └── On clicking the "+ Add" button, opens a modal dialog to add a new contact (by username that user has signed up with and a Name field that current user can set for that contact on his own choice)
|   |   └── The user can add multiple contacts
|   |   └── The new contact is added to the contact list and saved in the database
|   |   └── On creating a new contact, the user is redirected to that contact's profile page '/<username>' if public, else a request is sent to that user for approval
|   └── The main content area with a lot of public random posts for users without logged-in and a lot of public + private posts for logged-in users
|   └── Each post has a title, content, author, timestamp, copy, hide, promote, dislike, and like buttons
|   |    └── On clicking the copy button, the post content is copied to clipboard
|   └── An option to create a new post with title and content that directs to '/create_post' page If user is logged in
|
|── A Header at the top
|   └── Website Logo & Title
|   └── Navigation Bar with links to other pages
|   └── A User Profile Icon at top right 
|   └── A Search icon for global search
|   └── A theme toggle button (Default: Pink, others: Blue, Green, Dark, Rainbow, Gold, Purple, Red)
|
└── A Footer at the bottom

```
