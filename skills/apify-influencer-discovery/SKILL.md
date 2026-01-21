---
name: apify-influencer-discovery
description: Find and evaluate influencers for brand partnerships, verify authenticity, and track collaboration performance across Instagram, Facebook, YouTube, and TikTok.
---

# Influencer Discovery

Discover and analyze influencers across multiple platforms using Apify Actors.

## Prerequisites

- `.env` file with `APIFY_TOKEN`
- Python 3.9+ and `uv`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Determine discovery source (select Actor)
- [ ] Step 2: Read Actor schema from reference docs
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the discovery script
- [ ] Step 5: Summarize results
```

### Step 1: Determine Discovery Source

Select the appropriate Actor based on user needs:

| User Need | Actor ID | Best For | Reference Doc |
|-----------|----------|----------|---------------|
| Influencer profiles | `apify/instagram-profile-scraper` | Profile metrics, bio, follower counts | [Schema](reference/actors/apify-instagram-profile-scraper.md) |
| Find by hashtag | `apify/instagram-hashtag-scraper` | Discover influencers using specific hashtags | [Schema](reference/actors/apify-instagram-hashtag-scraper.md) |
| Reel engagement | `apify/instagram-reel-scraper` | Analyze reel performance and engagement | [Schema](reference/actors/apify-instagram-reel-scraper.md) |
| Discovery by niche | `apify/instagram-search-scraper` | Search for influencers by keyword/niche | [Schema](reference/actors/apify-instagram-search-scraper.md) |
| Brand mentions | `apify/instagram-tagged-scraper` | Track who tags brands/products | [Schema](reference/actors/apify-instagram-tagged-scraper.md) |
| Comprehensive data | `apify/instagram-scraper` | Full profile, posts, comments analysis | [Schema](reference/actors/apify-instagram-scraper.md) |
| API-based discovery | `apify/instagram-api-scraper` | Fast API-based data extraction | [Schema](reference/actors/apify-instagram-api-scraper.md) |
| Engagement analysis | `apify/export-instagram-comments-posts` | Export comments for sentiment analysis | [Schema](reference/actors/apify-export-instagram-comments-posts.md) |
| Facebook content | `apify/facebook-posts-scraper` | Analyze Facebook post performance | [Schema](reference/actors/apify-facebook-posts-scraper.md) |
| Micro-influencers | `apify/facebook-groups-scraper` | Find influencers in niche groups | [Schema](reference/actors/apify-facebook-groups-scraper.md) |
| Influential pages | `apify/facebook-search-scraper` | Search for influential pages | [Schema](reference/actors/apify-facebook-search-scraper.md) |
| YouTube creators | `streamers/youtube-channel-scraper` | Channel metrics and subscriber data | [Schema](reference/actors/streamers-youtube-channel-scraper.md) |
| TikTok influencers | `clockworks/tiktok-scraper` | Comprehensive TikTok data extraction | [Schema](reference/actors/clockworks-tiktok-scraper.md) |
| TikTok (free) | `clockworks/free-tiktok-scraper` | Free TikTok data extractor | [Schema](reference/actors/clockworks-free-tiktok-scraper.md) |
| Live streamers | `clockworks/tiktok-live-scraper` | Discover live streaming influencers | [Schema](reference/actors/clockworks-tiktok-live-scraper.md) |

### Step 2: Read Actor Schema

Read the corresponding reference doc from the table above to understand:
- Required and optional input parameters
- Output fields available
- Actor-specific requirements

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top 5 results in chat (no file saved)
   - **CSV (all data)** - Full export with all fields
   - **CSV (basic fields)** - Export with essential fields only
   - **JSON (all data)** - Full export in JSON format
2. **Output filename** (if file output selected): Suggest descriptive name based on search

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV (all data):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output OUTPUT_FILE.csv \
  --format csv
```

**CSV (basic fields):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output OUTPUT_FILE.csv \
  --format csv \
  --fields basic
```

**JSON (all data):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output OUTPUT_FILE.json \
  --format json
```

The script handles:
- Loading `APIFY_TOKEN` from `.env`
- Starting and polling the Actor run
- Downloading results in requested format (or displaying in chat)
- Reporting record count and file size

### Step 5: Summarize Results

After completion, report:
- Number of influencers found
- File location
- Key metrics available (followers, engagement rate, etc.)
- Suggested next steps (filtering, outreach, deeper analysis)

## Quick Examples

**Quick answer - display top 5 Instagram influencers in chat:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-profile-scraper" \
  --input '{"usernames": ["influencer1", "influencer2", "influencer3"]}'
```

**Hashtag discovery - CSV with basic fields:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-hashtag-scraper" \
  --input '{"hashtags": ["fitness", "workout"], "resultsLimit": 100}' \
  --output fitness-influencers.csv \
  --format csv \
  --fields basic
```

**TikTok influencer analysis - full JSON export:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-scraper" \
  --input '{"profiles": ["@creator1", "@creator2"]}' \
  --output tiktok-influencers.json \
  --format json
```

See [reference/workflows.md](reference/workflows.md) for detailed step-by-step guides for each use case.

## Error Handling

| Error | Solution |
|-------|----------|
| `APIFY_TOKEN not found` | Ask user to create `.env` with `APIFY_TOKEN=your_token` |
| `Actor not found` | Check Actor ID spelling |
| `Run FAILED` | Ask user to check Apify console link in error output |
| `Timeout` | Reduce input size or increase `--timeout` |
