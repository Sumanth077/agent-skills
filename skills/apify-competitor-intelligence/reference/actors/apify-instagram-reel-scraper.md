# Instagram Reel Scraper

**Actor ID:** `apify/instagram-reel-scraper`

Scrape or download Instagram reels. Extract caption, timestamp, transcript, hashtags, mentions, tagged users, comments, likes, shares, views, duration, and downloaded video.

## Key Input Parameters

```json
{
  "username": ["natgeo"],
  "resultsLimit": 27,
  "includeTranscript": false,
  "includeDownloadedVideo": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `username` | array | Instagram username, profile URL, ID, or reel URL (required) |
| `resultsLimit` | integer | Maximum reels per profile (default: 27) - does not apply when scraping by reel URLs |
| `skipPinnedPosts` | boolean | Skip pinned reels (default: false) |
| `includeSharesCount` | boolean | Extract shares count - paid add-on (default: false) |
| `includeTranscript` | boolean | Add reel transcript - paid add-on (default: false) |
| `includeDownloadedVideo` | boolean | Download video copy to Apify platform (stored for 3 days) - paid add-on (default: false) |
| `onlyPostsNewerThan` | string | Limit history by date (YYYY-MM-DD, ISO timestamp, or relative like "1 days", "2 months", "3 years") |

## Output Fields

### Basic Reel Information

| Field | Description |
|-------|-------------|
| `inputUrl` | Original input URL provided |
| `url` | Direct reel URL |
| `type` | Content type (typically "Video" for reels) |
| `shortCode` | Instagram reel short code |
| `id` | Reel ID |
| `caption` | Reel caption text |
| `timestamp` | Reel timestamp (ISO format) |
| `isPinned` | Boolean flag indicating if reel is pinned |

### Video Content

| Field | Description |
|-------|-------------|
| `displayUrl` | Video thumbnail/display image URL |
| `videoUrl` | Direct video URL (CDN link) |
| `videoDuration` | Video duration in seconds |
| `dimensionsHeight` | Video height in pixels |
| `dimensionsWidth` | Video width in pixels |

### Caption Content

| Field | Description |
|-------|-------------|
| `hashtags` | Array of hashtags used in caption |
| `mentions` | Array of mentioned usernames |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `likesCount` | Number of likes |
| `commentsCount` | Number of comments |
| `videoViewCount` | Number of video views |
| `sharesCount` | Number of shares (only when includeSharesCount is enabled) |

### Comments

| Field | Description |
|-------|-------------|
| `latestComments` | Array of recent comments with ownerUsername and text |

### Author Information

| Field | Description |
|-------|-------------|
| `ownerFullName` | Reel author's full name |
| `ownerUsername` | Reel author's username |
| `ownerId` | Reel author's ID |

### Tagged Users

| Field | Description |
|-------|-------------|
| `taggedUsers` | Array of tagged users in the reel |

### Add-on Features

| Field | Description |
|-------|-------------|
| `transcript` | Reel transcript (only when includeTranscript is enabled) |
| `downloadedVideoUrl` | URL to downloaded video stored on Apify platform (only when includeDownloadedVideo is enabled, expires after 3 days) |

### Status Flags

| Field | Description |
|-------|-------------|
| `isCommentsDisabled` | Boolean flag indicating if comments are disabled |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `url` | Direct reel URL |
| 2 | `ownerUsername` | Author username |
| 3 | `caption` | Reel caption |
| 4 | `videoViewCount` | Number of views |
| 5 | `likesCount` | Number of likes |
| 6 | `commentsCount` | Number of comments |
| 7 | `timestamp` | Reel date |
| 8 | `videoDuration` | Video length |
