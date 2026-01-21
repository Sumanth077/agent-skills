# Fast YouTube Channel Scraper

**Actor ID:** `streamers/youtube-channel-scraper`

Scrape channel information from YouTube channels without API limitations. Extract channel details, subscriber counts, video information, and creator bios for competitive analysis and lead generation.

## Key Input Parameters

```json
{
  "startUrls": [
    {
      "url": "https://www.youtube.com/@Apify",
      "method": "GET"
    }
  ],
  "maxResults": 10,
  "maxResultsShorts": 0,
  "maxResultStreams": 0,
  "oldestPostDate": "100 days",
  "sortVideosBy": "NEWEST"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Direct URLs to YouTube channels (required). Each URL must be a public channel URL. |
| `maxResults` | integer | Maximum number of regular videos to scrape per channel (default: 0). Set to 0 to get only channel information without videos. |
| `maxResultsShorts` | integer | Maximum number of Shorts videos to scrape per channel (default: 0). |
| `maxResultStreams` | integer | Maximum number of stream videos to scrape per channel (default: 0). |
| `oldestPostDate` | string | Scrape only videos published after this date. Supports absolute dates (YYYY-MM-DD), ISO timestamps, or relative values like "1 day", "2 days", "3 months", "1 hour", "2 minutes". Note: This parameter automatically resets sorting to NEWEST. |
| `sortVideosBy` | string | Sort channel videos by: "NEWEST", "POPULAR", "OLDEST". Maps to sorting buttons on the channel's Videos, Shorts, and Live pages. |

## Output Fields

### Basic Video Information

| Field | Description |
|-------|-------------|
| `id` | YouTube video ID |
| `title` | Video title |
| `url` | Full video URL |
| `thumbnailUrl` | Video thumbnail URL |
| `duration` | Video duration (formatted as MM:SS or HH:MM:SS) |
| `date` | Publication date (relative format like "6 days ago") |
| `viewCount` | Video view count |
| `type` | Video type: "video", "short", or "stream" |
| `order` | Order position of the video in results |
| `input` | Original input channel URL that generated this result |
| `fromYTUrl` | Original YouTube URL from which this video was scraped |

### Channel Information

| Field | Description |
|-------|-------------|
| `channelName` | Channel name |
| `channelUsername` | Channel username handle (e.g., "@Apify") |
| `channelUrl` | Full channel URL |
| `channelId` | YouTube channel ID |
| `inputChannelUrl` | Original input channel URL |

### About Channel Information

All fields below are nested under the `aboutChannelInfo` object:

| Field | Description |
|-------|-------------|
| `channelDescription` | Full channel description/bio |
| `channelDescriptionLinks` | Array of link objects from channel description, each containing `text` and `url` fields |
| `channelJoinedDate` | Date when channel was created (e.g., "Jan 4, 2017") |
| `channelLocation` | Channel's location/country (if specified) |
| `channelUsername` | Channel username handle |
| `channelAvatarUrl` | Channel avatar/profile picture URL |
| `channelBannerUrl` | Channel banner image URL |
| `channelTotalVideos` | Total number of videos on the channel |
| `channelTotalViews` | Total view count across all channel videos |
| `numberOfSubscribers` | Channel subscriber count |
| `isChannelVerified` | Boolean indicating if the channel is verified |
| `channelName` | Channel name |
| `channelUrl` | Full channel URL |
| `channelId` | YouTube channel ID |
| `inputChannelUrl` | Original input channel URL |
| `isAgeRestricted` | Boolean indicating if the channel is age-restricted |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `aboutChannelInfo.channelName` | Channel name |
| 2 | `aboutChannelInfo.channelUrl` | Channel URL |
| 3 | `aboutChannelInfo.numberOfSubscribers` | Subscriber count |
| 4 | `aboutChannelInfo.channelTotalViews` | Total channel views |
| 5 | `aboutChannelInfo.channelTotalVideos` | Total videos on channel |
| 6 | `aboutChannelInfo.channelDescription` | Channel description/bio |
| 7 | `aboutChannelInfo.channelLocation` | Channel location |
| 8 | `title` | Video title (for video results) |
| 9 | `url` | Video URL (for video results) |
| 10 | `viewCount` | Video views (for video results) |
