# Fast YouTube Channel Scraper

**Actor ID:** `streamers/youtube-channel-scraper`

Alternative YouTube Data API with no limits or quotas to scrape channel information, subscriber counts, and video data from YouTube channels.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.youtube.com/@Apify"}],
  "maxResults": 10,
  "maxResultsShorts": 0,
  "maxResultStreams": 0,
  "oldestPostDate": "100 days",
  "sortVideosBy": "NEWEST"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Channel URLs to scrape (required) |
| `maxResults` | integer | Number of regular videos to scrape per channel (default: 0) |
| `maxResultsShorts` | integer | Number of Shorts videos to scrape per channel (default: 0) |
| `maxResultStreams` | integer | Number of Stream videos to scrape per channel (default: 0) |
| `oldestPostDate` | string | Scrape videos published after date (YYYY-MM-DD, "1 days", "2 months", "3 years", "1 hour", "2 minutes") |
| `sortVideosBy` | string | Sort order: "NEWEST", "POPULAR", "OLDEST" |

## Output Fields

### Video Information

| Field | Description |
|-------|-------------|
| `id` | Video ID |
| `title` | Video title |
| `duration` | Video duration |
| `date` | Upload date (relative) |
| `url` | Video URL |
| `viewCount` | Number of views |
| `type` | Video type (video, short, stream) |
| `thumbnailUrl` | Video thumbnail URL |
| `order` | Result order number |

### Channel Information (Basic)

| Field | Description |
|-------|-------------|
| `channelName` | Channel name |
| `channelUsername` | Channel username |
| `channelUrl` | Channel URL |
| `fromYTUrl` | Original input URL |
| `input` | Input channel URL |

### Detailed Channel Information (aboutChannelInfo object)

| Field | Description |
|-------|-------------|
| `channelDescription` | Full channel description |
| `channelJoinedDate` | Channel creation date |
| `channelDescriptionLinks` | Array of links from channel description (text, url) |
| `channelLocation` | Channel location/country |
| `channelUsername` | Channel username |
| `channelAvatarUrl` | Channel avatar/profile picture URL |
| `channelBannerUrl` | Channel banner image URL |
| `channelTotalVideos` | Total number of videos on channel |
| `channelTotalViews` | Total channel views |
| `numberOfSubscribers` | Subscriber count |
| `isChannelVerified` | Channel verification status |
| `channelName` | Channel name |
| `channelUrl` | Channel URL |
| `channelId` | Channel ID |
| `inputChannelUrl` | Original input URL |
| `isAgeRestricted` | Age restriction status |
