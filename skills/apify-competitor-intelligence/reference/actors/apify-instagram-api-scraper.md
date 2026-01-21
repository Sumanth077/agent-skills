# Instagram API Scraper

**Actor ID:** `apify/instagram-api-scraper`

Scrape and download Instagram posts, profiles, places, hashtags, photos without login. Supports search keywords and URL lists.

## Key Input Parameters

```json
{
  "directUrls": ["https://www.instagram.com/humansofny/"],
  "resultsType": "posts",
  "resultsLimit": 200
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `directUrls` | array | Instagram URLs to scrape (profiles, posts, hashtags, locations, IGTV, reels) |
| `resultsType` | string | Type of data to scrape: "posts", "comments", "details", "mentions", "reels", "stories" (default: "posts") |
| `resultsLimit` | integer | Maximum results per URL (default: 200, max 50 comments per post for comments type) |
| `onlyPostsNewerThan` | string | Limit scraping by date (YYYY-MM-DD, ISO format, or relative like "1 days", "2 months", "3 years") |
| `search` | string | Search query to find profiles, hashtags, or places |
| `searchType` | string | Type of search: "user", "hashtag", "place" (default: "hashtag") |
| `searchLimit` | integer | Number of search results to return (default: 1) |
| `addParentData` | boolean | Add metadata/data source to feed item results (default: false) |

## Output Fields

### Post Output

| Field | Description |
|-------|-------------|
| `id` | Post ID |
| `type` | Post type (Image, Video, Sidecar, etc.) |
| `shortCode` | Post short code |
| `caption` | Post caption text |
| `hashtags` | Array of hashtags in the post |
| `mentions` | Array of mentioned users |
| `url` | Direct post URL |
| `commentsCount` | Number of comments |
| `topComments` | Array of top comment objects |
| `dimensionsHeight` | Image/video height |
| `dimensionsWidth` | Image/video width |
| `displayUrl` | Main display URL |
| `images` | Array of image URLs (for carousel posts) |
| `likesCount` | Number of likes |
| `timestamp` | Post timestamp (ISO format) |
| `childPosts` | Array of child post objects (for carousel posts) |
| `ownerFullName` | Post owner's full name (available for profile feed posts) |
| `ownerUsername` | Post owner's username (available for profile feed posts) |
| `ownerId` | Post owner's ID |
| `locationName` | Location name (available for location feed posts) |
| `locationId` | Location ID (available for location feed posts) |

### Top Comment Object

| Field | Description |
|-------|-------------|
| `id` | Comment ID |
| `text` | Comment text |
| `created_at` | Comment timestamp (Unix timestamp) |
| `owner` | Object with commenter information (id, profile_pic_url, username) |

### Comment Output (when resultsType is "comments")

| Field | Description |
|-------|-------------|
| `url` | Post URL |
| `id` | Comment ID |
| `text` | Comment text |
| `created_at` | Comment timestamp (Unix timestamp) |
| `owner` | Object with commenter information (id, is_verified, profile_pic_url, username) |
| `repliesCount` | Number of replies |
| `replies` | Array of reply objects (up to 3 replies) |
| `likesCount` | Number of likes on comment |

### Reply Object

| Field | Description |
|-------|-------------|
| `id` | Reply ID |
| `text` | Reply text |
| `created_at` | Reply timestamp (Unix timestamp) |
| `owner` | Object with replier information (id, is_verified, profile_pic_url, username) |
| `likesCount` | Number of likes on reply |
