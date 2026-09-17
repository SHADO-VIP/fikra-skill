# Execution and Connections

Read this reference for requested media production/editing, saved campaign packages, connections, publishing, scheduling, analytics, or external modifications. Campaign mode controls content depth; execution is a separate, conditional capability.

## Guided Next-Step Choice

After delivering the completed plan/content package for a full campaign with no explicit next step, ask exactly: «اكتملت خطة الحملة. ماذا تريد أن أنفذ الآن؟» Present a numbered subset of the following choices, with the short explanation beside each. Renumber the visible choices and adapt asset names to the actual campaign.

| Choice | Simple explanation |
| --- | --- |
| استلام النصوص والخطة فقط | تسليم المنشورات ونصوص الشرائح وسيناريوهات الفيديو. |
| إنشاء التصاميم والصور | إنتاج الصور وشرائح الكاروسيل كملفات فعلية. |
| إنتاج الفيديوهات | إنشاء ملفات الفيديو الفعلية، وليس السيناريوهات فقط. |
| إنتاج جميع مواد الحملة | إنشاء النصوص والصور والفيديوهات المطلوبة للحملة. |
| تجهيز الحملة للمعاينة قبل النشر | جمع المواد وعرض ما سيُنشر في كل منصة. |
| نشر المحتوى أو جدولته بعد المعاينة والموافقة | النشر على الحساب المحدد بعد التحقق والمعاينة والموافقة. |
| متابعة النتائج وتحليل الأداء بعد النشر | قراءة التحليلات المتاحة واقتراح تحسينات. |

Filter using the campaign's requested formats, completed work and known capabilities. Omit video when no video is needed, completed production choices, and unrelated or known-impossible actions. Do not promise unverified tools: when feasibility is unknown, describe execution as conditional on checking tools; when a capability is known absent, offer documented setup/manual delivery separately instead of advertising it as executable. Publishing may be an optional later step even if not requested, never an assumed action. Offer analytics only for already published material with a viable data source, or clearly as a later step after publication; do not imply results already exist.

Skip this menu when the user already chose a specific step, explicitly wants text only, or requested one deliverable/revision. Follow that scope and its approval gates directly. A choice of production is not approval to use an undisclosed tool; a choice of publishing is not final publication approval.

Use plain Arabic and numbered steps, with one clear decision at each stage. Explain unavoidable terms briefly. Do not ask the user to know API, MCP or OAuth names; introduce them only if a documented connection step needs them, explaining their purpose. Tell the user what happens next before doing it. Accept stopping, returning to a previous step, revising any asset, producing only some images, or manual publishing without connecting an account. Do not repeatedly offer further stages after a text-only/stop choice or pressure completion.

For Facebook and YouTube, use asset-specific labels in the same filtered menu, only for required materials: «تصميم منشورات Facebook»، «إنتاج Facebook Reel»، «إنتاج YouTube Short»، «إنتاج فيديو YouTube طويل»، «إنشاء صورة YouTube المصغرة»، «تجهيز مواد Facebook وYouTube للمعاينة»، and «رفعها أو جدولتها بعد الربط والمعاينة والموافقة». Explain each in one short sentence, such as «إنشاء ملف الفيديو الطويل الفعلي» or «إنشاء ملف صورة الغلاف». Do not show all these merely because the platforms are supported. Apply the existing feasibility filter and approvals; an upload choice is not upload consent.

## Route the Selected Step

1. Identify the exact assets needed for the selected step, using the existing brief and completed files. For text-only delivery, provide the copy/plan, record the agreed scope and stop. For a subset, list only the selected assets; leave other assets deferred.
2. Inspect available tool descriptions and already exposed account/permission metadata without running production or account actions. Read-only catalog discovery is preparation, not execution. Before invoking a selected tool, including an account verification or analytics read, explain the operation and obtain explicit permission unless the same tool and scope already have it. Never run a tool merely to see whether it generates media.
3. Present the suitable tools, expected files and relevant known costs/credits only. If unknown, state that briefly without estimates or unsupported credit warnings. Apply the tool-choice gate below; obtain approval for each named tool or clearly bounded group of operations before use.
4. If a needed tool/connection is missing, follow the official documented installation/connection steps below. Save the paused step and offer the available manual alternative. After the user completes setup, perform the authorized safe verification and resume from that checkpoint without asking for the campaign again.
5. Execute only the selected, authorized stage; inspect each actual result. Update the package and `execution-status.md` after each stage, including failures, changed choices and pauses. Show what finished, what is missing and the next single decision, if one is needed. Do not automatically advance into publication or analytics.

