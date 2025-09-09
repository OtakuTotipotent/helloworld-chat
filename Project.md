# Helloworld Chat

> This project is based on [OtakuTotipotent/my_flask_app](https://github.com/OtakuTotipotent/my_flask_app)
>
> Read the original README.md for more details here [README.md](README.md)
>
> ie. Introduction, Installation & Setup, Features, Technologies Used, Contributing, License, Contact Information, Acknowledgements

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
