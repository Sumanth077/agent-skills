# Export Instagram Comments and Posts

**Actor ID:** `apify/export-instagram-comments-posts`

Scrape Instagram posts and their comments in one run. Add a username and get post details: caption, likes, tagged users, timestamp, and comment details: text, usernames, profile pics, and likes. Export scraped data, schedule via API, and integrate with other tools or AI workflows.

## Key Input Parameters

```json
{
  "username": ["natgeo"],
  "resultsLimitPosts": 20,
  "resultsLimitComments": 10
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `username` | array | Instagram usernames to scrape (required) |
| `resultsLimitPosts` | integer | Maximum number of posts to scrape per username (default: 20, priced at $2.3 per 1000 posts) |
| `resultsLimitComments` | integer | Maximum number of comments to scrape per post (default: 10, priced at $2.3 per 1000 comments) |

## Output Fields

### Comment Details

| Field | Description |
|-------|-------------|
| `commentText` | Comment text content |
| `commentatorUserName` | Commenter's username |
| `commentatorProfilePicUrl` | Commenter's profile picture URL |

### Post Information

Each comment includes a `postInfo` object with the following fields:

#### Basic Post Information

| Field | Description |
|-------|-------------|
| `inputUrl` | Original input URL |
| `id` | Post ID |
| `type` | Post type (e.g., "Image", "Video") |
| `shortCode` | Instagram post short code |
| `caption` | Post caption text |
| `hashtags` | Array of hashtags used in caption |
| `mentions` | Array of mentioned usernames |
| `url` | Direct post URL |

#### Post Dimensions and Media

| Field | Description |
|-------|-------------|
| `dimensionsHeight` | Post image/video height in pixels |
| `dimensionsWidth` | Post image/video width in pixels |
| `displayUrl` | Main display image URL |
| `images` | Array of image URLs |
| `alt` | Alt text description |

#### Post Engagement

| Field | Description |
|-------|-------------|
| `likesCount` | Number of likes on post |

#### Post Author

| Field | Description |
|-------|-------------|
| `ownerFullName` | Post author's full name |
| `ownerUsername` | Post author's username |
| `ownerId` | Post author's ID |

#### Post Metadata

| Field | Description |
|-------|-------------|
| `timestamp` | Post timestamp (ISO format) |
| `isSponsored` | Whether the post is sponsored |

#### Tagged Users

| Field | Description |
|-------|-------------|
| `taggedUsers` | Array of tagged user objects with: `full_name`, `id`, `is_verified`, `profile_pic_url`, `username` |
