---
iso-thes:broaderGeneric: "[[communication protocol]]"
skos:related:
  - "[[access control]]"
  - "[[authentication]]"
  - "[[delegation]]"
---
**OAuth 2.0**: open protocol by which a user lets an application act on a resource on their behalf, within a limited scope, without giving it their password. The application receives tokens (a short-lived access token, and with `access_type=offline` a long-lived **refresh token**).

## Field notes (Bom Bom Boom, 2026-11-17 → 23)

Goal: let a server read 2D drawings that can only be shared inside the company domain, through a bot user `bbb@…` (read-only Drive scope).

- **The password never travels.** The user signs in on Google's page; the script only gets the refresh token. "I have the password" is not an input for the agent.
- **Client type matters.** A *Web application* client fails a local `run_local_server` flow (`redirect_uri_mismatch`, no `installed` key). It must be a *Desktop app* client.
- **A client secret is shown once.** The console no longer lets you download it again; if lost, add a new secret on the same client.
- **The protocol can succeed and the service still refuse.** Sign-in worked, then Workspace answered "no access to Drive": the service was switched off for the bot's organisational unit. That's an admin setting, outside OAuth, and nothing in code fixes it.
- **Access ≠ visibility.** Even with Drive on, the bot sees nothing until the folders are shared with it.

Alternative without any user token: domain-wide [[delegation]] of a service account, granted by a Workspace admin for one scope. Less code, no revocable token, but requires admin trust.
