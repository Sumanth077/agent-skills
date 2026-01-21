# Facebook Search Scraper

**Actor ID:** `apify/facebook-search-scraper`

Extract Facebook search data from pages that match your search query. Get page URL, address, email, website, check-ins, creation date, ad status, category, follower count, messenger link.

## Key Input Parameters

```json
{
  "categories": ["Pub"],
  "locations": ["Montreal"],
  "resultsLimit": 20
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `categories` | array | Search terms/keywords (required) - can be added one by one or in bulk |
| `locations` | array | Location filter (country, city, or province) - applied to each search term |
| `resultsLimit` | integer | Maximum number of search results to return (default: 20, max: 1000) |

## Output Fields

### Basic Page Information

| Field | Description |
|-------|-------------|
| `facebookUrl` | Original Facebook URL |
| `title` | Page name with location |
| `pageId` | Numeric page ID |
| `pageName` | Page username/handle |
| `pageUrl` | Canonical Facebook page URL |
| `facebookId` | Facebook ID |
| `categories` | Page categories array |
| `info` | Array of page information strings |

### Contact Information

| Field | Description |
|-------|-------------|
| `email` | Contact email (if available) |
| `phone` | Phone number (if available) |
| `address` | Business address with Google Maps link (if available) |
| `website` | Primary website URL |
| `messenger` | Messenger link (if available) |

### Engagement Metrics

| Field | Description |
|-------|-------------|
| `likes` | Page likes count |
| `followers` | Page followers count |

### Ratings & Reviews

| Field | Description |
|-------|-------------|
| `rating` | Page rating with review count string (e.g., "5.0 (6 Reviews)") |
| `ratingOverall` | Numeric rating value |
| `ratingCount` | Number of ratings |

### Page Details

| Field | Description |
|-------|-------------|
| `about_me` | Object with detailed about information (text, urls array) |
| `priceRange` | Price range indicator (e.g., "££") if applicable |

### Advertising Information

| Field | Description |
|-------|-------------|
| `creation_date` | Page creation date |
| `ad_status` | Current ad running status |
| `pageAdLibrary` | Ad library information object (is_business_page_active, id) |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `title` | Page name with location |
| 2 | `pageUrl` | Facebook URL |
| 3 | `email` | Email |
| 4 | `phone` | Phone |
| 5 | `website` | Website |
| 6 | `address` | Address |
| 7 | `likes` | Page likes |
| 8 | `followers` | Followers |
