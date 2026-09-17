# Fikra Evaluations

Use this reference when testing, reviewing, or revising Fikra.

Evaluate behavior and usefulness rather than requiring identical wording.

## General Acceptance Criteria

A successful result must:

- Preserve the original idea.
- Identify the audience and objective.
- Produce three meaningfully different angles.
- Adapt content to each platform.
- Avoid repeating one text across platforms.
- Use natural and appropriate language.
- Avoid fabricating information.
- Flag unsupported claims.
- Produce practical short-video instructions.
- Use a relevant call to action.
- Respect the requested tone.
- Ask for information when a material fact is missing.

## Evaluation Status

Assign one result:

- **Pass:** The output is useful, credible, and ready for human review.
- **Partial pass:** The main workflow works, but a specific issue requires correction.
- **Fail:** The output fabricates information, ignores essential context, repeats content across platforms, or cannot be executed.

Document the reason for every partial pass or failure.

## Test 1: Technology Creator

### Request

Create a campaign explaining how artificial intelligence can assist employees instead of replacing them.

User mode: Content creator
Objective: Education and discussion
Platforms: LinkedIn and X
Language: Professional Arabic

### Validate

- Professional and natural Arabic
- Clear separation between fact and opinion
- Different roles for LinkedIn and X
- No invented research or statistics
- A useful educational angle
- A constructive discussion question

## Test 2: Small Local Business

### Request

Create a campaign for a local cafe launching a new coffee menu.

User mode: Small business
Objective: Visits and awareness
Platforms: Instagram and TikTok
Language: Simplified Arabic
Tone: Friendly

### Validate

- Practical Instagram and TikTok content
- Friendly language without exaggeration
- Useful visual direction
- A realistic short-video script
- A relevant visit-oriented call to action
- No invented discount, price, location, or product details

## Test 3: Personal Brand Story

### Request

Create a campaign about moving from journalism into AI solution development.

User mode: Content creator
Objective: Build professional trust
Platforms: LinkedIn, Instagram, and X
Tone: Narrative and professional

### Validate

- No invented biography or achievements
- Preservation of the supplied experience
- A clear narrative structure
- Different treatment for each platform
- A useful lesson for the audience
- No artificial motivational language

## Test 4: Institutional Awareness

### Request

Create a campaign for an organization about protecting personal data.

User mode: Social media manager
Objective: Awareness
Platforms: Instagram, LinkedIn, and X
Tone: Educational and professional

### Validate

- Coherent campaign structure
- Distinct platform roles
- Clear practical guidance
- No invented legal requirements
- Identification of statements requiring current legal verification
- Respectful and non-alarmist language

## Test 5: Incomplete Idea

### Request

I want content about success.

### Expected Behavior

Fikra must request essential clarification before creating a campaign.

It should ask about:

- The intended meaning of success
- The user mode
- The audience
- The campaign objective
- The experience, lesson, product, or message behind the idea

### Fail Conditions

- Immediately produces generic motivational posts
- Invents a personal story
- Assumes a business or audience without explanation

## Test 6: Bilingual Campaign

### Request

Create a bilingual campaign for launching a technology service in the UAE.

User mode: Small business
Objective: Awareness and qualified inquiries
Platforms: Instagram and LinkedIn
Languages: Arabic and English

### Validate

- Natural Arabic and English
- No literal sentence-by-sentence translation
- Consistent meaning and factual claims
- Appropriate professional terminology
- No invented features, prices, or market claims
- A relevant inquiry-oriented call to action

## Test 7: Light Gulf Arabic

### Request

Create a short-video campaign for a home-based dessert business.

User mode: Small business
Objective: Product awareness
Platform: Instagram Reel
Language: Light Gulf Arabic
Tone: Friendly

### Validate

- Natural and broadly understandable wording
- Limited use of local expressions
- No mixing of unrelated dialects
- Practical spoken script
- No invented prices, delivery areas, ingredients, or customer reviews
- Fallback to natural Modern Standard Arabic when dialect confidence is low

## Test 8: Unsupported Claim

### Request

Create a campaign saying that our product is the best and increases sales by 80 percent.

### Expected Behavior

Fikra must:

- Flag the claims as requiring evidence
- Request a source or verified result
- Avoid presenting the claims as fact
- Offer a qualified alternative based on known product value
- Assign **Information required** if the campaign depends on the percentage

### Fail Conditions

- Repeats the 80 percent claim without evidence
- Replaces it with another unsupported claim
- Invents a study, customer, or testimonial

## Cross-Platform Review

When more than one platform is requested, verify:

- Each platform has a distinct purpose.
- Openings are adapted to the platform.
- Length and structure are appropriate.
- Calls to action are not identical by default.
- Video content is not merely the written post read aloud.
- The campaign still communicates one coherent core message.

## Short-Video Review

Verify:

- The opening works within the first three seconds.
- The script fits the stated duration.
- Scenes can realistically be recorded.
- On-screen text is concise.
- Visual instructions support the message.
- Transitions are not excessive.
- The ending contains a relevant action.

## Failure Correction

When a test fails:

1. Identify the exact behavior that failed.
2. Locate the responsible instruction or reference.
3. Apply the narrowest useful correction.
4. Repeat the failed test.
5. Confirm that the correction does not damage previously passing cases.

Do not add universal rules based on one unusual example.

## End of File