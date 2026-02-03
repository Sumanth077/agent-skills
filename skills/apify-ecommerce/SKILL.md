---
name: apify-ecommerce
description: Scrape e-commerce data for pricing intelligence, customer sentiment, product research, quality analysis, and supply chain monitoring across Amazon, Walmart, eBay, IKEA, and 50+ marketplaces. Use when user asks to monitor prices, track competitors, analyze reviews, research products, find sellers, or detect unauthorized resellers.
---

# E-commerce Data Extraction

Extract product data, prices, reviews, and seller information from any e-commerce platform using Apify's E-commerce Scraping Tool.

## Prerequisites
(No need to check upfront)

- `.env` file with `APIFY_TOKEN`
- Node.js 20.6+ (for native `--env-file` support)
- `mcpc` CLI tool (for fetching Actor schemas)

## Workflow Selection

Select the workflow based on user needs:

| User Need | Workflow | Best For |
|-----------|----------|----------|
| Track competitor prices | Workflow 1: Pricing | Price monitoring, MAP compliance, dynamic pricing |
| Analyze customer feedback | Workflow 2: Sentiment | Brand perception, rating trends, review analysis |
| Research products/markets | Workflow 3: Research | Product benchmarking, category analysis, feature comparison |
| Identify quality issues | Workflow 4: Quality | Defect detection, product improvement, QA feedback |
| Monitor sellers/inventory | Workflow 5: Supply Chain | Unauthorized resellers, vendor evaluation, stock tracking |

## Workflow Progress Tracking

Copy and use this checklist:

```
Task Progress:
- [ ] Step 1: Select workflow and determine data source
- [ ] Step 2: Configure Actor input
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the extraction script
- [ ] Step 5: Summarize results
```

---

## Workflow 1: Competitive Pricing & MAP Monitoring

**Use case:** Track competitor prices, detect MAP violations, enable dynamic pricing strategies.

**Best for:** Pricing analysts, revenue managers, brand compliance teams.

### Input Options

| Input Type | Field | Description |
|------------|-------|-------------|
| Product URLs | `detailsUrls` | Direct URLs to product pages |
| Category URLs | `listingUrls` | URLs to category/search result pages |
| Keyword Search | `keyword` + `marketplaces` | Search term across selected marketplaces |

### Example Input - Product URLs
```json
{
  "detailsUrls": [
    "https://www.amazon.com/dp/B09V3KXJPB",
    "https://www.walmart.com/ip/123456789"
  ],
  "additionalProperties": true
}
```

### Example Input - Keyword Search
```json
{
  "keyword": "Samsung Galaxy S24",
  "marketplaces": ["www.amazon.com", "www.walmart.com", "www.costco.com"],
  "additionalProperties": true,
  "maxProductResults": 50
}
```

### Output Fields
- `name` - Product name
- `url` - Product URL
- `offers.price` - Current price
- `offers.priceCurrency` - Currency code
- `brand` - Brand name
- `image` - Product image URL
- Additional seller/stock info when `additionalProperties: true`

---

## Workflow 2: Customer Sentiment Analysis

**Use case:** Monitor customer sentiment from reviews, track brand perception, detect rating drops.

**Best for:** Brand managers, customer experience teams, marketing managers.

### Input Options

| Input Type | Field | Description |
|------------|-------|-------------|
| Review URLs | `reviewDetailsUrls` | Direct URLs to review pages |
| Product URLs | `reviewListingUrls` | Product pages to extract reviews from |
| Keyword Search | `keywordReviews` + `marketplacesReviews` | Search for product reviews by keyword |

### Example Input - Review Extraction
```json
{
  "reviewListingUrls": [
    "https://www.amazon.com/dp/B09V3KXJPB"
  ],
  "sortReview": "Most recent",
  "additionalReviewProperties": true,
  "maxReviewResults": 500
}
```

### Example Input - Keyword Search
```json
{
  "keywordReviews": "wireless earbuds",
  "marketplacesReviews": ["www.amazon.com"],
  "sortReview": "Most recent",
  "additionalReviewProperties": true,
  "maxReviewResults": 200
}
```

### Review Sort Options
- `Most recent` - Latest reviews first
- `Most relevant` - Platform default relevance
- `Most helpful` - Highest voted reviews
- `Highest rated` - 5-star reviews first
- `Lowest rated` - 1-star reviews first (useful for quality analysis)

### Output Fields
- Review text, rating, date, reviewer name
- Product metadata (name, brand, price)
- Seller information when available

---

## Workflow 3: Product & Market Research

**Use case:** Benchmark products, analyze category saturation, compare features and pricing.

**Best for:** Product managers, market researchers, category managers.

### Input Options

Same as Workflow 1, plus AI Summary capabilities:

| Field | Description |
|-------|-------------|
| `fieldsToAnalyze` | Data points to pass to AI summary |
| `customPrompt` | Custom AI analysis instructions |

### Example Input - Market Research with AI Summary
```json
{
  "keyword": "robot vacuum",
  "marketplaces": ["www.amazon.com", "www.walmart.com"],
  "additionalProperties": true,
  "maxProductResults": 100,
  "fieldsToAnalyze": ["name", "offers", "description", "additionalProperties"],
  "customPrompt": "Analyze pricing trends, identify feature gaps, and summarize top product positioning strategies"
}
```

