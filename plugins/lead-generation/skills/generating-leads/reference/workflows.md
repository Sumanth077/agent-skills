# Lead Generation Workflows

Step-by-step guides for common lead generation tasks.

---

## Workflow 1: Local Business Lead Generation

Find local businesses (restaurants, gyms, shops) with contact details.

### Checklist

```
Task Progress:
- [ ] Ask user for business type and location
- [ ] Ask user for output format (CSV/JSON)
- [ ] Run Google Maps Scraper
- [ ] Summarize results with key fields
```

### Example Interaction

**User:** "Find coffee shops in Seattle"

**Response:**
1. Ask: "Would you like the results in CSV or JSON format?"
2. Suggest filename: `coffee-shops-seattle.csv`
3. Run command:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "compass~crawler-google-places" \
  --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA", "maxCrawledPlacesPerSearch": 100, "language": "en"}' \
  --output coffee-shops-seattle.csv \
  --format csv
```

4. Report: "Found 87 coffee shops. Key fields: title, address, phone, website, rating."

---

## Workflow 2: Website Contact Enrichment

Extract contact details from a list of websites.

### Checklist

```
Task Progress:
- [ ] Collect website URLs from user
- [ ] Ask user for output format
- [ ] Run Contact Details Scraper
- [ ] Summarize emails and social profiles found
```

### Example Interaction

**User:** "Get contact info from these sites: acme.com, widgets.io"

**Response:**
1. Confirm URLs and format preference
2. Run command:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "vdrmota~contact-info-scraper" \
  --input '{"startUrls": [{"url": "https://acme.com"}, {"url": "https://widgets.io"}], "maxRequestsPerStartUrl": 20, "mergeContacts": true}' \
  --output contacts.json \
  --format json
```

3. Report: "Found 5 emails, 3 LinkedIn profiles, 2 Twitter handles."

---

## Workflow 3: Instagram Influencer Discovery

Find Instagram profiles for influencer outreach.

### Checklist

```
Task Progress:
- [ ] Get list of usernames from user
- [ ] Run Instagram Profile Scraper
- [ ] Report follower counts and engagement
```

### Example Interaction

**User:** "Get info on these Instagram accounts: humansofny, natgeo"

**Response:**
1. Run command:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "apify~instagram-profile-scraper" \
  --input '{"usernames": ["humansofny", "natgeo"]}' \
  --output instagram-profiles.csv \
  --format csv
```

2. Report: "Scraped 2 profiles. humansofny: 12.5M followers, natgeo: 283M followers."

---

## Workflow 4: TikTok Creator Research

Research TikTok creators for partnerships.

### Checklist

```
Task Progress:
- [ ] Get TikTok usernames from user
- [ ] Ask how many videos to analyze
- [ ] Run TikTok Profile Scraper
- [ ] Report engagement metrics
```

### Example Interaction

**User:** "Analyze TikTok creator @charlidamelio"

**Response:**
1. Ask: "How many recent videos should I analyze? (default: 50)"
2. Run command:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "clockworks~tiktok-profile-scraper" \
  --input '{"profiles": ["charlidamelio"], "resultsPerPage": 50}' \
  --output tiktok-charli.json \
  --format json
```

3. Report engagement summary: avg views, likes, comments per video.

---

## Workflow 5: Facebook Group Prospecting

Find buying intent in Facebook groups.

### Checklist

```
Task Progress:
- [ ] Get Facebook group URL from user
- [ ] Ask max posts to scrape
- [ ] Run Facebook Groups Scraper
- [ ] Identify posts with buying signals
```

### Example Interaction

**User:** "Find posts with buying intent in this Facebook group: [URL]"

**Response:**
1. Ask: "How many posts should I analyze? (default: 100)"
2. Run command:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "apify~facebook-groups-scraper" \
  --input '{"startUrls": [{"url": "https://www.facebook.com/groups/example"}], "maxPosts": 100}' \
  --output group-posts.json \
  --format json
```

3. Analyze posts for keywords: "looking for", "recommend", "need help", "where can I buy"

---

## Workflow 6: Facebook Event Networking

Discover networking opportunities and event-based leads through Facebook events.

### Checklist

```
Task Progress:
- [ ] Get search query or event category from user
- [ ] Ask for location/filters (optional)
- [ ] Ask max events to scrape
- [ ] Run Facebook Events Scraper
- [ ] Identify high-engagement events and organizers
```

### Example Interaction

**User:** "Find tech startup events in San Francisco"

**Response:**
1. Ask: "How many events should I scrape? (default: 50)"
2. Ask: "Would you like the results in CSV or JSON format?"
3. Run command:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "apify~facebook-events-scraper" \
  --input '{"searchQueries": ["startup tech San Francisco"], "maxEvents": 50}' \
  --output tech-events-sf.json \
  --format json
```

