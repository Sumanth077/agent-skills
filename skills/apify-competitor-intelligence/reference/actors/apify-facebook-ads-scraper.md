# Facebook Ads Scraper

**Actor ID:** `apify/facebook-ads-scraper`

Extract advertising data from Facebook, Instagram, WhatsApp, Threads, Messenger. Get ad details, publishers, prices, reach estimates, impressions, links, images, ad IDs, timestamps, and more from Meta Ad Library.

## Key Input Parameters

```json
{
  "startUrls": [{"url": "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&search_type=page&view_all_page_id=15087023444"}],
  "resultsLimit": 99999,
  "activeStatus": "active",
  "isDetailsPerAd": false,
  "onlyTotal": false
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `startUrls` | array | Meta Ad Library URL or Facebook Page URL (required) |
| `resultsLimit` | integer | Maximum number of ads to scrape (default: 99999) |
| `activeStatus` | string | Active status for ads: "active" or "inactive" (only if not specified in URL) |
| `isDetailsPerAd` | boolean | Scrape extra audience details for each ad (default: false) |
| `onlyTotal` | boolean | Return only total count of ads per page (default: false) |

## Output Fields

### Basic Ad Information

| Field | Description |
|-------|-------------|
| `adArchiveID` | Ad archive ID |
| `adArchiveId` | Ad archive ID (duplicate field) |
| `adId` | Ad ID (when available) |
| `inputUrl` | Original input URL |
| `startDateFormatted` | Ad start date (ISO format) |
| `endDateFormatted` | Ad end date (ISO format) |
| `startDate` | Ad start timestamp (Unix) |
| `endDate` | Ad end timestamp (Unix) |
| `isActive` | Whether ad is currently active |
| `categories` | Ad categories array |
| `archiveTypes` | Archive type indicators |
| `collationId` | Collation ID |
| `collationCount` | Number of collated ads |

### Page Information

| Field | Description |
|-------|-------------|
| `pageID` | Facebook page ID |
| `pageId` | Page ID (duplicate field) |
| `pageName` | Page name |
| `pageIsDeleted` | Whether page is deleted |
| `isProfilePage` | Whether this is a profile page |
| `entityType` | Entity type (e.g., "person_profile") |
| `pageInfo` | Object with detailed page information |

### Page Details Object

The `pageInfo` object contains:

| Field | Description |
|-------|-------------|
| `adLibraryPageInfo.pageInfo.pageName` | Page name |
| `adLibraryPageInfo.pageInfo.pageId` | Page ID |
| `adLibraryPageInfo.pageInfo.pageAlias` | Page alias/username |
| `adLibraryPageInfo.pageInfo.pageCategory` | Page category |
| `adLibraryPageInfo.pageInfo.pageProfileUri` | Page profile URL |
| `adLibraryPageInfo.pageInfo.pageVerification` | Verification status (e.g., "BLUE_VERIFIED") |
| `adLibraryPageInfo.pageInfo.likes` | Page likes count |
| `adLibraryPageInfo.pageInfo.igUsername` | Instagram username |
| `adLibraryPageInfo.pageInfo.igFollowers` | Instagram followers count |
| `adLibraryPageInfo.pageInfo.igVerification` | Instagram verification status |
| `page.confirmedPageOwner` | Confirmed page owner information (name, address, etc.) |
| `page.pagesTransparencyInfo.adminLocations` | Admin locations by country |

### Ad Creative & Content

| Field | Description |
|-------|-------------|
| `snapshot.body.text` | Ad text content |
| `snapshot.title` | Ad title (when available) |
| `snapshot.displayFormat` | Display format (e.g., "IMAGE", "VIDEO") |
| `snapshot.images` | Array of image objects with URLs |
| `snapshot.videos` | Array of video objects with URLs |
| `snapshot.ctaText` | Call-to-action text |
| `snapshot.ctaType` | CTA type (e.g., "NO_BUTTON", "SHOP_NOW") |
| `snapshot.linkUrl` | Destination link URL |
| `snapshot.caption` | Video/image caption |
| `snapshot.cards` | Array of carousel cards |

### Image Objects

| Field | Description |
|-------|-------------|
| `originalImageUrl` | Original high-resolution image URL |
| `resizedImageUrl` | Resized image URL |
| `watermarkedResizedImageUrl` | Watermarked version (if applicable) |
| `imageCrops` | Image crop information |

### Video Objects

| Field | Description |
|-------|-------------|
| `videoHdUrl` | HD video URL |
| `videoSdUrl` | SD video URL |
| `videoPreviewImageUrl` | Video thumbnail URL |
| `watermarkedVideoHdUrl` | Watermarked HD version |
| `watermarkedVideoSdUrl` | Watermarked SD version |

### Branded Content

| Field | Description |
|-------|-------------|
| `snapshot.brandedContent.currentPageName` | Branded content partner page name |
| `snapshot.brandedContent.pageId` | Partner page ID |
| `snapshot.brandedContent.pageCategories` | Partner page categories |
| `snapshot.brandedContent.pageProfileUri` | Partner page URL |
| `snapshot.brandedContent.pageProfilePicUrl` | Partner profile picture URL |
| `snapshot.brandedContent.pageIsDeleted` | Whether partner page is deleted |

### Publishing & Platform

| Field | Description |
|-------|-------------|
| `publisherPlatform` | Array of platforms (e.g., ["FACEBOOK"], ["INSTAGRAM"]) |
| `snapshot.currentPageName` | Current page name |
| `snapshot.pageId` | Current page ID |
| `snapshot.pageCategories` | Page categories |
| `snapshot.pageEntityType` | Page entity type |
| `snapshot.pageProfileUri` | Page profile URL |

### Performance & Reach

| Field | Description |
|-------|-------------|
| `spend` | Ad spend data (when available) |
| `currency` | Currency for spend data |
| `reachEstimate` | Estimated reach (when available) |
| `impressionsWithIndex.impressionsText` | Impressions text |
| `impressionsWithIndex.impressionsIndex` | Impressions index |

### Compliance & Safety

| Field | Description |
|-------|-------------|
| `gatedType` | Gating status (e.g., "ELIGIBLE") |
| `containsDigitalCreatedMedia` | Whether ad contains AI-generated media |
| `containsSensitiveContent` | Whether ad contains sensitive content |
| `hiddenSafetyData` | Whether safety data is hidden |
| `hideDataStatus` | Data hiding status |
| `hasUserReported` | Whether users have reported the ad |
| `reportCount` | Number of user reports |

### Political & Regulatory

| Field | Description |
|-------|-------------|
| `politicalCountries` | Array of countries for political ads |
| `stateMediaRunLabel` | State media run label |
| `snapshot.disclaimerLabel` | Disclaimer label text |
| `snapshot.countryIsoCode` | Country ISO code |
| `fevInfo` | FEV (Facebook Electoral Verification) info |
| `finservAdData` | Financial services ad data |

### Additional Details

| Field | Description |
|-------|-------------|
| `totalCount` | Total count of ads from this page |
| `totalActiveTime` | Total active time for the ad |
| `menuItems` | Array of menu items |
| `isAaaEligible` | Whether AAA (Advanced Ad Auction) eligible |
| `snapshot.isReshared` | Whether content is reshared |
| `snapshot.rootResharedPost` | Original post if reshared |
| `snapshot.event` | Event information (for event ads) |
| `snapshot.brazilTaxId` | Brazil tax ID (for Brazilian ads) |
| `snapshot.byline` | Ad byline text |

### Ad Details Object

The `ad_details` object contains additional advertiser and compliance information:

| Field | Description |
|-------|-------------|
| `ad_details.advertiser.page.about.text` | Page about text |
| `ad_details.advertiser.ad_library_page_info.page_info` | Detailed page information |
| `ad_details.advertiser.ad_library_page_info.page_spend` | Page spending information |
| `ad_details.violation_types` | Array of violation types |
| `ad_details.verified_voice_context` | Verified voice context |

## Essential Fields

For quick answers and basic data exports, these fields are most relevant (in priority order):

| Priority | Field | Description |
|----------|-------|-------------|
| 1 | `pageName` | Page running the ad |
| 2 | `snapshot.body.text` | Ad text content |
| 3 | `publisherPlatform` | Platforms where ad runs |
| 4 | `snapshot.displayFormat` | Ad format type |
| 5 | `isActive` | Current status |
| 6 | `startDateFormatted` | Start date |
| 7 | `snapshot.ctaText` | Call-to-action |
| 8 | `snapshot.linkUrl` | Destination URL |
| 9 | `snapshot.images` | Ad images |
| 10 | `spend` | Ad spend data |
