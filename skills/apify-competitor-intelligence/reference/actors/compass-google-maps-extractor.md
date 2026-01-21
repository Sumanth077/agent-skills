# Google Maps Extractor

**Actor ID:** `compass/google-maps-extractor`

Extract data from hundreds of places fast. Scrape Google Maps by keyword, category, location, URLs & other filters. Get addresses, contact info, opening hours, popular times, prices, menus & more. Export scraped data, run the scraper via API, schedule and monitor runs, or integrate with other tools.

## Key Input Parameters

```json
{
  "searchStringsArray": ["restaurant"],
  "locationQuery": "New York, USA",
  "maxCrawledPlacesPerSearch": 50,
  "language": "en"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `searchStringsArray` | array | Search terms (e.g., "restaurant", "English breakfast", "pet shelter") |
| `locationQuery` | string | Location using free text (City + Country recommended) |
| `maxCrawledPlacesPerSearch` | integer | Number of results per search term/URL (leave empty to scrape all available) |
| `language` | string | Results language (default: "en") - supports 50+ languages |
| `categoryFilterWords` | array | Filter by place categories (e.g., "restaurant", "hotel", "beach club") - see 4,000+ [available categories](https://api.apify.com/v2/key-value-stores/epxZwNRgmnzzBpNJd/records/categories) |
| `placeMinimumStars` | string | Minimum star rating filter: "two", "twoAndHalf", "three", "threeAndHalf", "four", "fourAndHalf" (excludes places without reviews) |
| `website` | string | Filter by website presence: "allPlaces" (default), "withWebsite", "withoutWebsite" |
| `searchMatching` | string | Name matching: "all" (default), "only_includes", "only_exact" |
| `skipClosedPlaces` | boolean | Skip temporarily or permanently closed places (default: false) |
| `countryCode` | string | Country code filter (e.g., "us", "uk", "de") |
| `city` | string | City name (do not include state/country) |
| `state` | string | State/province name |
| `county` | string | County/regional district |
| `postalCode` | string | Postal code (combine only with countryCode, not city) |
| `customGeolocation` | object | Custom search area using coordinate pairs (format: [longitude, latitude]) |
| `startUrls` | array | Direct Google Maps URLs (max 300 results per URL) |

## Output Fields

### Basic Information

| Field | Description |
|-------|-------------|
| `title` | Business name |
| `subTitle` | Business subtitle |
| `categoryName` | Primary business category |
| `categories` | Array of all business categories |
| `description` | Place description |
| `price` | Price level information |

### Contact & Location

| Field | Description |
|-------|-------------|
| `address` | Full address with street, city, state, zip, country |
| `street` | Street address |
| `city` | City name |
| `postalCode` | Postal/ZIP code |
| `state` | State/province |
| `countryCode` | Country code |
| `neighborhood` | Neighborhood name |
| `phone` | Formatted phone number |
| `phoneUnformatted` | Phone in international format (e.g., +17183565168) |
| `website` | Website URL |
| `location` | Object with latitude (lat) and longitude (lng) coordinates |
| `plusCode` | Google Plus Code |

### Identifiers

| Field | Description |
|-------|-------------|
| `placeId` | Google Place ID |
| `cid` | Google CID (Company ID) |
| `url` | Google Maps URL |
| `searchPageUrl` | Original search page URL |

### Ratings & Reviews

| Field | Description |
|-------|-------------|
| `totalScore` | Average rating (1-5) |
| `reviewsCount` | Total number of reviews |

### Images

| Field | Description |
|-------|-------------|
| `imageUrl` | Primary image URL |
| `imagesCount` | Total number of images |

### Business Details

| Field | Description |
|-------|-------------|
| `openingHours` | Array of operating hours by day |
| `permanentlyClosed` | Boolean flag for permanently closed status |
| `temporarilyClosed` | Boolean flag for temporarily closed status |
| `claimThisBusiness` | Boolean flag indicating if business is unclaimed |

### Metadata

| Field | Description |
|-------|-------------|
| `searchString` | Original search string used |
| `rank` | Result ranking position |
| `scrapedAt` | Timestamp when place was scraped |

## Essential Fields

| Field | Description |
|-------|-------------|
| `title` | Business name |
| `url` | Google Maps link |
| `address` | Full address |
| `phone` | Phone number |
| `website` | Website URL |
| `totalScore` | Rating (1-5) |
| `reviewsCount` | Number of reviews |
| `categoryName` | Primary category |
