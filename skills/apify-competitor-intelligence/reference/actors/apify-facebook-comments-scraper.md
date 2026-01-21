# Facebook Comments Scraper

**Actor ID:** `apify/facebook-comments-scraper`

Extract data from hundreds of Facebook comments from one or multiple Facebook posts. Get comment text, timestamp, likes count and basic commenter info. Download the data in JSON, CSV, Excel and use it in apps, spreadsheets, and reports.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/humansofnewyork/posts/pfbid0BbKbkisExKGSKuhee9a7i86RwRuMKFC8NSkKStB7CsM3uXJuAAfZLrkcJMXxhH4Yl"}],
  "resultsLimit": 50,
  "includeNestedComments": false,
  "viewOption": "RANKED_UNFILTERED"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Facebook post URLs (posts, photos, reels, videos) (required) |
| `resultsLimit` | integer | If this limit is not set as many results as possible are returned |
| `includeNestedComments` | boolean | If checked, the actor will return up to 3 levels of comments/replies for each post. Note that each reply/comment will be returned as a separate result (default: false) |
| `viewOption` | string | Choose the way the comments are sorted: "RANKED_THREADED" (most relevant), "RECENT_ACTIVITY" (newest), "RANKED_UNFILTERED" (non-filtered) (default: "RANKED_UNFILTERED") |

## Output Fields

### Basic Comment Information

| Field | Description |
|-------|-------------|
| `facebookUrl` | Facebook post URL |
| `commentUrl` | Direct comment URL |
| `id` | Comment ID |
| `feedbackId` | Feedback ID |
| `date` | Comment timestamp (ISO format) |
| `text` | Comment text |
| `facebookId` | Facebook ID |
| `inputUrl` | Original input URL |

### Post Information

| Field | Description |
|-------|-------------|
| `postTitle` | Post title/content |
| `pageAdLibrary` | Ad library information object (is_business_page_active, id) |

### Commenter Information

| Field | Description |
|-------|-------------|
| `profileUrl` | Commenter's profile URL |
| `profilePicture` | Commenter's profile picture URL |
| `profileId` | Commenter's profile ID |
| `profileName` | Commenter's name |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `likesCount` | Number of likes on comment |
| `commentsCount` | Number of replies to this comment |

### Thread Information

| Field | Description |
|-------|-------------|
| `threadingDepth` | Comment thread depth (0 for top-level comments) |
| `replyToCommentId` | ID of the comment being replied to (for nested comments) |
| `comments` | Array of nested comment replies |

### Parent Information (for replies)

| Field | Description |
|-------|-------------|
| `parentComment` | Object with parent comment author information (author.__typename, author.name, author.short_name, author.id) |
| `parentReply` | Object with parent reply author information (author.__typename, author.name, author.gender, author.id) |
