---
name: apify-competitor-intelligence
description: Analyze competitor strategies, content, pricing, ads, and market positioning across Google Maps, Booking.com, Facebook, Instagram, YouTube, and TikTok.
---

# Competitor Intelligence

Analyze competitors using Apify Actors to extract data from multiple platforms.

## Prerequisites

- `.env` file with `APIFY_TOKEN`
- Python 3.9+ and `uv`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify competitor analysis type (select Actor)
- [ ] Step 2: Read Actor schema from reference docs
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analysis script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Competitor Analysis Type

Select the appropriate Actor based on analysis needs:

| User Need | Actor ID | Best For | Reference Doc |
|-----------|----------|----------|---------------|
| Competitor business data | `compass/crawler-google-places` | Location analysis | [Schema](reference/actors/compass-crawler-google-places.md) |
| Competitor contact discovery | `poidata/google-maps-email-extractor` | Email extraction | [Schema](reference/actors/apify-google-maps-email-extractor.md) |
| Feature benchmarking | `compass/google-maps-extractor` | Detailed business data | [Schema](reference/actors/compass-google-maps-extractor.md) |
| Competitor review analysis | `compass/Google-Maps-Reviews-Scraper` | Review comparison | [Schema](reference/actors/compass-google-maps-reviews-scraper.md) |
| Hotel competitor data | `voyager/booking-scraper` | Hotel benchmarking | [Schema](reference/actors/voyager-booking-scraper.md) |
| Hotel review comparison | `voyager/booking-reviews-scraper` | Review analysis | [Schema](reference/actors/voyager-booking-reviews-scraper.md) |
| Competitor ad strategies | `apify/facebook-ads-scraper` | Ad creative analysis | [Schema](reference/actors/apify-facebook-ads-scraper.md) |
| Competitor page metrics | `apify/facebook-pages-scraper` | Page performance | [Schema](reference/actors/apify-facebook-pages-scraper.md) |
| Competitor content analysis | `apify/facebook-posts-scraper` | Post strategies | [Schema](reference/actors/apify-facebook-posts-scraper.md) |
| Competitor reels performance | `apify/facebook-reels-scraper` | Reels analysis | [Schema](reference/actors/apify-facebook-reels-scraper.md) |
| Competitor audience analysis | `apify/facebook-comments-scraper` | Comment sentiment | [Schema](reference/actors/apify-facebook-comments-scraper.md) |
| Competitor event monitoring | `apify/facebook-events-scraper` | Event tracking | [Schema](reference/actors/apify-facebook-events-scraper.md) |
| Competitor audience overlap | `apify/facebook-followers-following-scraper` | Follower analysis | [Schema](reference/actors/apify-facebook-followers-following-scraper.md) |
| Competitor review benchmarking | `apify/facebook-reviews-scraper` | Review comparison | [Schema](reference/actors/apify-facebook-reviews-scraper.md) |
| Competitor ad monitoring | `apify/facebook-search-scraper` | Ad discovery | [Schema](reference/actors/apify-facebook-search-scraper.md) |
| Competitor profile metrics | `apify/instagram-profile-scraper` | Profile analysis | [Schema](reference/actors/apify-instagram-profile-scraper.md) |
| Competitor content monitoring | `apify/instagram-post-scraper` | Post tracking | [Schema](reference/actors/apify-instagram-post-scraper.md) |
| Competitor engagement analysis | `apify/instagram-comment-scraper` | Comment analysis | [Schema](reference/actors/apify-instagram-comment-scraper.md) |
| Competitor reel performance | `apify/instagram-reel-scraper` | Reel metrics | [Schema](reference/actors/apify-instagram-reel-scraper.md) |
| Competitor growth tracking | `apify/instagram-followers-count-scraper` | Follower tracking | [Schema](reference/actors/apify-instagram-followers-count-scraper.md) |
| Comprehensive competitor data | `apify/instagram-scraper` | Full analysis | [Schema](reference/actors/apify-instagram-scraper.md) |
| API-based competitor analysis | `apify/instagram-api-scraper` | API access | [Schema](reference/actors/apify-instagram-api-scraper.md) |
| Competitor video analysis | `streamers/youtube-scraper` | Video metrics | [Schema](reference/actors/streamers-youtube-scraper.md) |
| Competitor sentiment analysis | `streamers/youtube-comments-scraper` | Comment sentiment | [Schema](reference/actors/streamers-youtube-comments-scraper.md) |
| Competitor channel metrics | `streamers/youtube-channel-scraper` | Channel analysis | [Schema](reference/actors/streamers-youtube-channel-scraper.md) |
| TikTok competitor analysis | `clockworks/tiktok-scraper` | TikTok data | [Schema](reference/actors/clockworks-tiktok-scraper.md) |
| Competitor video strategies | `clockworks/tiktok-video-scraper` | Video analysis | [Schema](reference/actors/clockworks-tiktok-video-scraper.md) |
| Competitor TikTok profiles | `clockworks/tiktok-profile-scraper` | Profile data | [Schema](reference/actors/clockworks-tiktok-profile-scraper.md) |

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
2. **Output filename** (if file output selected): Suggest descriptive name based on analysis

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

### Step 5: Summarize Findings

After completion, report:
- Number of competitors analyzed
- File location
- Key competitive insights
- Suggested next steps (deeper analysis, benchmarking)

## Quick Examples

**Quick answer - display top 5 competitor locations in chat:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/crawler-google-places" \
  --input '{"searchStringsArray": ["pizza restaurant"], "locationQuery": "Chicago, USA", "maxCrawledPlacesPerSearch": 50}'
```

**Google Maps competitor reviews - CSV with basic fields:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/Google-Maps-Reviews-Scraper" \
  --input '{"startUrls": [{"url": "https://www.google.com/maps/place/..."}], "maxReviews": 100}' \
  --output competitor-reviews.csv \
  --format csv \
  --fields basic
```

**Instagram competitor analysis - full JSON export:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-profile-scraper" \
  --input '{"usernames": ["competitor1", "competitor2"]}' \
  --output instagram-competitors.json \
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
