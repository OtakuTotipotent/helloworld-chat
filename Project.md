# Helloworld Chat

> This project is based on [OtakuTotipotent/my_flask_app](https://github.com/OtakuTotipotent/my_flask_app)
>
> Read the original README.md for more details here [README.md](README.md)
>
> ie. Introduction, Installation & Setup, Features, Technologies Used, Contributing, License, Contact Information, Acknowledgements

## Structure of website: Application Blueprint

``` Markdown

'/'
├── The homepage of the website (base.html + home.html)
    └── Available for all with limited features and access (users without account/login)
    └── Without account, users can only view public content (content owners can set their posts as public or private while creating them). Users can't create posts, comments, contacts, or like/dislike/promote others' posts, add contacts, or message others, but they can search for users and view public profiles and posts.
    └── With account, users can access private content and features. They can create posts, comments, contacts, like/dislike/promote others' posts, add contacts, and message others. They can also search for users and view both public and private profiles and posts.
|── The main layout is divided into three sections:
       └── A contacts section (as a left sidebar for bigger screens and as a top div/box for smaller screens, like mobile devices). This section displays the user's contacts as bubble buttons. If the user is not logged in, this section is still visible but shows a message prompting the user to log in or sign up to access contact features, plus a few random public contacts to view their profiles and posts and a search bar at the top to search for users by username/email/name. The contacts section also includes an "+ Add" button at the bottom right to add new contacts (if logged in).
       └── A Main Content Area (center on bigger screens, below the contacts section on smaller/mobile screens) that displays posts. For users without an account or not logged in, it shows a variety of public posts from different users. For logged-in users, it shows both public and private posts from their contacts and other users. Each post includes a title, content, author, timestamp, and buttons for copy, hide, promote, dislike, and like. Users can create new posts by clicking a button that directs them to the '/create_post' page (if logged in).
       └── A Footer at the bottom (base.html) that is consistent across all pages, containing links to important sections of the website, contact information, and social media links. It provides easy navigation and access to essential information regardless of the page the user is on.

|── If user is logged-in, the contacts section shows:
    └── A search bar at the top to search for users by username/email/name
    └── On hovering over any contact bubble, shows a delete icon (at top right of that bubble) to delete that contact (delete icon is hidden when not hovering and when user is not logged in, also the deletion process asks for confirmation to avoid accidental deletions)
    └── On confirming, deletes the contact from the list and from the database, as well as all messages and posts associated with that contact, and also informs other user about the deletion via a notification (notifications are gathered in a notification center accessible from the user profile icon at top right)
    └── On clicking the contact bubble, opens target user's profile page '/<username>' if public, else a request is sent to that user for approval
    └── An "+ Add" button at the end of all contacts, to add new contacts
    └── On clicking the "+ Add" button, opens a modal dialog to add a new contact (by username that target user has used for signing up, and a Name field that current user can set for that contact, which can be different from target user's actual name)
    |   └── The user can add multiple contacts at once by separating usernames with commas
    |   └── On submitting the form, checks if the username(s) exist (existed users are skipped, others are added as new contacts, and a notification is sent to those users about being added as a contact. If the target user has set their profile to private, a request is sent to that user for approval before adding them as a contact)
    |   └── The new contact is added to the contact list and saved in the database
    |   └── On creating a new contact, the user is redirected to that contact's profile page 'users/<username>' if public, else a request is sent to that user for approval
    └── The main content area with a lot of public random posts for users without logged-in and a lot of public + private posts for logged-in users
    └── Each post has a title, content, author, timestamp, public/private status, copy, hide, promote, dislike, and like buttons
    |    └── On clicking the copy button, the post content is copied to clipboard
    └── An option to create a new post with title and content that directs to '/create_post' page If user is logged in

|── A Header at the top
    └── Website Logo & Title "Helloworld-Chat" at top left
    └── Navigation Bar with links to other pages
    └── A User Profile Icon at top right 
    └── A Search icon for global search
    └── A theme toggle button (Default: Pink, others: Blue, Green, Dark, Rainbow, Gold, Purple, Red)

|── The Profile page of any user (base.html + profile.html)
    └── Accessible via '/<username>' URL if public, else a request is sent to that user for approval if not contacts (only for logged-in users)
    └── Displays user's profile information (name, username, email (if public), bio, avatar, join date, number of posts, number of contacts, birthday (if public), location (if public), website (if public), social media links (if public), and privacy settings, if the user has set them to public)
    └── If the visitor is not logged in, shows a message prompting the user to log in or sign up to access more features, plus a few random public contacts to view their profiles and posts and a search bar at the top to search for users by username/email/name
    └── If the visitor is logged in but not contacts with the profile owner, shows a message prompting the user to send a contact request to the profile owner to access more features, plus a few random public contacts to view their profiles and posts and a search bar at the top to search for users by username/email/name
    └── If the visitor is logged in and contacts with the profile owner, shows the full profile information and posts
    └── Add actions based on the relationship between the visitor and the profile owner:
        └── a "Report User" button to report the user for inappropriate behavior (with confirmation), which sends a report to the admin for review, and informs the profile owner about being reported via a notification (notifications are gathered in a notification center accessible from the user profile icon at top right), and a "Unblock User" button to unblock the user if they were previously blocked.
        └── If not contacts, shows an "Add Contact" button to send a contact request to the profile owner
        └── If contacts, shows a "Message" button to start a private conversation with the profile owner, and a "Remove Contact" button to remove the contact (with confirmation), which also deletes all messages and posts associated with that contact, and informs the other user about the deletion via a notification (notifications are gathered in a notification center accessible from the user profile icon at top right), and a "Block User" button to block the user (with confirmation), which also removes them from contacts if they were contacts, deletes all messages and posts associated with that user, and prevents any future contact requests or messages from that user, and informs the other user about being blocked via a notification (notifications are gathered in a notification center accessible from the user profile icon at top right).
        └── If a contact request is pending (sent by either party), shows a "Cancel Request" button to cancel the contact request, or refresh the request to send a new request if the previous one was ignored/declined or to boost the request (boosting a request sends a notification to the target user)
        └── Displays user's posts (public posts for all visitors, both public and private posts for logged-in contacts), posts count, and pagination (5 posts per page), with each post showing title, content, author, timestamp, and buttons for copy, hide, promote, dislike, and like, share the post to visiting user's profile, and a comment section for each post to view/add comments (if logged in)
        └── Each post has a title, content, author, timestamp, public/private status, copy, hide, promote, dislike, and like buttons, and a comment section to view/add comments (if logged in).
        └── On clicking the copy button, the post content is copied to clipboard
|── The Logged-in user's Profile Dropdown Menu 
    (accessible by clicking the user profile icon at top right from header, available on all pages, base.html)
    └── Shows user's avatar, name, username, email (if public), bio, join date, number of posts, number of contacts, birthday (if public), location (if public), website (if public), social media links (if public), and privacy settings
    └── A link to view/edit the profile ('/profile'), edits can be made to name, bio, avatar, birthday, location, website, social media links, and privacy settings
    └── A link to view notifications ('/notifications')
    └── A link to view messages/conversations ('/messages')
    └── A link to view contacts ('/contacts')
    └── A link to Gallery of public posts ('/gallery')
    └── A link to create a new post ('/create_post')
    └── A link to settings ('/settings')
    └── A link to help & support ('/help')
    └── A link to report a problem ('/report')
    └── A link to delete the account ('/delete_account') (with confirmation, which deletes all user data including posts, comments, contacts, messages, and profile information from the database, and informs all contacts about the account deletion via a notification (notifications are gathered in a notification center accessible from the user profile icon at top right)) deleting the account logs out the user and redirects to homepage, sends a deletion message to admin for record-keeping, and the username/email becomes available for new users to sign-up again
    └── A logout button to log out the user (with confirmation)
|--- The Create Post page (base.html + create_post.html)
    └── Accessible via '/create_post' URL (only for logged-in users)
    └── A form to create a new post with fields for title, content, and public/private status (default: private)
    └── On submitting the form, the post is saved in the database and the user is redirected to their profile page to view the new post
    └── If the user is not logged in, redirects to the login page with a message prompting the user to log in or sign up to create a post
|--- The Messages/Conversations page (base.html + messages.html)
    └── Accessible via '/messages' URL (only for logged-in users)
    └── Displays a list of conversations with contacts on the left (contact's name, avatar, last message snippet, timestamp, unread message count)
    └── On clicking a conversation, opens the chat window on the right to view/send messages
    └── The chat window shows the contact's name, avatar, and online status at the top
    └── Below that, displays the message history with timestamps, read receipts, and typing indicators
    └── At the bottom, a text input box to type and send new messages (with emoji support, file attachment, and send button)
    └── Messages are sent/received in real-time using WebSockets
    └── If the user is not logged in, redirects to the login page with a message prompting the user to log in or sign up to view messages
|--- The Contacts page (base.html + contacts.html)
    └── Accessible via '/contacts' URL (only for logged-in users)
    └── Displays the user's contacts in a grid/list view with their name, avatar, and online status
    └── A search bar at the top to search for contacts by name/username/email
    └── An "+ Add Contact" button to add new contacts (same functionality as the "+ Add" button in the contacts section)
    └── On clicking a contact, opens that user's profile page '/<username>' if public, else a request is sent to that user for approval
    └── If the user is not logged in, redirects to the login page with a message prompting the user to log in or sign up to view contacts
|--- The Notifications page (base.html + notifications.html)
    └── Accessible via '/notifications' URL (only for logged-in users)
    └── Displays a list of notifications (new messages, contact requests, post likes/comments, account activity) with timestamps and read/unread status
    └── A "Mark all as read" button to mark all notifications as read
    └── On clicking a notification, redirects to the relevant page (message thread, contact profile, post, etc.) and marks the notification as read
    └── If the user is not logged in, redirects to the login page with a message prompting the user to log in or sign up to view notifications
|--- The Settings page (base.html + settings.html)
    └── Accessible via '/settings' URL (only for logged-in users)
    └── Allows the user to update account settings (email, password, privacy settings, notification preferences)
    └── A form to change the email address (with verification)
    └── A form to change the password (with current password confirmation)
    └── Privacy settings to control profile visibility, post visibility, contact requests, and message permissions
    └── Notification preferences to enable/disable email and in-app notifications for various events
    └── If the user is not logged in, redirects to the login page with a message prompting the user to log in or sign up to view settings
    └── Logged-in users can change their theme preference (Default: Pink, others: Blue, Green, Dark, Rainbow, Gold, Purple, Red) from settings page, which is saved in the database and applied across all pages
|--- The Help page (base.html + help.html)
    └── Accessible via '/help' URL (only for logged-in users)
    └── Provides FAQs, user guides, and contact support options
    └── A search bar to search for help topics
    └── A contact form to submit support requests (with subject, description, and optional screenshot attachment)
    └── If the user is not logged in, redirects to the login page with a message prompting the user to log in or sign up to view help
|--- The Report Problem page (base.html + report.html)
    └── Accessible via '/report' URL (only for logged-in users)
    └── A form to report bugs, suggest features, or provide feedback (with subject, description, and optional screenshot attachment)
    └── On submitting the form, the report is sent to the admin for review and the user is redirected to a thank-you page
    └── If the user is not logged in, redirects to the login page with a message prompting the user to log in or sign up to report a problem
|--- The Delete Account page (base.html + delete_account.html)
    └── Accessible via '/delete_account' URL (only for logged-in users)
    └── A confirmation page to delete the account (with warning about data loss and a checkbox to confirm)
    └── On confirming, deletes all user data including posts, comments, contacts, messages, and profile information from the database, and informs all contacts about the account deletion via a notification (notifications are gathered in a notification center accessible from the user profile icon at top right), logs out the user, and redirects to the homepage
    └── If the user is not logged in, redirects to the login page with a message prompting the user to log in or sign up to delete the account, sends a deletion message to admin for record-keeping, and the username/email becomes available for new users to sign-up again.


```

## 🚀 Application Feature Roadmap

This document outlines the planned and implemented features of the application.  
Features are grouped by category, with an MVP checklist and a suggested 3-phase rollout roadmap.  

---

### Table of Contents

1. [Core: Authentication & Accounts](#core-authentication--accounts)  
2. [Contacts & Presence](#contacts--presence)  
3. [Messaging & Conversations](#messaging--conversations)  
4. [Real-time, Calls & Notifications](#real-time-calls--notifications)  
5. [Media, Rich Content & Attachments](#media-rich-content--attachments)  
6. [Groups, Community & Collaboration](#groups-community--collaboration)  
7. [Admin, Moderation & Compliance](#admin-moderation--compliance)  
8. [Search, Analytics & Reporting](#search-analytics--reporting)  
9. [Data, Backups & Reliability](#data-backups--reliability)  
10. [Performance, Scalability & Caching](#performance-scalability--caching)  
11. [APIs, Integrations & Webhooks](#apis-integrations--webhooks)  
12. [UX, Accessibility & Internationalization](#ux-accessibility--internationalization)  
13. [Developer Experience, CI/CD & Observability](#developer-experience-cicd--observability)  
14. [Quality Assurance & Maintenance](#quality-assurance--maintenance)  
15. [Miscellaneous Helpful Features](#miscellaneous-helpful-features)  
16. [MVP (Must-Have) Checklist](#mvp-must-have-checklist)  
17. [Suggested 3-Phase Roadmap](#suggested-3-phase-roadmap)  

---

### Core: Authentication & Accounts

- Sign Up / Login / Logout  
- Email verification & Password reset  
- Secure password handling (bcrypt/argon2, validation)  
- Two-Factor Authentication (2FA)  
- Session management (JWT / server-side sessions)  
- Account deletion & data export (GDPR-ready)  
- User roles & permissions (user, moderator, admin)  
- Profile management (name, bio, avatar, privacy controls)  
- Third-party authentication (OAuth: Google, Facebook, etc.)  

---

### Contacts & Presence

- Contact management (add, remove, block, mute)  
- Contact groups / labels / favorites  
- User invitations & referrals  
- Presence & status (online, offline, last seen)  
- Privacy controls (who can see status/profile)  

---

### Messaging & Conversations

- Direct messaging (1:1)  
- Group chats (create, manage, roles)  
- Message history & pagination  
- Delivery guarantees (delivered/read receipts)  
- Typing indicators  
- Threads / replies / quoting  
- Mentions (@user)  
- Message editing & deletion  
- Message reactions (emoji)  
- Message search (conversation-level)  
- Scheduled messages & drafts  
- Pinning/starred messages  
- Link previews & inline media  
- Message encryption (TLS, optional E2E)  

---

### Real-time, Calls & Notifications

- Real-time updates (WebSockets / fallback)  
- Push notifications (mobile & browser)  
- In-app notifications center  
- Audio & video calls (WebRTC)  
- Call features (mute, camera toggle, screen share, recording)  
- Voice messages (record & send)  
- Notification throttling / digest  

---

### Media, Rich Content & Attachments

- File sharing (images, videos, docs)  
- Inline previews & thumbnails  
- Media storage via CDN (S3 or similar)  
- Transcoding & optimization  
- Virus/malware scanning on uploads  
- Stickers, GIFs & emoji support  
- Location sharing (map integration)  
- Rich text / markdown formatting  

---

### Groups, Community & Collaboration

- Group roles & permissions (admins, mods)  
- Public / private groups  
- Announcement channels  
- Polls & surveys  
- Forums / discussion boards  
- Event invites & RSVPs  

---

### Admin, Moderation & Compliance

- Admin panel (dashboard)  
- Reporting & abuse workflows  
- Moderation tools (mute, ban, remove)  
- Automated moderation (keyword filters, spam detection)  
- Audit & event logging  
- Legal compliance (GDPR, TOS, privacy policy)  
- Data retention rules  

---

### Search, Analytics & Reporting

- Search index (users, messages, groups)  
- Usage analytics (DAU/MAU, retention)  
- Admin dashboards & reports  
- Data visualization (charts, exports)  

---

### Data, Backups & Reliability

- Database integration (relational or document DB)  
- Automated backups & restore testing  
- Export/import user data (CSV/JSON)  
- Redundancy & failover  
- Disaster recovery plan  

---

### Performance, Scalability & Caching

- Caching strategies (Redis, etc.)  
- Message queues (Celery / RabbitMQ / Kafka)  
- Horizontal scaling & load balancing  
- CDN for static & media content  
- Rate limiting & abuse prevention  
- Performance monitoring (APM, alerts)  

---

### APIs, Integrations & Webhooks

- Public API (REST/GraphQL)  
- API documentation (OpenAPI/Swagger)  
- Webhooks (events: new message, new user)  
- Third-party integrations (CRM, SSO, analytics)  
- Mobile SDKs / app integration  

---

### UX, Accessibility & Internationalization

- Responsive design (mobile-first)  
- Dark mode / theme customization  
- Localization & multi-language support  
- Accessibility (WCAG, ARIA)  
- User onboarding flow (tooltips, walkthroughs)  
- Help & support (FAQs, contact support)  
- Keyboard shortcuts for power users  

---

### Developer Experience, CI/CD & Observability

- CI/CD pipelines (tests, builds, deployments)  
- Environment configuration (dev/test/prod)  
- Version control strategy (Git, PRs, branching)  
- Automated testing (unit, integration, E2E)  
- Logging & monitoring (structured logs, metrics)  
- Feature flags & A/B testing  

---

### Quality Assurance & Maintenance

- Bug reporting system  
- Feature request system  
- Release notes & changelog  
- Regular updates & patching  

---

### Miscellaneous Helpful Features

- SEO optimization (public pages)  
- PWA / desktop app support  
- Webhooks marketplace for integrations  
- Collaboration tools (shared docs, comments)  

---

### MVP (Must-Have) Checklist

- [ ] User sign up, login, logout (with verification & password reset)  
- [ ] User profile (basic info, avatar)  
- [ ] Contact management & 1:1 messaging  
- [ ] Message history (stored & paginated)  
- [ ] Real-time messaging (WebSocket)  
- [ ] Responsive UI (desktop & mobile)  
- [ ] File/image sharing  
- [ ] Basic notifications (in-app)  
- [ ] Admin: manage users  
- [ ] Security: password hashing, TLS, input validation  
- [ ] CI/CD pipeline & deployment docs  
- [ ] Logging & monitoring  

---

## Suggested 3-Phase Roadmap

### Phase 1 — MVP Launch

Core authentication, profiles, contacts, 1:1 chat, message storage, real-time updates, image sharing, responsive UI, logging, deployment setup.

### Phase 2 — Growth & UX

Group chats, typing/read receipts, search, edit/delete, mentions, reactions, dark mode, onboarding, accessibility, OAuth login.

### Phase 3 — Advanced & Scale

Voice/video calls, analytics dashboards, admin moderation automation, CDN scaling, backups/DR, PWA/mobile app, multi-language support, advanced integrations.

---
