---
iso-thes:broaderGeneric: "[[communication protocol]]"
skos:related:
  - "[[access control]]"
  - "[[authentication]]"
  - "[[delegation]]"
---
**OAuth 2.0**: open protocol by which a user lets an application act on a resource on their behalf, within a limited scope, without giving it their password. The application receives tokens (a short-lived access token, and with `access_type=offline` a long-lived **refresh token**).

## Field notes: letting a server read domain-restricted files through a bot user

- **The password never travels.** The user signs in on the provider's page; the script only gets the refresh token. Having the password is not an input for the agent.
- **Client type matters.** A *Web application* client fails a local `run_local_server` flow (`redirect_uri_mismatch`, no `installed` key). It must be a *Desktop app* client.
- **A client secret is shown once.** Consoles no longer let you download it again; if lost, add a new secret on the same client.
- **The protocol can succeed and the service still refuse.** Sign-in works, then the workspace answers "no access to Drive": the service is switched off for the bot's organisational unit. That's an admin setting, outside OAuth; nothing in code fixes it.
- **Access ≠ visibility.** Even with the service on, the bot sees nothing until the folders are shared with it.

Alternative without any user token: domain-wide [[delegation]] of a [[service account]], granted by an admin for one scope. Less code, no revocable token, but requires admin trust.
