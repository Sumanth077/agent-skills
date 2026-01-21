# YouTube Comments Scraper

**Actor ID:** `streamers/youtube-comments-scraper`

This alternative YouTube Data API has no limits or quotas. Extract YouTube comments data from one or multiple YouTube videos: full comment text, posting date, author username, video title, videoId. Download YouTube comments in JSON, CSV, and Excel.

## Key Input Parameters

```json
{
  "startUrls": [
    {"url": "https://www.youtube.com/watch?v=xObhZ0Ga7EQ"}
  ],
  "maxComments": 10,
  "commentsSortBy": "1"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Enter a link to a specific Youtube video. You can also import a CSV file or Google Sheet with a list of URLs (required) |
| `maxComments` | integer | Limit the number of comments you want to scrape per video (default: 1) |
| `commentsSortBy` | string | Select Youtube sorting parameter for comments: "0" or "1" (default: "1") |

## Output Fields

### Comment Information

| Field | Description |
|-------|-------------|
| `comment` | Full comment text content |
| `cid` | Unique comment ID |
| `author` | Comment author username (e.g., "@username") |
| `voteCount` | Number of likes on the comment |
| `replyCount` | Number of replies to the comment |

### Video Context

| Field | Description |
|-------|-------------|
| `videoId` | YouTube video ID |
| `pageUrl` | Full video URL |
| `title` | Video title |
| `commentsCount` | Total number of comments on the video |

### Additional Flags

| Field | Description |
|-------|-------------|
| `authorIsChannelOwner` | Boolean indicating if comment author is the video channel owner |
| `hasCreatorHeart` | Boolean indicating if the video creator liked/hearted the comment |
| `type` | Content type (e.g., "comment") |
| `replyToCid` | Parent comment ID if this is a reply (null for top-level comments) |
