# Competitor Intelligence Workflows

Multi-step workflows that combine multiple Actors for comprehensive competitor analysis.

---

## Workflow 1: Local Business Competitor Analysis

Analyze local competitors in a specific geographic area.

### Checklist

```
Task Progress:
- [ ] Clarify competitor type and location
- [ ] Step 1: Run Google Maps Scraper for competitor businesses
- [ ] Step 2: Run Google Maps Reviews Scraper on top competitors
- [ ] Analyze review sentiment and ratings
- [ ] Export competitor benchmarking report
```

### Example Interaction

**User:** "Analyze pizza restaurant competitors in Chicago"

**Response:**
1. Start with Google Maps to find all pizza restaurants
2. Extract top 20 competitors by reviews/ratings
3. Run Reviews Scraper on top 5 competitors
4. Compare:
   - Average ratings
   - Review volume
   - Common complaints
   - Pricing signals

---

## Workflow 2: Social Media Competitor Benchmarking

Compare competitor performance across Instagram and TikTok.

### Checklist

```
Task Progress:
- [ ] Get competitor usernames from user
- [ ] Step 1: Run Instagram Profile Scraper for metrics
- [ ] Step 2: Run Instagram Post Scraper for content analysis
- [ ] Step 3: Run TikTok Profile Scraper for comparison
- [ ] Generate comparative analysis report
```

### Example Interaction

**User:** "Compare social media presence of @competitor1, @competitor2, @competitor3"

**Response:**
1. Ask: "Should I analyze Instagram, TikTok, or both?"
2. Step 1 - Get Instagram profile metrics:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-profile-scraper" \
  --input '{"usernames": ["competitor1", "competitor2", "competitor3"]}' \
  --output instagram-profiles.json \
  --format json
```

3. Step 2 - Analyze recent posts:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "apify/instagram-scraper" \
  --input '{"directUrls": ["https://instagram.com/competitor1"], "resultsLimit": 20}' \
  --output competitor-posts.csv \
  --format csv
```

4. Report: "Competitor1 has 50K followers with 3.2% engagement rate, posting 5x/week. Competitor2 has 25K followers with 5.1% engagement rate, posting 3x/week. Top performing content types: Reels (65%), Carousels (25%), Single images (10%)."

---

## Workflow 3: Facebook Ad Strategy Analysis

Monitor and analyze competitor advertising strategies.

### Checklist

```
Task Progress:
- [ ] Get competitor page names/URLs
- [ ] Step 1: Run Facebook Ads Scraper for ad library data
- [ ] Step 2: Run Facebook Pages Scraper for page metrics
- [ ] Analyze ad creative themes and messaging
- [ ] Report on ad spend estimates and frequency
```

### Example Interaction

**User:** "What ads are my competitors running?"

**Response:**
1. Ask: "Which competitor Facebook pages should I analyze?"
2. Scrape Facebook Ad Library for active ads
3. Analyze:
   - Ad formats (video, image, carousel)
   - Key messaging themes
   - Call-to-action patterns
   - Run duration estimates

---

## Workflow 4: Hotel/Travel Competitor Analysis

Compare hotels and hospitality competitors on Booking.com.

### Checklist

```
Task Progress:
- [ ] Get competitor hotel names or location
- [ ] Step 1: Run Booking Scraper for property data
- [ ] Step 2: Run Booking Reviews Scraper for guest feedback
- [ ] Compare pricing, amenities, and ratings
- [ ] Generate competitive positioning report
```

### Example Interaction

**User:** "Compare boutique hotels in Manhattan"

**Response:**
1. Step 1 - Get hotel listings:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "voyager/booking-scraper" \
  --input '{"search": "Manhattan, New York", "maxItems": 30}' \
  --output manhattan-hotels.csv \
  --format csv
```

2. Step 2 - Analyze reviews for top competitors:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "voyager/booking-reviews-scraper" \
  --input '{"startUrls": [{"url": "https://www.booking.com/hotel/..."}], "maxReviews": 50}' \
  --output hotel-reviews.json \
  --format json
```

3. Report: "Found 30 boutique hotels. Top 5 by rating: Hotel A (9.2), Hotel B (9.0), Hotel C (8.8). Price range: $250-$450/night. Common positive themes: Location, design, service. Common complaints: Room size, noise."

---

## Workflow 5: YouTube Channel Competitor Analysis

Analyze competitor YouTube channels and content strategies.

### Checklist

```
Task Progress:
- [ ] Get competitor channel names/URLs
- [ ] Step 1: Run YouTube Channel Scraper for channel metrics
- [ ] Step 2: Run YouTube Scraper for video performance
- [ ] Step 3: Run YouTube Comments Scraper for audience sentiment
- [ ] Generate content strategy insights
```

### Example Interaction

**User:** "Analyze top 3 competitors in the tech review space"

**Response:**
1. Get channel metrics (subscribers, video count, total views)
2. Analyze recent videos for:
   - View counts and engagement
   - Upload frequency
   - Video length patterns
   - Title/thumbnail strategies
3. Analyze comments for audience sentiment

---

## Workflow 6: TikTok Competitor Content Analysis

Monitor competitor TikTok strategies and viral content.

### Checklist

```
Task Progress:
- [ ] Get competitor TikTok usernames
- [ ] Step 1: Run TikTok Profile Scraper for account metrics
- [ ] Step 2: Run TikTok Scraper for video analysis
- [ ] Identify viral content patterns
- [ ] Report on content strategy insights
```

### Example Interaction

**User:** "What content is working for my TikTok competitors?"

**Response:**
1. Step 1 - Get profile metrics:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-profile-scraper" \
  --input '{"profiles": ["competitor1", "competitor2"]}' \
  --output tiktok-profiles.json \
  --format json
```

2. Step 2 - Analyze recent videos:

```bash
uv run --with python-dotenv --with requests \
  ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.py \
  --actor "clockworks/tiktok-scraper" \
  --input '{"profiles": ["competitor1"], "resultsPerPage": 30}' \
  --output tiktok-videos.csv \
  --format csv
```

3. Report viral patterns, posting frequency, engagement rates, and content themes.

---

## Tips for Competitor Intelligence

- **Regular monitoring**: Set up periodic scrapes to track changes over time
- **Benchmark metrics**: Focus on engagement rates, not just follower counts
- **Content themes**: Identify what topics and formats perform best
- **Timing analysis**: Note posting schedules and frequency
- **Review sentiment**: Look for common complaints to find market gaps
- **Price tracking**: Monitor competitor pricing for positioning insights
