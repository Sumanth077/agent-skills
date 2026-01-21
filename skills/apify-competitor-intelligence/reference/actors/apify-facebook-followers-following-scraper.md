# Facebook Followers & Following Scraper

**Actor ID:** `apify/facebook-followers-following-scraper`

Extract data from Facebook pages and profiles about its followers and profiles it follows.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/LeonardoDiCaprio"}],
  "resultsLimit": 50,
  "followType": ""
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Valid Facebook page or profile URLs (required) |
| `resultsLimit` | integer | If this limit is not set as many results as possible are returned (default: 50) |
| `followType` | string | Select follows sub-section(s): "follower", "following", or empty string for both (default: "") |

## Output Fields

### Follower/Following Information

| Field | Description |
|-------|-------------|
| `title` | Follower/following profile title/name |
| `subtitle` | Follower/following profile subtitle |
| `url` | Follower/following profile URL |
| `image` | Profile image URL |
| `type` | Type of relation: "follower" or "following" |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `title` | Profile name |
| 2 | `url` | Profile URL |
| 3 | `type` | Follower or following |
| 4 | `subtitle` | Profile subtitle |