### Produce All Campaign Materials

Before tools run, build an inventory grouped by platform: asset identifier, format/count, completed text/script, existing media, media still to produce, dependencies and expected file properties. Include only materials required by this campaign; “all” does not add unrequested platforms, audio or video.

Check required image, video, audio and editing/export capabilities separately. Present the full production sequence, named tools, handoff files and known costs; obtain approval covering each tool or a clearly described batch. Produce in stages (for example images, clips/audio, then editing/export), inspecting every file with the media checks below. After every stage, save real outputs under the proper platform, preserve originals/versioned edits, and update file paths, validation evidence, blockers and next steps in the package and `execution-status.md`.

Do not equate completed copy with completed production. Every required asset must have an inspected actual file or an explicit blocked entry with reason and next action. If any required file remains blocked, report partial delivery with those exceptions, not an unqualified completed campaign; only an explicit user scope change can make a smaller delivery complete.

### Prepare a Preview Without Publishing

Collect existing content and files; preview preparation does not authorize producing missing media. Show one row/card per asset with:

| Platform | Connected account, if any | Final copy | Actual image/video file | Dimensions and format | Proposed date and time | Timezone | Review status | Missing items |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Link actual viewable files and preserve carousel order. Mark text-only items as requiring no media; mark missing files, unconnected accounts and unknown timings explicitly. Suggested times are proposals, not booked slots. An incomplete preview may help review, but remains blocked for publication. Let the user revise or choose manual delivery. Do not publish, schedule, or upload publicly during this stage.

### Publish or Schedule After Review

First verify the intended account connection and relevant permissions with an authorized safe read. Then show the final preview and obtain separate, direct approval immediately before each operation under the final approval gate below. Name the platform, account, exact material/version and date/time/timezone. Previous text, tool, connection, preview or analytics approvals do not authorize publication. Report actual results and available links/IDs; reconcile partial or ambiguous outcomes without automatic duplicate publishing.

### Follow Results

Check for a connection that can read analytics, and obtain permission before access unless already granted for that scope. Identify the period, timezone and posts to analyze before reading; ask only for missing essential scope. Use only actually available metrics, distinguish measured data from inferences and recommendations, and follow the analytics guidance below. Suggest improvements and repurposing grounded in those results, without inventing metrics or trends.

### Short Behavioral Examples

For a campaign that actually includes an Instagram carousel and Reel plus LinkedIn copy, with feasible production routes:

«اكتملت حملة Instagram وLinkedIn. ماذا تريد الآن؟
1. استلام النصوص فقط — تسليم المنشورات ونصوص الشرائح والسيناريو.
2. تصميم شرائح Instagram — إنشاء ملفات صور الشرائح.
3. إنتاج Reel — إنشاء ملف الفيديو الفعلي.
4. إنتاج جميع المواد — تجهيز كل الملفات المطلوبة للحملة.
5. تجهيز معاينة للنشر — عرض النصوص والملفات قبل أي نشر.»

After choosing Instagram slides, only if tool discovery confirms the capability and potential credit usage:

«وجدت أداة image_gen. يمكنها إنشاء سبع شرائح بنسبة 4:5. قد تستخدم من رصيد التوليد. هل تسمح باستخدامها؟»

If credit information is unavailable, replace that sentence with «استهلاك الأرصدة غير معلوم من المعلومات المتاحة.» Tool name, count and ratio must match the actual discovery and campaign, not this example.

When a directly requested video step has no production tool:

«لم أجد أداة متصلة تنتج ملف فيديو فعليًا. يمكنني تسليم السيناريو فقط، أو إرشادك لربط أداة فيديو ثم إكمال الإنتاج من هذه المرحلة.»

## Discover Before Promising

Inspect the environment's actual tool catalog and relevant connected accounts. Use available discovery facilities; do not invent tool names, integrations, API endpoints, commands, or settings. Read tool schemas and official documentation relevant to the requested operation.