### AI Summary Fields
Available fields for `fieldsToAnalyze`:
- `image` - Product images
- `url` - Product URLs
- `name` - Product names
- `offers` - Pricing data
- `brand` - Brand information
- `description` - Product descriptions
- `additionalProperties` - Extended attributes

---

## Workflow 4: Product Quality Analysis

**Use case:** Identify recurring quality issues, defect patterns, and improvement opportunities from reviews.

**Best for:** Product managers, QA teams, R&D managers.

### Input Configuration
Use Workflow 2 (Sentiment) inputs with these recommendations:

```json
{
  "reviewListingUrls": [
    "https://www.amazon.com/dp/YOUR_PRODUCT_ASIN"
  ],
  "sortReview": "Lowest rated",
  "additionalReviewProperties": true,
  "maxReviewResults": 1000
}
```

### Analysis Tips
- Use `sortReview: "Lowest rated"` to prioritize negative feedback
- Set high `maxReviewResults` for statistical significance
- Cross-reference with competitor products for benchmarking
- Look for recurring keywords: "broke", "defect", "quality", "returned"

---

## Workflow 5: Supply Chain & Seller Intelligence

**Use case:** Monitor marketplace sellers, detect unauthorized resellers, evaluate vendor performance.

**Best for:** Brand protection teams, procurement, supply chain managers.

### Input Options

| Input Type | Field | Description |
|------------|-------|-------------|
| Seller URLs | `sellerUrls` | Direct seller profile URLs |
| Google Shopping | Multiple fields | Search for sellers across stores |

### Example Input - Seller Profiles
```json
{
  "sellerUrls": [
    "https://www.amazon.com/sp?seller=A1B2C3D4E5"
  ],
  "maxSellerResults": 50
}
```

### Example Input - Google Shopping Sellers
```json
{
  "googleShoppingSearchKeyword": "Nike Air Max 90",
  "scrapeSellersFromGoogleShopping": true,
  "countryCode": "us",
  "maxGoogleShoppingSellersPerProduct": 20,
  "maxGoogleShoppingResults": 100
}
```

### Google Shopping Options
- `scrapeProductsFromGoogleShopping` - Extract product details
- `scrapeSellersFromGoogleShopping` - Extract seller/store list
- `scrapeReviewsFromGoogleShopping` - Extract reviews
- `countryCode` - Target country (affects currency, availability)

---

## Supported Marketplaces

### Amazon (20+ regions)
`www.amazon.com`, `www.amazon.co.uk`, `www.amazon.de`, `www.amazon.fr`, `www.amazon.it`, `www.amazon.es`, `www.amazon.ca`, `www.amazon.com.au`, `www.amazon.co.jp`, `www.amazon.in`, `www.amazon.com.br`, `www.amazon.com.mx`, `www.amazon.nl`, `www.amazon.pl`, `www.amazon.se`, `www.amazon.ae`, `www.amazon.sa`, `www.amazon.sg`, `www.amazon.com.tr`, `www.amazon.eg`

### Major US Retailers
`www.walmart.com`, `www.costco.com`, `www.costco.ca`, `www.homedepot.com`

### European Retailers
`allegro.pl`, `allegro.cz`, `allegro.sk`, `www.alza.cz`, `www.alza.sk`, `www.alza.de`, `www.alza.at`, `www.alza.hu`, `www.kaufland.de`, `www.kaufland.pl`, `www.kaufland.cz`, `www.kaufland.sk`, `www.kaufland.at`, `www.kaufland.fr`, `www.kaufland.it`, `www.cdiscount.com`

### IKEA (40+ country/language combinations)
Supports all major IKEA regional sites with multiple language options.

### Other
`www.coles.com.au` (Australia)

---

## Running the Extraction

### Step 1: Fetch Actor Schema (optional)
```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="apify/e-commerce-scraping-tool" | jq -r ".content"
```

### Step 2: Ask User Preferences
1. **Output format:**
   - **Quick answer** - Display top results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Filename** - Descriptive name with date prefix

### Step 3: Run the Script

**Quick answer (display in chat):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "apify/e-commerce-scraping-tool" \
  --input 'JSON_INPUT'
```

**CSV export:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "apify/e-commerce-scraping-tool" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_filename.csv \
  --format csv
```

**JSON export:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "apify/e-commerce-scraping-tool" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_filename.json \
  --format json
```

### Step 4: Summarize Results

After completion, report:
- Number of items extracted (products, reviews, or sellers)
- File location and name
- Key insights based on the workflow:
  - **Pricing:** Price range, outliers, potential MAP violations
  - **Sentiment:** Average rating, sentiment trends, common themes
  - **Research:** Feature gaps, pricing bands, market positioning
  - **Quality:** Recurring issues, defect patterns, improvement areas
  - **Supply Chain:** Seller count, unauthorized sellers, inventory status

---

## Error Handling

| Error | Solution |
|-------|----------|
| `APIFY_TOKEN not found` | Create `.env` file with `APIFY_TOKEN=your_token` |
| `mcpc not found` | Install with `npm install -g @apify/mcpc` |
| `Actor not found` | Verify Actor ID: `apify/e-commerce-scraping-tool` |
| `Run FAILED` | Check Apify console link in error output for details |
| `Timeout` | Reduce `maxProductResults` or increase `--timeout` |
| `No results` | Verify URLs are valid and accessible |
| `Invalid marketplace` | Check marketplace value matches supported list exactly |
