# Instagram Comments Scraper

**Actor ID:** `apify/instagram-comment-scraper`

Scrape Instagram comments from posts or reels. Just add one or more Instagram post URLs to get comment text, post and comment IDs, replies, timestamp, owner IDs, usernames, profile pics. Export scraped datasets, run the scraper via API, schedule and monitor runs or integrate with other tools.

## Key Input Parameters

```json
{
  "directUrls": [
    "https://www.instagram.com/p/DN8-GjPkgjS",
    "https://www.instagram.com/reel/DDIJAfeyemG"
  ],
  "resultsLimit": 15,
  "isNewestComments": false,
  "includeNestedComments": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `directUrls` | array | Instagram posts or reels URLs to scrape comments from (required) |
| `resultsLimit` | integer | Number of comments to scrape per URL (default: 15). If you add 2 URLs with limit 5, you will extract 10 results total |
| `isNewestComments` | boolean | Extract newest comments first (for paying users only, default: false) |
| `includeNestedComments` | boolean | Include replies for each comment (for paying users only, default: false). Note: each reply will be a separate result, increasing total count |

## Output Fields

| Field | Description |
|-------|-------------|
| `id` | Comment ID |
| `postId` | Instagram post ID |
| `text` | Comment text content |
| `position` | Comment position in the list |
| `timestamp` | Comment timestamp (ISO format) |
| `ownerId` | Comment author's user ID |
| `ownerIsVerified` | Whether the comment author is verified |
| `ownerUsername` | Comment author's username |
| `ownerProfilePicUrl` | Comment author's profile picture URL |
