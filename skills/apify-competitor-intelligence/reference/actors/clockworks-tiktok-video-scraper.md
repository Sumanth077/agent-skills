# TikTok Video Scraper

**Actor ID:** `clockworks/tiktok-video-scraper`

Extract data from chosen TikTok videos. Just add a TikTok URL and get TikTok video and profile data: URLs, numbers of shares, followers, hashtags, hearts, video, and music metadata.

## Key Input Parameters

```json
{
  "postURLs": ["https://www.tiktok.com/@apifytech/video/7398101551744552225"],
  "scrapeRelatedVideos": false,
  "resultsPerPage": 100,
  "shouldDownloadVideos": false,
  "shouldDownloadCovers": false,
  "shouldDownloadSubtitles": false,
  "shouldDownloadSlideshowImages": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `postURLs` | array | Direct URLs of TikTok videos to scrape (required) |
| `scrapeRelatedVideos` | boolean | Scrape related videos for the post URLs (default: false) |
| `resultsPerPage` | integer | Number of related videos per post (applies when scrapeRelatedVideos is enabled, default: 1) |
| `shouldDownloadVideos` | boolean | Download TikTok videos (default: false) |
| `shouldDownloadCovers` | boolean | Download video thumbnails (default: false) |
| `shouldDownloadSubtitles` | boolean | Download video subtitles when present (default: false) |
| `shouldDownloadSlideshowImages` | boolean | Download slideshow images (default: false) |
| `videoKvStoreIdOrName` | string | Name or ID of Key-Value Store for storing videos and media (optional) |

## Output Fields

### Basic Video Information

| Field | Description |
|-------|-------------|
| `webVideoUrl` | Direct TikTok video URL |
| `url` | Post URL |
| `text` | Video caption/description |
| `id` | Video ID |
| `createTimeISO` | Timestamp (ISO format) |

### Author Information

| Field | Description |
|-------|-------------|
| `authorMeta.name` | Author username |
| `authorMeta.avatar` | Author profile picture URL |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `diggCount` | Number of likes (hearts) |
| `shareCount` | Number of shares |
| `playCount` | Number of video plays |
| `commentCount` | Number of comments |

### Video Metadata

| Field | Description |
|-------|-------------|
| `videoMeta.duration` | Video duration in seconds |

### Music Information

| Field | Description |
|-------|-------------|
| `musicMeta.musicName` | Music track name |
| `musicMeta.musicAuthor` | Music author name |
| `musicMeta.musicOriginal` | Whether music is original |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `webVideoUrl` | Video URL |
| 2 | `authorMeta.name` | Username |
| 3 | `text` | Video caption |
| 4 | `playCount` | Views |
| 5 | `diggCount` | Likes |
| 6 | `commentCount` | Comments |
| 7 | `shareCount` | Shares |