For each needed capability, establish:

- Actual tool and supported operation: image/design generation, video/audio production, editing, publishing, scheduling, or account/post analytics.
- Availability of the selected platform, account identity, granted permissions, and any account-type or media restrictions supported by the documentation.
- Missing inputs, tool limits, potential charges or credits, and whether outputs become public.
- Status: verified available, connection/permission required, unavailable, or unverified.

Inspect only accounts relevant to the request. Use read-only discovery before mutations. Access to analytics does not imply publishing permission; one connected platform does not establish support for another. If cost is unknown, say so. Establish a user-approved budget or cost limit before chargeable work outside an existing authorization; stop before exceeding it. Request only the minimum scopes needed for the requested action.

## Facebook and YouTube Capability Boundaries

Inspect actual available tools and exposed account metadata before offering connection instructions for Facebook or YouTube. Establish the exact requested format and operation, not only a platform label: Facebook page post, single/multiple images or supported carousel, Reel, Story; YouTube Short, long video, thumbnail, subtitle attachment or Community Post. A tool supporting one format or operation does not establish support for the others or for every account. Use current official provider/environment documentation when needed, after identifying the actual tool; never invent endpoints, permission names or connection paths.

Follow the existing secret-free documented setup and authorized safe-read verification process. Display the verified Facebook page/account or YouTube channel identity. Confirm format-specific access and permissions when exposed; keep unknown capabilities unverified. Facebook connection or approval does not authorize Instagram, or vice versa, even within one service. YouTube channel connection does not authorize video upload.

Treat each upload (including a private/unlisted upload), publication, schedule, thumbnail/subtitle change or Community Post mutation as an external action requiring a final preview and separate direct approval immediately beforehand. Include platform, verified page/channel, asset/version, visibility and timing/timezone; validate actual required files before seeking approval. A thumbnail brief, script or prompt cannot pass as a produced file. For timestamped chapters, use measured boundaries from the final video, never a script's estimated timing. Apply partial-result reporting and safe reconciliation below without automatic reposting.

Paid advertising operations are outside this release: do not create or launch Facebook/YouTube ads or manage budgets, targeting, billing or paid campaigns. If requested, deliver an ad idea or copy labeled as a content draft only. Paid execution requires a separate future mode; ordinary campaign approval does not expand this boundary.

## Mandatory Media-Tool Choice and Approval

Before any tool creates or modifies an image, video, audio, or other media file, inspect tool descriptions/schemas without executing generation. Read-only discovery and inspection, text planning, and organizing existing files do not themselves authorize or require media generation. This gate applies to built-in, free, paid, local, and connected production tools, including tools invoked through another skill.

- **One suitable tool:** name the tool actually found, summarize what it will do and the expected files, format and dimensions/duration where relevant. Disclose known costs/credit consumption and external effects. If pricing is unknown, say it is unknown; do not assert a charge or invent an estimate. Explicitly ask permission to use that tool and wait.
- **Multiple suitable tools:** present all suitable discovered options with supported output types, material differences, known cost/credits and unknowns. Recommend the best fit with a reason. Leave the final choice to the user and wait for both choice and permission; a recommendation is not authorization.
- **No suitable tool:** name the precise missing capability and follow the documented setup process below. Do not silently substitute another deliverable or invent availability.

Example when one tool is actually found: «وجدت أداة image_gen لإنشاء الصور. سأستخدمها لإنتاج غلاف Instagram بمقاس 1080×1350. تكلفة هذا الاستخدام غير معلومة من الأدوات المتاحة. هل تسمح باستخدامها؟» Replace every detail with observed capabilities and the actual request; this example is not evidence that the tool exists or supports exact-size export.

Record approval against the selected tool, operation, inputs/versions, outputs and any budget or retry limit. An explicit approval of a disclosed multi-tool workflow may cover the named tools and steps; do not run any unapproved tool. Mere campaign approval, silence, tool availability, or an existing budget is insufficient. A prior explicit approval for this exact tool and scope remains valid; do not ask redundantly. Changed tools, scope, external effects, or costs outside authorization need renewed approval. Stop at the approved retry/budget limit; unknown pricing requires explicit acceptance of that uncertainty before use, not a guessed price. Public side effects also require the separate final publication gate.

