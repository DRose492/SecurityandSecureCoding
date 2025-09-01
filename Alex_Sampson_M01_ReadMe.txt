README
~~~~~~~~~~~~~~~
This Python script is a demo employee login system with role separation for Users and Admins. It enforces CIA principles:
 * Confidentiality → email/password validation, lockouts after failed attempts.
 * Integrity → password rules, promotion/removal functions restricted to Admins.
 * Availability → simple menu system for users to check schedules, request time off, etc.

App Logic
~~~~~~~~~~~~~~~
 * Users/Admins are stored in registries.
 * Login verifies email + password before granting access.
 * Failed password attempts lock accounts after 3 tries.
 * Post-login, menus adapt by role (Admin gets extra tools).
 * Preloaded Accounts for Testing:

Test Logins
~~~~~~~~~~~~~~~
User → terydaman@email.com / TeryDaMan123

Admin → hlaurence45@email.com / G4rf23!:hHr9t6