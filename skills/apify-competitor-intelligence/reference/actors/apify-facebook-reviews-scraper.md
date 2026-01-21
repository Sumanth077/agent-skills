# Facebook Reviews Scraper

**Actor ID:** `apify/facebook-reviews-scraper`

Extract data from hundreds of Facebook reviews from one or multiple Facebook pages. Get review text, timestamp, review URL, likes and comments count and basic reviewer info. Download the data in JSON, CSV, Excel and use it in apps, spreadsheets, and reports.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/copperkettleyqr/reviews"}],
  "resultsLimit": 10
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Facebook Page reviews URLs in format facebook.com/pagename/reviews (required) |
| `resultsLimit` | integer | Number of results to scrape. If not set, as many results as possible will be scraped (default: not set) |

## Output Fields

### Basic Review Information

| Field | Description |
|-------|-------------|
| `facebookUrl` | Facebook page URL |
| `url` | Direct review URL |
| `id` | Review ID |
| `facebookId` | Facebook ID |
| `postFacebookId` | Post Facebook ID |
| `pageName` | Page name |
| `date` | Review timestamp (ISO format) |
| `text` | Review content |
| `isRecommended` | Whether the review is recommended (true/false) |

### Reviewer Information

| Field | Description |
|-------|-------------|
| `user` | Object with reviewer information |
| `user.id` | Reviewer ID |
| `user.name` | Reviewer name |
| `user.profileUrl` | Reviewer profile URL |
| `user.profilePic` | Reviewer profile picture URL |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `likesCount` | Number of likes on the review |
| `commentsCount` | Comment count |
