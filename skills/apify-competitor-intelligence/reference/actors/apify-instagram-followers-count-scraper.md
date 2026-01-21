# Instagram Followers Count Scraper

**Actor ID:** `apify/instagram-followers-count-scraper`

Scrape the number of followers and follows from any Instagram profile. Monitor how these numbers change over time.

## Key Input Parameters

```json
{
  "usernames": ["humansofny"]
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `usernames` | array | Instagram usernames to get followers and following count from (required) |

## Output Fields

### Basic Profile Metrics

| Field | Description |
|-------|-------------|
| `username` | Instagram username |
| `followersCount` | Number of followers |
| `followsCount` | Number of accounts following |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `username` | Instagram username |
| 2 | `followersCount` | Number of followers |
| 3 | `followsCount` | Number following |
