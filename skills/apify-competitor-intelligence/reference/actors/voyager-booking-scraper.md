# Booking.com Scraper

**Actor ID:** `voyager/booking-scraper`

Scrape hotel listings, prices, availability, and basic information from Booking.com for reputation monitoring and competitive analysis.

## Key Input Parameters

```json
{
  "search": "New York Hotels",
  "destType": "city",
  "checkIn": "2026-03-01",
  "checkOut": "2026-03-03",
  "rooms": 1,
  "adults": 2,
  "maxItems": 50,
  "sortBy": "review_score_and_price"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `search` | string | Location search query (city, region, or specific hotel name) (required) |
| `destType` | string | Destination type: "city", "region", "landmark", "district", "hotel" (default: "city") |
| `checkIn` | string | Check-in date in YYYY-MM-DD format (required) |
| `checkOut` | string | Check-out date in YYYY-MM-DD format (required) |
| `rooms` | integer | Number of rooms (default: 1) |
| `adults` | integer | Number of adults (default: 2) |
| `children` | integer | Number of children (default: 0) |
| `currency` | string | Currency code (e.g., "USD", "EUR", "GBP") (default: "USD") |
| `language` | string | Language code (e.g., "en-us", "en-gb") (default: "en-us") |
| `maxItems` | integer | Maximum number of properties to scrape (default: 50) |
| `sortBy` | string | Sort order: "popularity", "class_descending", "class_ascending", "review_score", "price", "review_score_and_price" (default: "popularity") |
| `minScore` | number | Minimum review score filter (0-10) |
| `propertyType` | array | Filter by property types: ["Hotels", "Apartments", "Resorts", "Villas", "Hostels", "Guest houses", "Bed and breakfasts"] |
| `starRating` | array | Filter by star rating: [1, 2, 3, 4, 5] |

## Output Fields

### Basic Property Information

| Field | Description |
|-------|-------------|
| `url` | Direct URL to the property on Booking.com |
| `name` | Property name |
| `type` | Property type (hotel, apartment, resort, etc.) |
| `address` | Full property address |
| `city` | City name |
| `country` | Country name |
| `zipcode` | Postal/ZIP code |
| `countryCode` | ISO country code |

### Location Details

| Field | Description |
|-------|-------------|
| `latitude` | Geographic latitude coordinate |
| `longitude` | Geographic longitude coordinate |
| `district` | District or neighborhood name |
| `distanceToCityCenter` | Distance to city center (with unit) |

### Ratings and Reviews

| Field | Description |
|-------|-------------|
| `rating` | Overall review score (0-10 scale) |
| `reviews` | Total number of reviews |
| `reviewScore` | Numeric review score |
| `reviewCount` | Review count |
| `guestReviews` | Object containing review breakdown by category |

### Pricing Information

| Field | Description |
|-------|-------------|
| `price` | Current price per night |
| `currency` | Currency code |
| `originalPrice` | Original price before discount (if applicable) |
| `pricePerNight` | Price per night value |
| `totalPrice` | Total price for entire stay |

### Property Features

| Field | Description |
|-------|-------------|
| `stars` | Star rating (1-5) |
| `facilities` | Array of available facilities/amenities |
| `description` | Property description text |
| `accommodationType` | Type of accommodation |
| `roomType` | Room type for the listed price |

### Availability

| Field | Description |
|-------|-------------|
| `available` | Boolean indicating availability |
| `urgencyMessage` | Urgency text (e.g., "Only 2 rooms left") |
| `soldOut` | Boolean indicating if property is sold out |

### Images

| Field | Description |
|-------|-------------|
| `image` | Main property image URL |
| `images` | Array of additional image URLs |

### Additional Information

| Field | Description |
|-------|-------------|
| `id` | Unique property identifier |
| `hotelId` | Booking.com hotel ID |
| `checkIn` | Check-in date used in search |
| `checkOut` | Check-out date used in search |
| `rooms` | Number of rooms searched |
| `adults` | Number of adults searched |
