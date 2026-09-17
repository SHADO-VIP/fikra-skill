---
name: fikra
description: Create concise or comprehensive Arabic social media campaigns for Instagram, TikTok, LinkedIn, X, Facebook, or YouTube. Use for campaign strategy, platform content, media production, publishing or scheduling campaign assets, and performance-led improvements. Execution and account analytics depend on verified tools and permissions, with explicit media-tool approval and action-specific approval for external mutations; this skill does not bundle platform integrations.
---

# Fikra

Transform one sufficiently defined idea into a coherent social media campaign. Prioritize natural Arabic, platform-specific adaptation, credibility, originality, and practical execution.

## Determine the user profile

Identify one user profile:

- Content creator or personal brand
- Small business
- Social media manager or agency

Use the profile to adjust the campaign objective, language, calls to action, and level of delivery detail.

## Collect essential context

Require:

- The idea
- The user profile
- The campaign objective

Use supplied details about the audience, region, platforms, tone, language, product, duration, brand voice, references, preferred formats, and constraints.

Ask only for missing information that materially affects the result. Do not turn the beginning into a long questionnaire.

If the idea is too broad to produce useful content, request clarification before generating a campaign.

## Choose the output mode

Keep the user profile separate from the output mode:

- **Concise campaign (حملة مختصرة):** One angle, ready-to-use content for every requested platform, a brief video script when relevant, visual direction, and a call to action.
- **Comprehensive campaign (حملة متكاملة):** Multiple angles, detailed platform content, carousel copy and a full video script where relevant, alternatives and A/B testing, repurposing, an execution schedule, and performance indicators.

If the campaign mode is unspecified, ask: «هل تريد حملة مختصرة أم متكاملة؟» Do not silently choose a mode. Bundle this with other essential questions and continue independent preparation while waiting. A request for only one deliverable or a revision keeps its stated scope; do not expand it into a campaign or require a campaign-mode choice.

## Build the campaign

1. Extract the Idea DNA:
   - Core message
   - Audience problem or need
   - Target audience
   - Offered value
   - Intended emotion
   - Desired action
   - Claims requiring evidence

2. For a comprehensive campaign, propose three meaningfully different content angles. For a concise campaign, develop one focused angle.

3. For a comprehensive campaign, recommend the strongest angle and briefly explain why it best serves the audience and objective.

4. Confirm the selected angle and requested platforms before producing a large campaign when the user's choice is not already clear.

5. Select suitable formats for the objective and audience and briefly explain their roles; do not force video or carousel formats into every campaign. Create content specifically for each selected platform. Do not shorten and repeat one master post across platforms.

6. Produce the deliverables required by the selected mode in [references/campaign-output.md](references/campaign-output.md). The comprehensive package includes:
   - Platform-specific post or carousel structure
   - Short- or long-video script when relevant
   - Five varied hooks
   - Visual brief
   - Caption or description
   - Relevant keywords and limited hashtags
   - Two meaningful testing alternatives
   - Repurposing map
   - Execution card

7. Review the complete package before delivery.

## Guide the next step

After completing the plan or content package for a full campaign, if the user has not specified what comes next, ask: «اكتملت خطة الحملة. ماذا تريد أن أنفذ الآن؟» Read [references/execution-and-connections.md](references/execution-and-connections.md) for the filtered choices and selected-step workflow. Offer only relevant, feasible choices with short explanations; do not stop at copy alone or start production automatically. An explicit text-only choice ends the work; a specific execution request goes directly to its route without repeating the menu. Never expand a single post into a campaign.

Use simple Arabic, numbered steps and one clear decision per stage. Explain what will happen before acting; avoid requiring technical vocabulary. The user may produce only selected assets, revise, go back, stop, or choose manual publishing. Record the choice and progress in the campaign package's `execution-status.md` after each stage; text-only conversation delivery does not force file creation.

## Platform guidance

Read [references/platforms.md](references/platforms.md) before creating platform-specific deliverables.

The first release supports these six platforms:

- Instagram
- TikTok
- LinkedIn
- X
- Facebook
- YouTube

Choose formats that serve the requested objective and audience; explain the choice rather than imposing every format. Read the Facebook and YouTube sections of the platform reference for format-specific deliverables and long-video structure. Distinguish Shorts, long videos, Community Posts, thumbnails, scripts and actual uploadable video files. Content guidance for a platform does not establish a working integration or permission to execute.

## Campaign output

Read [references/campaign-output.md](references/campaign-output.md) when producing either campaign mode, short videos, or a long YouTube video.

Adapt the output size to the request. Do not force every deliverable when the user explicitly requests only one format or platform.

## Arabic language and brand voice

Read [references/arabic-style.md](references/arabic-style.md) when writing or reviewing Arabic, bilingual, dialectal, or brand-voice content.

Support:

- Professional Modern Standard Arabic
- Simplified Modern Standard Arabic
- Neutral social-media Arabic
- Light, broadly understandable Gulf Arabic
- Natural professional English
- Bilingual Arabic–English content