## Missing Tools or Permissions

Identify the exact missing capability, account, or permission using observed tool results and current official documentation. Distinguish an absent tool from an installed tool with an expired connection or insufficient scope.

Explain setup step by step using the official documentation actually available for that provider and environment:

1. Suggest only tools/connections supported by accessible official documentation; never invent products or capabilities. Link the official documentation supporting the connection method and prerequisites.
2. Describe where the user starts the documented connection flow; name controls or commands only when verified.
3. Explain account selection and the minimum scopes needed for this task.
4. Have the user finish authentication through the provider's official secure flow, using OAuth when offered.
5. State the exact paused step and next verification, then wait for the user to finish installation/connection. Ask them to report completion without sharing secrets; perform the safe verification below only afterward.

Never request passwords, access tokens, API keys, client secrets, or recovery codes in chat or put them in task files. If official documentation requires a credential, direct the user to its documented secure credential interface. Do not create a substitute login form or broaden permissions to bypass failure.

If documentation cannot be accessed or does not confirm a step, state exactly what cannot be verified. Request a non-secret official help link if useful, or offer the manual fallback. Do not fill gaps with guessed instructions. This reference supplies a workflow, not a claim that any particular integration exists.

## Verify a Connection Safely

“Connected” from the user is a signal to check, not proof of access. Use a documented read-only operation to verify the intended account identity and relevant accessible resource or granted scope. Publish, upload publicly, schedule, send, or edit nothing during verification. Do not use a test post to check access.

Show the verified tool or account name and the actual granted permissions if the tool exposes them. If verification fails, explain the observed reason and next step without claiming success. Compare the result with the requested platform/account. A basic profile read verifies identity/access only; if it does not expose publishing or scheduling scopes, leave those capabilities unverified and use documented permission inspection where available. If no safe verification exists, report that limitation and pause dependent execution.

## Preserve and Resume the Task

Keep a minimal non-secret checkpoint in the conversation or an authorized local task artifact:

- Campaign brief, user profile, output mode, selected angle/platforms, and constraints.
- Current copy/asset versions and their paths or links.
- Target accounts, proposed dates/times with timezone, budget, and required permissions.
- Completed operations with returned IDs/statuses, pending operations, blocker, and next step.
- Any approval with the exact operation and version it covered; flag changes requiring new approval.

Do not store credentials or unnecessary private account data. Do not claim persistence beyond available storage. After connection verification, resume the blocked step using the checkpoint and preserve completed work. Connection approval never substitutes for approval of an external mutation. Recheck stale account, timing, cost, or asset details before execution.

## Produce, Edit, and Inspect Media

Follow the mandatory media-tool gate before production. Use only the requested scope, approved tools, and authorized cost/retry bounds. Follow relevant installed production skills when applicable without bypassing approval; do not require absent skills or tools.

For edits, locate and inspect the supplied original safely, then use that original file as the editing reference/input. Summarize requested changes, preserved elements, proposed tool, and expected output before requesting permission. If the original is unavailable, request it instead of recreating it from memory. Keep the original intact and save a new version, e.g. `image-v1.png`, `image-v2.png`, or `video-v2.mp4`; replacement needs an explicit user request. Never overwrite another final version merely to retry.

Inspect the actual resulting file before marking it ready: accessibility and decodability, dimensions, format, requested changes, Arabic spelling, connected letters/right-to-left layout, and brand/product fidelity as far as tools allow. For audio, check playability, duration, content and synchronization where relevant. Report uninspectable aspects or failed checks explicitly. A URL alone, submitted/running job, concept, prompt, or script is not a verified final asset. On failure or invalid output, say so and retain the original and checkpoint; retry only within explicit scope and bounds.

## Video Production Workflow

A writing/prompt tool produces a script or production instructions; it does not establish the ability to produce a video file. Map the request to required capabilities before committing to production:

| Capability, if requested | Verify in the actual tool description |
| --- | --- |
| Generate scenes | Actual video output, supported duration and inputs |
| Animate images | Original-image input and animated video output |
| Generate audio / voiceover | Audio or native speech output, voice/language and duration controls |
| Add subtitles | Caption generation versus actual burned or selectable subtitles, as requested |
| Edit / assemble | Combining clips, audio, timing, transitions and synchronization |
| Export | Actual supported container/codec, dimensions/aspect ratio and duration |

