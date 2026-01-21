# Google Maps Reviews Scraper

**Actor ID:** `compass/google-maps-reviews-scraper`

Extract all reviews of Google Maps places using place URLs. Get review text, published date, response from owner, review URL, and reviewer's details. Download scraped data, run the scraper via API, schedule and monitor runs or integrate with other tools.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.google.com/maps/place/Yellowstone+National+Park/@44.5857951,-110.5140571,9z/data=!3m1!4b1!4m5!3m4!1s0x5351e55555555555:0xaca8f930348fe1bb!8m2!3d44.427963!4d-110.588455?hl=en-GB"}],
  "maxReviews": 100,
  "reviewsSort": "newest",
  "language": "en",
  "reviewsOrigin": "all",
  "personalData": true
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | List of Google Maps place URLs (required). Valid URLs must contain: `/maps/search`, `/maps/place` or `/maps/reviews` |
| `placeIds` | array | List of place IDs as alternative to URLs |
| `maxReviews` | integer | Max number of reviews per place to scrape (default: 10000000, prefill: 100). Set to 99999 for all reviews |
| `reviewsSort` | string | Sort order: "newest", "mostRelevant", "highestRanking", "lowestRanking" (default: "newest") |
| `reviewsStartDate` | string | Only scrape reviews newer than specified date. Supports absolute date (e.g. "2024-05-03") or relative date (e.g. "8 days", "3 months"). JSON input also supports time in ISO format (e.g. "2024-05-03T20:00:00") or relative (e.g. "3 hours") |
| `language` | string | Language for results (default: "en"). Supported languages include: en, af, az, id, ms, bs, ca, cs, da, de, et, es, es-419, eu, fil, fr, gl, hr, zu, is, it, sw, lv, lt, hu, nl, no, uz, pl, pt-BR, pt-PT, ro, sq, sk, sl, fi, sv, vi, tr, el, bg, ky, kk, mk, mn, ru, sr, uk, ka, hy, iw, ur, ar, fa, am, ne, hi, mr, bn, pa, gu, ta, te, kn, ml, si, th, lo, my, km, ko, ja, zh-CN, zh-TW |
| `reviewsOrigin` | string | Select review source: "all" (Google + third-party like TripAdvisor) or "google" (Google-native reviews only) (default: "all") |
| `personalData` | boolean | Include personal data about reviewer (ID, name, URL, photo URL) and review (ID, URL). Protected by GDPR (default: true) |

## Output Fields

### Review Information

| Field | Description |
|-------|-------------|
| `searchString` | Original search URL or input string |
| `reviewId` | Review ID |
| `reviewUrl` | Direct review URL |
| `reviewOrigin` | Review source (e.g. "Google") |
| `text` | Review text content |
| `textTranslated` | Translated review text (if available) |
| `stars` | Review rating (1-5 stars) |
| `rating` | Detailed rating object |
| `publishAt` | Relative publish time (e.g. "2 hours ago") |
| `publishedAtDate` | Publish date in ISO format |
| `likesCount` | Number of likes on the review |
| `visitedIn` | When the location was visited (if specified) |
| `originalLanguage` | Original language code of the review |
| `translatedLanguage` | Language code of translation (if available) |
| `isAdvertisement` | Whether the review is an advertisement |

### Reviewer Information

| Field | Description |
|-------|-------------|
| `reviewerId` | Reviewer's unique ID |
| `reviewerUrl` | Reviewer's profile URL |
| `name` | Reviewer's name |
| `reviewerNumberOfReviews` | Total number of reviews by this reviewer |
| `isLocalGuide` | Whether reviewer is a Local Guide |
| `reviewerPhotoUrl` | Reviewer's profile photo URL |

### Owner Response

| Field | Description |
|-------|-------------|
| `responseFromOwnerText` | Response text from place owner |
| `responseFromOwnerDate` | Date of owner's response |

### Review Media & Context

| Field | Description |
|-------|-------------|
| `reviewImageUrls` | Array of image URLs attached to the review |
| `reviewContext` | Additional context object |
| `reviewDetailedRating` | Detailed rating per service object |

### Place Information

| Field | Description |
|-------|-------------|
| `placeId` | Google place ID |
| `title` | Place name |
| `url` | Google Maps place URL |
| `categoryName` | Primary category |
| `categories` | Array of all categories |
| `totalScore` | Overall place rating |
| `reviewsCount` | Total number of reviews for the place |
| `location` | Object with lat/lng coordinates |
| `address` | Full address |
| `neighborhood` | Neighborhood name |
| `street` | Street address |
| `city` | City name |
| `postalCode` | Postal/ZIP code |
| `state` | State/region |
| `countryCode` | Country code (e.g. "US") |
| `price` | Price level |
| `cid` | Place CID |
| `fid` | Place FID |
| `imageUrl` | Main image URL of the place |
| `permanentlyClosed` | Whether place is permanently closed |
| `temporarilyClosed` | Whether place is temporarily closed |

### Metadata

| Field | Description |
|-------|-------------|
| `scrapedAt` | Timestamp when data was scraped (ISO format) |
| `language` | Language setting used for scraping |
