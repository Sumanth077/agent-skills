# Instagram Post Scraper

**Actor ID:** `apify/instagram-post-scraper`

Scrape Instagram posts from profiles or specific post URLs. Extract captions, metrics, images, mentions, coauthors, recent comments, sponsored status, video duration, and views.

## Key Input Parameters

```json
{
  "username": ["natgeo", "https://www.instagram.com/natgeo/", "https://www.instagram.com/p/DLNsnpUTdVS/"],
  "resultsLimit": 24,
  "skipPinnedPosts": false,
  "onlyPostsNewerThan": "1 days"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `username` | array | Instagram usernames, profile URLs, or post URLs (required) |
| `resultsLimit` | integer | Maximum number of posts per profile (default: 24) - does not apply to post URLs |
| `skipPinnedPosts` | boolean | Skip pinned posts (default: false) |
| `onlyPostsNewerThan` | string | Extract posts newer than specified date (YYYY-MM-DD, ISO format, or relative like "1 days", "2 months", "3 years") |

## Output Fields

### Basic Post Information

| Field | Description |
|-------|-------------|
| `inputUrl` | Original input URL provided |
| `id` | Instagram post ID |
| `type` | Post type: "Image", "Video", "Sidecar" (carousel) |
| `shortCode` | Post short code |
| `url` | Direct post URL |
| `caption` | Post caption text |
| `timestamp` | Post date and time (ISO format) |
| `productType` | Product type (e.g., "clips" for reels) |
| `isPinned` | Boolean flag if post is pinned |
| `isCommentsDisabled` | Boolean flag if comments are disabled |

### Media Content

| Field | Description |
|-------|-------------|
| `displayUrl` | Main image display URL |
| `dimensionsHeight` | Image/video height in pixels |
| `dimensionsWidth` | Image/video width in pixels |
| `images` | Array of image URLs (for carousels) |
| `alt` | Alt text description |
| `videoUrl` | Video file URL (if video/reel) |
| `videoDuration` | Video duration in seconds |
| `childPosts` | Array of child post objects (for carousels) |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `likesCount` | Number of likes (-1 if hidden) |
| `commentsCount` | Total comment count |
| `videoViewCount` | Video view count (for videos) |
| `videoPlayCount` | Video play count (for videos) |

### Post Author

| Field | Description |
|-------|-------------|
| `ownerUsername` | Post owner's username |
| `ownerFullName` | Post owner's full name |
| `ownerId` | Post owner's Instagram ID |

### Social Elements

| Field | Description |
|-------|-------------|
| `hashtags` | Array of hashtags used in caption |
| `mentions` | Array of mentioned usernames |
| `taggedUsers` | Array of tagged user objects with id, username, is_verified, profile_pic_url, full_name |
| `coauthorProducers` | Array of coauthor objects with id, username, is_verified, profile_pic_url |

### Comments

| Field | Description |
|-------|-------------|
| `firstComment` | Text of first comment |
| `latestComments` | Array of latest comment objects with detailed information |

Latest comment object fields:

| Field | Description |
|-------|-------------|
| `id` | Comment ID |
| `text` | Comment text |
| `ownerUsername` | Commenter's username |
| `ownerProfilePicUrl` | Commenter's profile picture URL |
| `timestamp` | Comment timestamp (ISO format) |
| `likesCount` | Number of likes on comment |
| `repliesCount` | Number of replies to comment |
| `replies` | Array of reply objects |
| `owner` | Object with commenter details (id, username, is_verified, profile_pic_url) |

### Music & Audio

| Field | Description |
|-------|-------------|
| `musicInfo` | Object with audio information (if applicable) |
| `musicInfo.artist_name` | Artist name |
| `musicInfo.song_name` | Song title |
| `musicInfo.uses_original_audio` | Boolean flag for original audio |
| `musicInfo.should_mute_audio` | Boolean flag if audio should be muted |
| `musicInfo.audio_id` | Audio track ID |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `url` | Direct post URL |
| 2 | `caption` | Post content text |
| 3 | `timestamp` | When posted |
| 4 | `likesCount` | Engagement metric |
| 5 | `commentsCount` | Engagement metric |
| 6 | `type` | Post type |
| 7 | `ownerUsername` | Who posted it |
| 8 | `displayUrl` | Main image URL |
