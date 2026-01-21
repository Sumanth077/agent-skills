# Facebook Posts Scraper

**Actor ID:** `apify/facebook-posts-scraper`

Extract data from hundreds of Facebook posts from one or multiple Facebook pages and profiles. Get post URL, post text, page or profile URL, timestamp, number of likes, shares, comments, and more.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/humansofnewyork/"}],
  "resultsLimit": 20,
  "captionText": false,
  "onlyPostsNewerThan": "2023-01-01"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Facebook page URLs (required) - only works on public pages, not personal profiles |
| `resultsLimit` | integer | Maximum number of posts to scrape (default: 20) |
| `captionText` | boolean | Extract video transcript if available (default: false) |
| `onlyPostsNewerThan` | string | Scrape posts from date to present. Formats: YYYY-MM-DD, ISO timestamp, or relative (e.g., "1 days", "2 months", "3 years", "1 hour") |
| `onlyPostsOlderThan` | string | Scrape posts from date to past. Formats: YYYY-MM-DD, ISO timestamp, or relative (e.g., "1 days", "2 months", "3 years", "1 hour") |

## Output Fields

### Basic Post Information

| Field | Description |
|-------|-------------|
| `facebookUrl` | Facebook page URL |
| `url` | Direct post URL |
| `topLevelUrl` | Top-level post URL format |
| `time` | Post timestamp in readable format (e.g., "Thursday, 6 April 2023 at 07:10") |
| `timestamp` | Post timestamp in Unix milliseconds |
| `text` | Post content/caption text |
| `postId` | Post ID |
| `postFacebookId` | Facebook post ID |

### Page Information

| Field | Description |
|-------|-------------|
| `pageName` | Name of the Facebook page |
| `pageId` | Numeric page ID |
| `facebookId` | Facebook ID |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `likes` | Number of likes on the post |
| `comments` | Number of comments on the post |
| `shares` | Number of shares on the post |

### Media Content

| Field | Description |
|-------|-------------|
| `link` | External link shared in the post (if any) |
| `thumb` | Post thumbnail image URL (if available) |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `text` | Post content |
| 2 | `url` | Post URL |
| 3 | `pageName` | Page name |
| 4 | `timestamp` | Post date/time |
| 5 | `likes` | Engagement metric |
| 6 | `comments` | Engagement metric |
| 7 | `shares` | Engagement metric |
