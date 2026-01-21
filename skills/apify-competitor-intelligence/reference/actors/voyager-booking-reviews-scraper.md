# Booking Reviews Scraper

**Actor ID:** `voyager/booking-reviews-scraper`

Scraper to get reviews from hotels, apartments and other accommodations listed on the Booking.com portal. Extract data using hotel URLs for review text, ratings, stars, basic reviewer info, length of stay, liked/disliked parts, room info, date of stay and more.

## Key Input Parameters

```json
{
  "startUrls": [
    {"url": "https://www.booking.com/hotel/cz/jeromehouse.en-gb.html"}
  ],
  "maxReviewsPerHotel": 9999999,
  "sortReviewsBy": "f_relevance"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | URLs of hotels to scrape reviews from (required). If you add any userData, it will be included in each review for given hotel under the key `customData` |
| `maxReviewsPerHotel` | integer | Maximum number of reviews to scrape per hotel (default: 9999999) |
| `sortReviewsBy` | string | Review attribute by which the reviews will be ordered: "f_relevance", "f_recent_desc", "f_recent_asc", "f_score_desc", "f_score_asc" (default: "f_relevance") |
| `cutoffDate` | string | If you select Sort reviews by Newest first, when the scraper encounters the first review for each hotel older than this date, it will stop, and vice versa: reviews newer than this date will be ignored when Sort reviews by Oldest first is selected. This field is ignored for other sorting options. Input the date in the UTC timezone. |
| `reviewScores` | array | Filter reviews by their score: "ALL", "review_adj_superb" (9+), "review_adj_good" (7-9), "review_adj_average_passable" (5-7), "review_adj_poor" (3-5) (default: ["ALL"]) |

## Output Fields

### Basic Review Information

| Field | Description |
|-------|-------------|
| `id` | Review ID |
| `hotelId` | Hotel identifier |
| `reviewPage` | Review page number |
| `reviewDate` | Review publication date |
| `reviewTitle` | Review title |
| `rating` | Review rating score |

### Reviewer Information

| Field | Description |
|-------|-------------|
| `userName` | Reviewer's username |
| `userLocation` | Reviewer's indicated nationality/location |

### Stay Details

| Field | Description |
|-------|-------------|
| `roomInfo` | Information about the room type stayed in |
| `stayDate` | Date of stay (e.g., "January 2022") |
| `stayLength` | Length of stay (e.g., "2 nights") |

### Review Content

| Field | Description |
|-------|-------------|
| `reviewTextParts` | Object containing review text parts |
| `reviewTextParts.Liked` | What the reviewer liked about the stay |
| `reviewTextParts.Disliked` | What the reviewer disliked about the stay |

### Custom Data

| Field | Description |
|-------|-------------|
| `customData` | Any userData provided in startUrls for identification purposes |
