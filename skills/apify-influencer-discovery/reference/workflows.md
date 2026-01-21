# Advanced Influencer Discovery Workflows

Multi-step workflows that combine multiple Actors for comprehensive influencer discovery and analysis.

---

## Workflow 1: Instagram Influencer Discovery by Niche

Find influencers in a specific niche using hashtags and profile analysis.

### Checklist

```
Task Progress:
- [ ] Clarify target niche/hashtags
- [ ] Step 1: Run Hashtag Scraper to find posts
- [ ] Step 2: Extract unique usernames from posts
- [ ] Step 3: Run Profile Scraper for detailed metrics
- [ ] Filter by follower count and engagement
- [ ] Export influencer list
```

### Example Interaction

**User:** "Find fitness influencers on Instagram"

**Response:**
1. Ask: "What hashtags should I search? (e.g., #fitness, #workout, #fitnessmotivation)"
2. Ask: "Minimum follower count? (default: 10,000)"
3. Step 1 - Find posts with target hashtags:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-scraper" \
  --input '{"hashtags": ["fitness", "workout"], "resultsLimit": 200}' \
  --output fitness-posts.json \
  --format json
```

4. Extract unique usernames from posts
5. Step 2 - Get profile details:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-profile-scraper" \
  --input '{"usernames": ["influencer1", "influencer2", "influencer3"]}' \
  --output fitness-influencers.csv \
  --format csv \
  --fields basic
```

6. Report: "Found 45 unique fitness influencers. Top by followers: @fitpro (500K), @workoutqueen (250K), @gymbro (100K)."

---

## Workflow 2: TikTok Creator Analysis

Analyze TikTok creators in a specific category for partnership potential.

### Checklist

```
Task Progress:
- [ ] Get target category/keywords from user
- [ ] Step 1: Search for relevant videos/profiles
- [ ] Step 2: Extract creator engagement metrics
- [ ] Calculate engagement rate (likes+comments/views)
- [ ] Rank creators by partnership potential
- [ ] Export analysis
```

### Example Interaction

**User:** "Find TikTok beauty influencers"

**Response:**
1. Ask: "Any specific keywords? (e.g., makeup tutorial, skincare routine)"
2. Run TikTok Scraper:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-scraper" \
  --input '{"hashtags": ["beautytok", "makeuptutorial"], "resultsPerPage": 100}' \
  --output beauty-tiktok.csv \
  --format csv \
  --fields basic
```

3. Report engagement metrics and top creators by follower count and engagement rate.

---

## Workflow 3: YouTube Channel Discovery

Find YouTube creators making content about specific topics.

### Checklist

```
Task Progress:
- [ ] Get topic/keywords from user
- [ ] Step 1: Run YouTube Channel Scraper
- [ ] Extract channel metrics (subscribers, views, videos)
- [ ] Filter by channel size tier
- [ ] Export creator list with contact info
```

### Example Interaction

**User:** "Find tech review YouTubers"

**Response:**
1. Ask: "What subscriber range? (micro: 10K-100K, mid: 100K-1M, macro: 1M+)"
2. Run YouTube Channel Scraper:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "streamers/youtube-channel-scraper" \
  --input '{"searchKeywords": "tech review", "maxChannels": 50}' \
  --output tech-youtubers.csv \
  --format csv \
  --fields basic
```

3. Report: "Found 50 tech review channels. Subscriber breakdown: 15 micro, 25 mid, 10 macro tier."

---

## Workflow 4: Multi-Platform Influencer Audit

Verify an influencer's presence across multiple platforms.

### Checklist

```
Task Progress:
- [ ] Get influencer username/handle
- [ ] Step 1: Check Instagram profile
- [ ] Step 2: Check TikTok profile
- [ ] Step 3: Check YouTube channel (if applicable)
- [ ] Compare metrics across platforms
- [ ] Generate authenticity report
```

### Example Interaction

**User:** "Audit @fitnessinfluencer across platforms"

**Response:**
1. Run parallel scrapers for each platform
2. Compare follower counts, engagement rates
3. Check for consistent branding and content
4. Report: "Instagram: 500K followers, 3% engagement. TikTok: 200K followers, 8% engagement. YouTube: 50K subscribers. Recommendation: Strong TikTok engagement suggests authentic audience."

---

## Workflow 5: Brand Mention Tracking

Track influencers who mention or tag a specific brand.

### Checklist

```
Task Progress:
- [ ] Get brand name/account to monitor
- [ ] Step 1: Run Tagged Scraper for brand mentions
- [ ] Step 2: Extract users who tagged the brand
- [ ] Step 3: Get profile details for top taggers
- [ ] Identify potential brand ambassadors
- [ ] Export list with engagement metrics
```

### Example Interaction

**User:** "Find influencers who tagged @brandname"

**Response:**
1. Run Instagram Tagged Scraper:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-tagged-scraper" \
  --input '{"username": "brandname", "resultsLimit": 100}' \
  --output brand-mentions.json \
  --format json
```

2. Extract unique users who created tagged posts
3. Get profile details for each user
4. Report: "Found 85 users who tagged @brandname. Top by followers: @user1 (100K), @user2 (50K). These are potential brand ambassadors already engaging with your brand."

---

## Tips for Influencer Discovery

- **Engagement Rate**: Calculate as (likes + comments) / followers. Rates above 3% are good for Instagram.
- **Authenticity Signals**: Consistent posting schedule, genuine comments, organic follower growth.
- **Micro vs Macro**: Micro-influencers (10K-100K) often have higher engagement and lower costs.
- **Platform Fit**: Match platform to target audience (TikTok for Gen Z, Instagram for millennials).
- **Content Quality**: Review recent posts for brand alignment before outreach.
