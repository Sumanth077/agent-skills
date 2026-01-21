# TikTok Live Scraper

**Actor ID:** `clockworks/tiktok-live-scraper`

Extract data from TikTok live sessions such as owner ID, profile URL, bio and followers, number of live session guests, viewers, hashtags, or time stamps.

**Note:** This actor is deprecated.

## Key Input Parameters

```json
{
  "categoryLiveUrls": ["https://www.tiktok.com/live/category/lifestyle/chatting"],
  "resultsPerPage": 100
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `categoryLiveUrls` | array | URLs of categories feed to scrape (find categories at https://www.tiktok.com/live/category). If no category is matched, the general category feed ("For You" feed) will be scraped |
| `resultsPerPage` | integer | Max number of live streams to be scraped for every search input (default: 100) |

## Output Fields

### Owner Information

| Field | Description |
|-------|-------------|
| `owner.id` | Owner ID |
| `owner.profileUrl` | Owner profile URL |
| `owner.nickname` | Owner nickname |
| `owner.avatar` | Owner avatar URL |
| `owner.bio` | Owner bio |
| `owner.following` | Number of accounts owner is following |
| `owner.followers` | Number of owner's followers |

### Live Session Information

| Field | Description |
|-------|-------------|
| `guests` | Number of guests in live session |
| `viewers` | Number of viewers |
| `hashtag` | Hashtag associated with live session |
| `timestamp` | Live session timestamp |
| `tag` | Live session tag |