4. Analyze results for:
   - Events with high attendance (usersGoing, usersInterested)
   - Active organizers (check organizators array)
   - Upcoming events (isPast: false)
   - Online vs. in-person (isOnline field)
   - Contact opportunities (externalLinks, ticketsInfo)

5. Report: "Found 42 tech startup events. Top 5 by attendance: Event A (500 going), Event B (350 going)... Identified 15 active event organizers for potential partnership outreach."

### Tips
- Combine topic + location for targeted results: "marketing conference Chicago"
- Use Facebook's search filters for date ranges, then copy the filtered URL
- Check `externalLinks` for registration pages and organizer websites
- High `usersInterested` indicates strong market interest
- Contact organizers via their profile URLs for sponsorship opportunities
- Look for recurring events (check `duration` field) for ongoing engagement

---

## Workflow 7: Facebook Page Contact Extraction

Extract contact information directly from Facebook business pages.

### Checklist

```
Task Progress:
- [ ] Get Facebook page URLs or handles from user
- [ ] Ask for output format (CSV/JSON)
- [ ] Run Facebook Page Contact Information Scraper
- [ ] Report contact details found (emails, phones, addresses)
```

### Example Interaction

**User:** "Get contact information for these Facebook pages: @starbucks, @chipotle"

**Response:**
1. Ask: "Would you like the results in CSV or JSON format?"
2. Suggest filename: `facebook-page-contacts.csv`
3. Run command:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "apify~facebook-page-contact-information" \
  --input '{"pages": ["starbucks", "chipotle"], "language": "en-US"}' \
  --output facebook-page-contacts.csv \
  --format csv
```

4. Report: "Found contact details for 2 pages. Extracted: 2 email addresses, 2 phone numbers, 2 physical addresses, 2 websites."

### Tips
- Use short handles (e.g., "starbucks") or full URLs (e.g., "https://www.facebook.com/starbucks/")
- Not all pages display email or phone publicly - results vary by page completeness
- Check `likes`, `checkins`, and `rating` fields to prioritize high-value leads
- Use geographic data (city, country, latitude, longitude) for territory planning
- Combine with Facebook Pages Scraper for more comprehensive business data

---

## Workflow 8: B2B Lead List Building

Build a comprehensive B2B lead list combining multiple sources.

### Checklist

```
Task Progress:
- [ ] Clarify target industry and location
- [ ] Step 1: Run Google Maps Scraper for businesses
- [ ] Step 2: Run Contact Details Scraper on websites found
- [ ] Combine and deduplicate results
- [ ] Export final lead list
```

### Example Interaction

**User:** "Build a lead list for SaaS companies in Austin"

**Response:**
1. Start with Google Search or Maps to find companies
2. Extract websites from results
3. Run Contact Details Scraper on each website
4. Merge results into single lead list with:
   - Company name
   - Website
   - Email addresses
   - Phone numbers
   - Social profiles

---

## Workflow 9: YouTube Creator Lead Generation

Find YouTube creators making content about a specific topic.

### Checklist

```
Task Progress:
- [ ] Get topic/keyword from user
- [ ] Ask how many videos to search (default: 50)
- [ ] Run YouTube Scraper to find videos
- [ ] Extract unique channel names from results
- [ ] Run YouTube Scraper again for channel details
- [ ] Report creator stats and contact info
```

### Example Interaction

**User:** "Give me leads for YouTube creators about Claude Code"

**Response:**
1. Ask: "How many videos should I search? (default: 50)"
2. Step 1 - Find videos about the topic:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "apify~youtube-scraper" \
  --input '{"searchKeywords": ["Claude Code"], "maxResults": 50, "extendOutputFunction": "async ({ data, item, page, request, customData }) => { return item; }"}' \
  --output claude-code-videos.json \
  --format json
```

3. Extract unique channel names/URLs from results
4. Step 2 - Get detailed channel information:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/skills/generating-leads/reference/scripts/run_actor.py \
  --actor "apify~youtube-scraper" \
  --input '{"startUrls": [{"url": "https://www.youtube.com/@channel1"}, {"url": "https://www.youtube.com/@channel2"}], "maxResults": 1}' \
  --output youtube-creators.csv \
  --format csv
```

5. Report: "Found 35 unique creators making Claude Code content. Top channels by subscribers: Channel A (50K), Channel B (25K), Channel C (12K). Key fields: channelName, subscriberCount, description, email (if available)."

### Tips
- Use specific keywords to find niche creators
- Filter results by subscriber count for influencer tiers
- Look for email in channel description for outreach
- Consider engagement rate (views/subscribers) not just subscriber count

---

## Common Follow-up Actions

After generating leads, suggest:

1. **Filter results** - Remove duplicates or low-quality entries
2. **Enrich data** - Run Contact Details Scraper on websites
3. **Export to CRM** - Save as CSV for import
4. **Segment leads** - Group by location, industry, or size