Do not assume one tool supports all stages. Show the proposed sequence and tools, handoff files, expected final output, and known costs/credits before starting; use the choice gate where alternatives fit, and obtain permission for every tool in the workflow. Writing can proceed within the request, but generation, audio synthesis, animation, subtitle burning, editing and rendering must stay behind the media-tool gate. Do not silently downgrade a finished-video request to a script.

After rendering, verify the actual file exists and is accessible, valid/playable video, with format, duration, dimensions, and an audio stream when expected; inspect sound and synchronization when tools permit. Distinguish intentionally silent output from missing requested voiceover. Mark incomplete or unverified properties explicitly, and do not call a video complete if a required property failed or cannot be confirmed. A script, prompt, preview still, or job ID alone must remain labeled as such. If no video production tool exists, follow documented connection steps and resume the pending production stage after safe verification and tool approval.

## Operating States and Checkpoints

Use these explicit operating states, separate from editorial quality and per-deliverable status. Record the current state and next action in the conversation or the authorized package's `execution-status.md`; keep independent deliverables progressing where possible.

| State | Exit condition / next step |
| --- | --- |
| يحتاج إلى اختيار الخطوة التالية | Plan/content package complete; present only applicable next-step choices |
| متوقف باختيار المستخدم | Preserve checkpoint; resume only when requested |
| الأدوات جاهزة | Needed capabilities verified; inspect existing approval or present the tool-use gate |
| يحتاج إلى اختيار أداة | User selects from disclosed suitable options; obtain permission if not included |
| يحتاج إلى موافقة على استخدام الأداة | Wait for explicit permission for the disclosed tool/scope |
| يحتاج إلى تثبيت أداة أو ربط حساب | Give verified setup steps and wait at the saved checkpoint |
| جارٍ التحقق من الاتصال | Perform safe read; report identity/available scopes or failure |
| جاهز للمعاينة | Required files/content verified; show final preview |
| يحتاج إلى موافقة على النشر أو الجدولة | Wait for immediate approval of the exact external operation; also use for external edits |
| قيد التنفيذ | Approved action started; keep job/resource IDs and observed state |
| مكتمل | Every requested deliverable/action verified; manual delivery complete only if that is the agreed scope |
| نجاح جزئي | Some requested items succeeded; identify remaining items and reasons |
| فشل آمن | Affected action stopped safely; record failure or unresolved result and recovery step |
| وضع بديل للتسليم اليدوي | Deliver available files/copy and identify missing production or manual steps |

Transitions follow evidence, not elapsed time or an unverified «تم». After a blocker is resolved, restore the checkpoint, verify any connection, revisit only stale approvals/details, and continue the pending stage inside the same campaign package. Do not re-ask for the whole brief, regenerate completed files, repeat successful posts, or call a partial campaign complete.

## Saved Campaign Package

Create a package only when the user requests a complete campaign saved to files; text-only delivery without a save request stays in the conversation. Use one clear, filesystem-safe campaign slug under `output/`, with no personal identifiers or path traversal. Use a unique suffix for a different campaign with the same name. Reuse the exact existing directory when resuming the same campaign.

Adapt this layout to requested platforms and deliverables; do not create unrelated platform drafts:

```text
output/<campaign-name>/
├── README.md
├── campaign.md
├── execution-status.md
├── instagram/
│   ├── scripts/
│   ├── carousel-copy.md
│   ├── caption.md
│   ├── images/
│   └── videos/
├── linkedin/
│   ├── posts.md
│   ├── images/
│   └── videos/
├── tiktok/
│   ├── scripts/
│   └── videos/
├── x/
│   └── posts.md
├── facebook/
│   ├── posts.md
│   ├── scripts/
│   ├── images/
│   └── videos/
├── youtube/
│   ├── titles-and-descriptions.md
│   ├── scripts/
│   ├── images/
│   ├── videos/
│   ├── thumbnails/
│   └── subtitles/
└── prompts/
```

