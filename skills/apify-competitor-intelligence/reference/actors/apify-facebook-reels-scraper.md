# Facebook Reels Scraper

**Actor ID:** `apify/facebook-reels-scraper`

Extract data from hundreds of Facebook reels from one or multiple Facebook pages and profiles. Get reel URL, text, page or profile URL, timestamp, number of plays and more.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/LeonardoDiCaprio/"}],
  "resultsLimit": 20
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Facebook page or profile URLs (required) |
| `resultsLimit` | integer | Number of reels to scrape. If not set, only initial page of results returned (default: 20) |
| `onlyPostsNewerThan` | string | Scrape reels from date to present. Supports YYYY-MM-DD format, full ISO timestamp (e.g., `2025-09-23T10:02:01` in UTC), or relative format (e.g., "1 days", "2 months", "3 years", "1 hour", "2 minutes") |

## Output Fields

### Basic Reel Information

| Field | Description |
|-------|-------------|
| `url` | Direct reel URL |
| `text` | Reel description/caption |
| `time` | Reel timestamp (ISO format) |
| `id` | Reel ID |
| `legacyId` | Legacy reel ID |
| `facebookUrl` | Facebook page or profile URL |

### Author Information

| Field | Description |
|-------|-------------|
| `user` | Object with author information |
| `user.id` | Reel author ID |
| `user.name` | Reel author name |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `playCount` | Number of plays/views |
| `likesCount` | Total likes |
| `sharesCount` | Share count |
| `commentsCount` | Comment count |
| `topReactionsCount` | Top reactions count |
| `reactionLikeCount` | Number of like reactions |
| `reactionLoveCount` | Number of love reactions (if available) |

### Video Information

| Field | Description |
|-------|-------------|
| `videoUrl` | Direct video URL (if available) |
| `thumbnailUrl` | Video thumbnail/cover image URL |
| `duration` | Video duration in seconds |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `url` | Reel URL |
| 2 | `text` | Caption |
| 3 | `user.name` | Author name |
| 4 | `playCount` | Views |
| 5 | `likesCount` | Likes |
| 6 | `commentsCount` | Comments |
| 7 | `time` | Publish date |
