# Execution and Connections

Read this reference for requested media production, connections, publishing, scheduling, analytics, or external modifications. Campaign mode controls content depth; execution is a separate, conditional capability.

## Discover Before Promising

Inspect the environment's actual tool catalog and relevant connected accounts. Use available discovery facilities; do not invent tool names, integrations, API endpoints, commands, or settings. Read tool schemas and official documentation relevant to the requested operation.

For each needed capability, establish:

- Actual tool and supported operation: image/design generation, video/audio production, editing, publishing, scheduling, or account/post analytics.
- Availability of the selected platform, account identity, granted permissions, and any account-type or media restrictions supported by the documentation.
- Missing inputs, tool limits, potential charges or credits, and whether outputs become public.
- Status: verified available, connection/permission required, unavailable, or unverified.

Inspect only accounts relevant to the request. Use read-only discovery before mutations. Access to analytics does not imply publishing permission; one connected platform does not establish support for another. If cost is unknown, say so. Establish a user-approved budget or cost limit before chargeable work outside an existing authorization; stop before exceeding it. Request only the minimum scopes needed for the requested action.

## Missing Tools or Permissions

Identify the exact missing capability, account, or permission using observed tool results and current official documentation. Distinguish an absent tool from an installed tool with an expired connection or insufficient scope.

Explain setup step by step using the official documentation actually available for that provider and environment:

1. Link the official documentation supporting the connection method and prerequisites.
2. Describe where the user starts the documented connection flow; name controls or commands only when verified.
3. Explain account selection and the minimum scopes needed for this task.
4. Have the user finish authentication through the provider's official secure flow, using OAuth when offered.
5. Ask the user to report completion without sharing secrets, then perform the safe verification below.

Never request passwords, access tokens, client secrets, or recovery codes in chat or put them in task files. If official documentation requires a credential, direct the user to its documented secure credential interface. Do not create a substitute login form or broaden permissions to bypass failure.

If documentation cannot be accessed or does not confirm a step, state exactly what cannot be verified. Request a non-secret official help link if useful, or offer the manual fallback. Do not fill gaps with guessed instructions. This reference supplies a workflow, not a claim that any particular integration exists.

## Verify a Connection Safely

“Connected” from the user is a signal to check, not proof of access. Use a documented read-only operation to verify the intended account identity and relevant accessible resource or granted scope. Publish, upload publicly, schedule, send, or edit nothing during verification. Do not use a test post to check access.

Compare the result with the requested platform/account. A basic profile read verifies identity/access only; if it does not expose publishing or scheduling scopes, leave those capabilities unverified and use documented permission inspection where available. If no safe verification exists, report that limitation and pause dependent execution.

## Preserve and Resume the Task

Keep a minimal non-secret checkpoint in the conversation or an authorized local task artifact:

- Campaign brief, user profile, output mode, selected angle/platforms, and constraints.
- Current copy/asset versions and their paths or links.
- Target accounts, proposed dates/times with timezone, budget, and required permissions.
- Completed operations with returned IDs/statuses, pending operations, blocker, and next step.
- Any approval with the exact operation and version it covered; flag changes requiring new approval.

Do not store credentials or unnecessary private account data. Do not claim persistence beyond available storage. After connection verification, resume the blocked step using the checkpoint and preserve completed work. Connection approval never substitutes for approval of an external mutation. Recheck stale account, timing, cost, or asset details before execution.

## Produce and Inspect Media

Use available generation/editing tools only for the requested scope and within approved costs. Create final images/designs, video, audio, and edits when supported. Follow relevant installed production skills when applicable; do not require a skill or tool absent from the environment.

Check returned files for accessibility and suitability: Arabic spelling and layout, brand/product fidelity, requested format, video duration, audio, and synchronization as relevant. Report uninspectable aspects. Keep final files distinct from concepts, prompts, scripts, and previews. A submitted or running job is not a completed asset. Resolve failed jobs within scope and budget; do not incur unlimited retries.

If a production tool also posts publicly or makes a consequential external change, apply the approval gate before that operation.

## Final Preview and Approval Gate

Complete preparation and validation before asking for approval. Immediately before **each** publish, schedule, or consequential external modification (including editing/deleting a post, changing its schedule, or sending a response), show:

- Exact operation and final content, including caption, links, hashtags, and disclosures.
- Actual media attachments, their order, and a viewable preview or accessible file links.
- Platform and unambiguous target account identity.
- Publish now or exact scheduled date/time and timezone; clarify missing/ambiguous timing before scheduling.
- For modifications, the target ID/link and the precise before/after change.
- Known cost and unresolved constraints, if any.

Ask for explicit approval of that particular operation and wait. Approval to plan, prepare, generate assets, connect accounts, or approve a campaign generally is not permission to publish or schedule. Earlier “publish everything” requests do not replace the final per-operation approval. Silence is not consent.

Execute only the approved payload/account/time. A changed asset, text, account, timing, operation, or material cost requires a refreshed preview and approval. For a multi-platform campaign, obtain approval immediately before each separate publish/schedule operation; do not use one blanket campaign approval. A documented atomic carousel publication is one operation; independently created thread posts are separate operations. Do not silently use a bulk mutation that bypasses this gate.

## Execute and Report the Actual Result

Call only the verified operation within approved scope. Treat tool errors and returned state as evidence. Where available, read back the returned resource/status without changing it.

For each operation report platform/account, attempted action, actual state (published, scheduled, processing, failed, or uncertain), returned identifier or link, and confirmed timing where relevant. A queued job is not a published post; a scheduled post is not yet published. Never invent an ID, link, metric, or success message.

On partial success, list completed and incomplete operations separately with their observed reasons. Do not undo successful operations automatically: deletions and consequential rollbacks require their own preview and approval.

## Stop Conditions and Safe Failure

Pause the affected operation for denied/revoked permissions, account mismatch, unresolved costs, missing media, expired timing, changed payload, or unclear approval. Continue independent preparation where possible.

After a timeout or ambiguous mutation result, do not retry blindly. Use documented read-only status/history or idempotency facilities if available to reconcile whether it occurred. If uncertainty remains, stop and report it; another mutation risks a duplicate. A new publish/schedule attempt requires immediate explicit approval after reconciliation. Never repeat a successful operation or retry indefinitely. A denied permission requires corrected access, not repeated calls or broader scope by default.

If connection is unavailable, refused, or cannot be verified, provide a manual handoff: platform-specific copy and captions, available final files, carousel text/order, scripts/briefs for unproduced media, proposed schedule/timezone, and remaining manual steps. Clearly separate completed files from items still needing production. Missing tools must not prevent delivery of useful prepared work or be hidden by a false “ready” claim.

## Analytics and Improvements

For requested analysis, use verified read permissions and the minimum necessary account/post data. Report the source, account/post IDs, date range, timezone, retrieval time, metric definitions and denominators where available, and missing data. Distinguish account totals from post metrics and organic from paid data when supplied. Do not interpret unavailable values as zero.

Compare against a relevant baseline and campaign objective. Separate observations from hypotheses; small or incomparable samples do not prove causation. Recommend concrete changes to hooks, creative, calls to action, cadence, or repurposing, with an A/B plan and measurement window. Do not change live posts or schedules as part of reading analytics without a separate preview and approval.

If live analytics are unavailable, offer analysis of a user-provided non-secret export or a measurement template. Label the source accurately and never fabricate performance results.