- `campaign.md`: complete available plan, approved angles, platform strategy, schedule and text sources. When preserving an earlier campaign whose plan is inaccessible, explicitly record that it needs saving from that session; do not fabricate a reconstruction as the previous version.
- Platform folders: actual copy/captions with that platform; save new video scripts in `scripts/`, actual image files under `images/`, actual video files under `videos/`, actual thumbnail images under `thumbnails/`, and actual subtitle files under `subtitles/`. Create `facebook/` or `youtube/` only when that platform is used. Existing scripts may retain their paths when resuming an older package. Keep thumbnail briefs and subtitle/translation drafts as clearly labeled text, not fake media/subtitle files. Include Community Post copy only when requested and appropriate; record any execution support limitation. Add an `audio/` folder when real separate audio is requested. Empty media directories are acceptable, fake/zero-byte media or scripts renamed as media are not.
- `prompts/`: save the production prompts actually used and version associations; label unused planned prompts clearly. Include useful tool provenance for produced files without inventing it.
- `README.md`: package contents, how to use available assets, what remains, and the publication approval boundary.
- `execution-status.md`: selected route and asset subset, completed text versus pending media, deferred/excluded assets, manual-delivery choice, approval scope, stage history and next decision; update after every stage or user change. Track each requested output, current status (`مكتمل`, `بانتظار موافقة`, `يحتاج إلى أداة`, `يحتاج إلى ربط`, `فشل`, `نجاح جزئي`, `لم يبدأ`), actual file path if it exists, tool/provenance when useful, verification evidence/limitations, blocker, and next action. Include the overall operating state and resumable checkpoint. If the deliverable list is missing, mark its extent as unknown instead of inventing counts or platforms.

Save approved work incrementally in this same package after tools/accounts become available. Preserve original media and existing final files, create clear new versions, and never replace a final file without explicit user instruction. When organizing existing files, verify destination bytes (for example with hashes) before considering the move complete; do not delete unrelated output.

Keep `/output/` ignored at the repository root and all campaign/test artifacts local. Check Git tracking as well as ignore rules: ignore rules do not untrack existing files. Never stage or commit generated output. If output is already tracked, report it and arrange index-only removal within authorization, preserving local files. Do not save passwords, tokens, API keys, personal information, customer records, or sensitive client data anywhere in the package, including prompts, filenames, logs or checkpoints. Save only non-sensitive campaign copy and minimal task metadata; sanitize inputs before saving or pause a conflicting request.

## Final Preview and Approval Gate

Complete preparation and validation before asking for approval. Immediately before **each** publish, schedule, or consequential external modification (including editing/deleting a post, changing its schedule, or sending a response), show:

- Exact operation and final content, including caption, links, hashtags, and disclosures.
- Actual media attachments, their order, and a viewable preview or accessible file links.
- Platform and unambiguous target account identity.
- Publish now or exact scheduled date/time and timezone; clarify missing/ambiguous timing before scheduling.
- For modifications, the target ID/link and the precise before/after change.
- Known cost and unresolved constraints, if any.

Ask for explicit approval of that particular operation and wait. Approval to plan, prepare, generate assets, connect accounts, read analytics, or approve a campaign generally is not permission to publish or schedule. Earlier “publish everything” requests do not replace the final per-operation approval. Silence is not consent.

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

If analytics require a new permission, explain the specific scope and request separate explicit approval before acquiring it or reading analytics; do not bundle this with account connection or publishing approval. For requested analysis, use verified read permissions and the minimum necessary account/post data. Report the source, account/post IDs, date range, timezone, retrieval time, metric definitions and denominators where available, and missing data. Distinguish account totals from post metrics and organic from paid data when supplied. Do not interpret unavailable values as zero.

Keep Facebook, YouTube and each other platform's data identified separately. Use only metrics actually returned by the connected tools; do not assume a particular metric exists. Do not equate differently defined metrics across platforms, even when their labels look similar; explain definitions and comparability limits. Views alone do not prove campaign success. Present measured observations, inferences and recommendations distinctly.

Compare against a relevant baseline and campaign objective. Separate observations from hypotheses; small or incomparable samples do not prove causation. Recommend concrete changes to hooks, creative, calls to action, cadence, or repurposing, with an A/B plan and measurement window. Do not change live posts or schedules as part of reading analytics without a separate preview and approval.

If live analytics are unavailable, offer analysis of a user-provided non-secret export or a measurement template. Label the source accurately and never fabricate performance results.