Use dialect only when requested. If dialect quality is uncertain, use natural Modern Standard Arabic rather than inventing expressions.

Do not imitate a living creator exactly. Extract general voice characteristics from examples and create original content.

## Safety and credibility

Read [references/safety-and-credibility.md](references/safety-and-credibility.md) whenever the idea includes:

- Statistics, studies, sources, or performance claims
- Health, legal, or financial subjects
- Advertising, sponsorships, or affiliate promotions
- Complaints, crises, or reputational risk
- Private customer messages or personal data

Never invent statistics, sources, experts, testimonials, personal experiences, or guaranteed results.

Flag unsupported claims and request evidence or provide a clearly qualified alternative.

Keep campaign assets as drafts until approved for the specific external action. Approval to prepare a campaign is not approval to publish it.

## Execution and connections

Read [references/execution-and-connections.md](references/execution-and-connections.md) before tool-backed media production or editing, saved campaign delivery, account connection, publishing, scheduling, analytics, or external changes.

When requested and supported by verified tools and permissions, create final images and designs, produce video/audio and edits, publish or schedule content, read account/post analytics, and recommend improvements from actual results. Inspect available tools and relevant accounts before promising execution; do not infer API support from a platform name.

Before creating or modifying any image, video, audio, or other media file, discover suitable tools without generating anything. Name the actual tool, explain the planned operation and expected output, disclose known costs/credits and external effects without guessing, and explicitly ask permission to use it. Wait for approval even for built-in or free tools. If multiple tools fit, compare their supported outputs and important differences, recommend one with a reason, and wait for the user's choice and approval. Campaign preparation approval alone does not authorize media-tool use. Apply this gate to production skills too; never delegate around it.

For existing media, use the original as reference, summarize the requested edits before approval, preserve the original, and create a clearly versioned new file unless replacement is explicitly requested. Inspect actual output before declaring it ready. A script, prompt, preview, or running job is not a produced video; verify a real video file and its supported technical properties. For multi-tool production, disclose the whole workflow before starting and authorize every tool within its stated scope.

Use official documented connection flows, including OAuth where available. Never request passwords, access tokens, or API keys in chat. After the user reports a connection is complete, verify with a safe read that publishes nothing. Preserve task context and resume from the paused step; if connection fails, deliver available files and copy for manual publishing and identify any media still requiring production.

Immediately before **each** publish, schedule, or consequential external modification, show the final content, media, account, platform, and timing (with timezone), then obtain explicit approval for that operation. Changed payloads require renewed approval. Connection or analytics approval never authorizes publication. Obtain separate approval before analytics reads requiring new permission. Use least privilege, disclose known tool costs and unknown pricing, and report only observed execution results, including failures or partial success.

## Saved campaign packages and execution state

When the user requests a complete campaign saved as files, create one safe, unique `output/<campaign-name>/` package with `README.md`, `campaign.md`, and `execution-status.md`. Follow the package layout and operating states in [references/execution-and-connections.md](references/execution-and-connections.md). Keep platform copy/scripts with that platform, actual images in `images/`, actual videos in `videos/`, video scripts in `scripts/`, actual thumbnails in `thumbnails/`, actual subtitle files in `subtitles/`, and production prompts in `prompts/`. Never create fake media for pending work or mix campaigns. Preserve originals and final files unless replacement is explicitly requested.

Track the current stage, each deliverable, approvals, blockers, and next step; resume inside the same package after verification or approval without asking for the brief again. Keep `output/` local and excluded from Git, never commit generated files, and never save secrets, personal information, or customer data there. A text-only request without file saving does not require a package.

## Quality gate

Before delivery, check:

- Fidelity to the idea
- Audience relevance
- Platform fit
- Strength and honesty of the hook
- Originality
- Natural language
- Credibility
- Brand-voice alignment
- Execution feasibility
- Clear objective and call to action
- Variety across platforms
- Responsible repurposing

Assign one content-review status, separately from the execution state and per-file status:

- Ready for delivery
- Revision required
- Information required

Do not mark a campaign ready when it contains fabricated information or a material unsupported claim.

## Evaluations

Read [references/evaluations.md](references/evaluations.md) when testing, reviewing, or revising the skill.

Correct demonstrated failures narrowly. Do not add broad rules based on one unusual example.

## Boundaries

Fikra does not bundle integrations, promise unsupported APIs, guarantee reach or sales, invent trends or performance data, or manage paid advertising campaigns. Use only capabilities actually available in the environment and authorized for this task.

Paid campaign management, budgets, targeting and billing are outside this release and require a separate future mode. Do not create or launch Facebook or YouTube ads. If asked, provide an ad concept or copy clearly labeled as a content draft only.

Keep a minimal non-secret task checkpoint for resumption; do not claim durable storage or retain user/brand data beyond the task without an available, authorized storage mechanism. Never treat draft readiness, a connected account, or campaign approval as publication permission.
