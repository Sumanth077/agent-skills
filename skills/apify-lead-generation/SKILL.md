---
name: apify-lead-generation
description: Generates B2B/B2C leads by scraping Google Maps, websites, Instagram, TikTok, Facebook, LinkedIn, YouTube, and Google Search. Use when user asks to find leads, prospects, businesses, build lead lists, enrich contacts, or scrape profiles for sales outreach.
---

# Lead Generation

Scrape leads from multiple platforms using Apify Actors.

## Prerequisites

- `.env` file with `APIFY_TOKEN`
- Python 3.9+ and `uv`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Determine lead source (select Actor)
- [ ] Step 2: Fetch Actor schema via mcpc
- [ ] Step 3: Parse input schema and output fields
- [ ] Step 4: Ask user preferences (format, filename)
- [ ] Step 5: Run the lead finder script
- [ ] Step 6: Summarize results
```

### Step 1: Determine Lead Source

Select the appropriate Actor based on user needs:

| User Need | Actor ID | Best For |
|-----------|----------|----------|
| Local businesses | `compass/crawler-google-places` | Restaurants, gyms, shops ([pricing notes](reference/gotchas/compass-crawler-google-places.md)) |
| Contact enrichment | `vdrmota/contact-info-scraper` | Emails, phones from URLs |
| Instagram profiles | `apify/instagram-profile-scraper` | Influencer discovery |
| Instagram posts/comments | `apify/instagram-scraper` | Posts, comments, hashtags, places |
| Instagram search | `apify/instagram-search-scraper` | Places, users, hashtags discovery |
| TikTok videos/hashtags | `clockworks/tiktok-scraper` | Comprehensive TikTok data extraction |
| TikTok hashtags/profiles | `clockworks/free-tiktok-scraper` | Free TikTok data extractor |
| TikTok user search | `clockworks/tiktok-user-search-scraper` | Find users by keywords |
| TikTok profiles | `clockworks/tiktok-profile-scraper` | Creator outreach |
| TikTok followers/following | `clockworks/tiktok-followers-scraper` | Audience analysis, segmentation |
| Facebook pages | `apify/facebook-pages-scraper` | Business contacts |
| Facebook page contacts | `apify/facebook-page-contact-information` | Extract emails, phones, addresses |
| Facebook groups | `apify/facebook-groups-scraper` | Buying intent signals |
| Facebook events | `apify/facebook-events-scraper` | Event networking, partnerships |
| Google Search | `apify/google-search-scraper` | Broad lead discovery |
| YouTube channels | `streamers/youtube-scraper` | Creator partnerships |
| Google Maps emails | `poidata/google-maps-email-extractor` | Direct email extraction |

### Step 2: Fetch Actor Schema via mcpc

Fetch the Actor details dynamically using mcpc:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"
```

This returns:
- **Input schema**: JSON schema with required/optional parameters
- **README**: Documentation with output field examples
- **Description**: Actor summary

### Step 3: Parse Input Schema and Output Fields

From the mcpc response:

1. **Input parameters**: Look in the `inputSchema` section for:
   - Required fields (check `required` array)
   - Field types and descriptions
   - Default values

2. **Output fields**: Look in the README for:
   - JSON example blocks showing output structure
   - Field descriptions in tables
   - Pick few most useful fields as "essential fields"

**Example essential fields selection:**
- For business leads: `title`, `address`, `phone`, `website`, `email`, `rating`
- For social profiles: `username`, `url`, `followers`, `bio`, `verified`
- For posts/content: `url`, `text`, `likes`, `comments`, `timestamp`

### Step 4: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top 5 results with essential fields in chat (no file saved)
   - **CSV (all data)** - Full export with all fields
   - **CSV (essential fields)** - Export with essential fields only
   - **JSON (all data)** - Full export in JSON format
2. **Output filename** (if file output selected): Suggest descriptive name based on search and use prefix with current date ("YYYY-XX-MM_process-data.csv")

### Step 5: Run the Script

**Quick answer (display in chat, no file):**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**Quick answer with essential fields filter:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --essential-fields 'field1,field2,field3'
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

**CSV (essential fields) - requires --essential-fields:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output OUTPUT_FILE.csv \
  --format csv \
  --fields basic \
  --essential-fields 'field1,field2,field3'
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

### Step 6: Summarize Results

After completion, report:
- Number of leads found
- File location
- Key fields available
- Suggested next steps (filtering, enrichment)

## Quick Examples

**Quick answer - display top 5 in chat:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/crawler-google-places" \
  --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA", "maxCrawledPlacesPerSearch": 50}' \
  --essential-fields 'title,address,phone,website,totalScore,reviewsCount'
```

**Google Maps - CSV with basic fields:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "compass/crawler-google-places" \
  --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA", "maxCrawledPlacesPerSearch": 50}' \
  --output coffee-shops-seattle.csv \
  --format csv \
  --fields basic \
  --essential-fields 'title,address,phone,website,totalScore,reviewsCount,categoryName'
```

**Contact enrichment - full JSON export:**
```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "vdrmota/contact-info-scraper" \
  --input '{"startUrls": [{"url": "https://example.com"}], "maxRequestsPerStartUrl": 20}' \
  --output contacts.json \
  --format json
```

See [reference/workflows.md](reference/workflows.md) for detailed step-by-step guides for each use case.

## Special Actor Notes

Some Actors have complex pricing or special configuration requirements. Read these before using:

- **Google Maps Scraper** (`compass/crawler-google-places`): Has tiered pricing with premium add-ons. See [pricing notes](reference/gotchas/compass-crawler-google-places.md) for cost management guidelines.

## Error Handling

| Error | Solution |
|-------|----------|
| `APIFY_TOKEN not found` | Ask user to create `.env` with `APIFY_TOKEN=your_token` |
| `Actor not found` | Check Actor ID spelling |
| `Run FAILED` | Ask user to check Apify console link in error output |
| `Timeout` | Reduce input size or increase `--timeout` |
| `--essential-fields required` | Provide comma-separated essential fields when using `--fields basic` |
