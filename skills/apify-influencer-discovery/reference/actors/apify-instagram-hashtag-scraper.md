# Instagram Hashtag Scraper

**Actor ID:** `apify/instagram-hashtag-scraper`

Scrape Instagram posts and reels by hashtags. Just add one or more hashtags and extract captions, locations, likes, plays, shares, comments count, images, timestamps, audio, and other hashtags.

## Key Input Parameters

```json
{
  "hashtags": ["webscraping"],
  "resultsType": "posts",
  "resultsLimit": 20
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `hashtags` | array | Hashtag(s) to scrape with or without # symbol (required) |
| `resultsType` | string | Choose whether to scrape "posts" or "reels" for the selected hashtags (default: "posts") |
| `resultsLimit` | integer | Maximum number of posts or reels to scrape per hashtag (default: 20) |
| `keywordSearch` | boolean | Enable to scrape by keyword instead of hashtag (default: false) |

## Output Fields

### Basic Post Information

| Field | Description |
|-------|-------------|
| `inputUrl` | Instagram hashtag URL |
| `url` | Direct post URL |
| `type` | Post type: "Image", "Video", "Sidecar" (carousel) |
| `shortCode` | Instagram post short code |
| `id` | Post ID |
| `caption` | Post caption text |
| `timestamp` | Post timestamp (ISO format) |

### Post Content

| Field | Description |
|-------|-------------|
| `hashtags` | Array of hashtags used in caption |
| `mentions` | Array of mentioned usernames |
| `displayUrl` | Main display image URL |
| `images` | Array of image URLs (for carousel posts) |
| `dimensionsHeight` | Image/video height in pixels |
| `dimensionsWidth` | Image/video width in pixels |
| `videoUrl` | Video URL (if post is a video) |
| `videoViewCount` | Number of video views (if applicable) |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `likesCount` | Number of likes |
| `commentsCount` | Number of comments |
| `firstComment` | First comment text |
| `latestComments` | Array of recent comment objects |

Comment object fields:

| Field | Description |
|-------|-------------|
| `id` | Comment ID |
| `text` | Comment text |
| `ownerUsername` | Username of commenter |
| `ownerProfilePicUrl` | Commenter's profile picture URL |
| `timestamp` | Comment timestamp (ISO format) |
| `likesCount` | Number of likes on comment |

### Author Information

| Field | Description |
|-------|-------------|
| `ownerFullName` | Post author's full name |
| `ownerUsername` | Post author's username |
| `ownerId` | Post author's ID |
| `ownerIsVerified` | Author's verification status |

### Location Information

| Field | Description |
|-------|-------------|
| `locationName` | Tagged location name |
| `locationId` | Tagged location ID |
| `locationSlug` | Location URL slug |

### Additional Metadata

| Field | Description |
|-------|-------------|
| `alt` | Alt text description |
| `isSponsored` | Sponsored content flag |
| `isAdvertisement` | Advertisement flag |
| `taggedUsers` | Array of tagged user objects |
| `commentsDisabled` | Comments disabled flag |
| `captionIsEdited` | Caption edited flag |
