# Actor Development Plugin

Develop, debug, and deploy Apify Actors with AI assistance. This plugin provides comprehensive guidance for building serverless web scraping and automation programs on the Apify platform.

## What This Plugin Does

This plugin helps you create and maintain Apify Actors - serverless programs that run in the cloud for web scraping, automation, and data processing. Claude Code will guide you through best practices, schema configuration, debugging, and deployment.

## Real-World Examples

### Creating a New Web Scraper

**E-commerce developer building a product scraper:**
> "Create an Apify Actor that scrapes product listings from an e-commerce site"

Claude will scaffold the Actor with proper input schema, crawler configuration, data validation, and output formatting.

### Debugging Actor Issues

**Developer troubleshooting a failing Actor:**
> "My Actor is timing out on large crawls. Help me optimize it."

Claude will analyze your code, suggest concurrency settings, recommend switching from browser to HTTP crawling, and implement proper retry strategies.

### Schema Configuration

**Developer setting up Actor inputs:**
> "Add input fields for proxy configuration and max results limit"

Claude will update your `.actor/input_schema.json` with proper validation, defaults, and Console UI configuration.

### Output Schema Setup

**Developer configuring result display:**
> "Set up the dataset schema to display product images, prices, and links in a table"

Claude will create the dataset schema with proper field transformations and display formatting for the Apify Console.

### Actor Deployment

**Developer ready to publish:**
> "Deploy this Actor to Apify platform"

Claude will validate your configuration, run final checks, and deploy using `apify push`.

### Migration and Upgrades

**Developer updating legacy code:**
> "Migrate this Actor from Crawlee v2 to v3"

Claude will identify deprecated options, update API calls, and ensure compatibility with the latest SDK version.

## How to Use

Just ask Claude naturally:

- "Create a new Actor to scrape [website]"
- "Add input field for [parameter]"
- "Fix the error in my Actor code"
- "Optimize this crawler for better performance"
- "Set up the output schema for [data structure]"
- "Deploy my Actor to Apify"

Claude will:
1. Understand your Actor development needs
2. Apply Apify best practices and conventions
3. Generate or modify code with proper validation
4. Configure schemas for input/output
5. Help debug issues and optimize performance

## Key Features

### Best Practices Enforcement

- Automatic selection of optimal crawler type (Cheerio vs Playwright)
- Proper concurrency and rate limiting settings
- Secure logging with sensitive data censoring
- Input validation and error handling

### Schema Management

- Input schema configuration with proper validation
- Output schema setup with display formatting
- Dataset schema for structured data presentation
- Key-value store schema for file organization

### Performance Optimization

- Crawler type selection (HTTP vs Browser)
- Concurrency tuning
- Request retry strategies
- Resource management

### Security and Safety

- Automatic use of `apify/log` package for sensitive data censoring
- Proxy configuration guidance
- Terms of Service compliance checks
- Standby mode readiness probe implementation

## Supported Actor Features

| Feature | Purpose |
|---------|---------|
| Input Schema | Define Actor parameters and Console UI |
| Output Schema | Configure result access and templates |
| Dataset Schema | Structure and display scraped data |
| Key-Value Store | Organize files and configuration |
| Standby Mode | Real-time API-like Actor behavior |
| Proxy Configuration | Anti-bot protection and geo-targeting |
| Crawlee Routers | Complex multi-page crawling logic |

## Prerequisites

- Node.js or Python environment
- Apify CLI installed (`npm install -g apify-cli`)
- Apify account (free tier available)
- Basic understanding of web scraping concepts

## Quick Start

1. **Initialize a new Actor:**
   ```bash
   apify create my-actor
   ```

2. **Ask Claude for help:**
   > "Help me set up this Actor to scrape product prices"

3. **Test locally:**
   ```bash
   apify run
   ```

4. **Deploy to Apify:**
   ```bash
   apify login
   apify push
   ```

## Common Development Tasks

### Setting Up Input Fields

Claude will help you define input parameters in `.actor/input_schema.json` with:
- Proper type definitions
- Default values
- Validation rules
- Console UI editors

### Configuring Crawlers

Get guidance on:
- CheerioCrawler for static HTML (fast)
- PlaywrightCrawler for JavaScript-heavy sites
- Request routing and URL patterns
- Concurrency and rate limiting

### Data Handling

Learn to:
- Push data to datasets
- Store files in key-value stores
- Validate and clean scraped data
- Handle pagination and infinite scroll

### Error Handling

Implement:
- Request retry strategies
- Input validation
- Graceful failure handling
- Proper error logging

## Resources

- [Apify Documentation](https://docs.apify.com)
- [Crawlee Documentation](https://crawlee.dev)
- [Actor Specification](https://raw.githubusercontent.com/apify/actor-whitepaper/refs/heads/master/README.md)
- [Apify SDK Reference](https://docs.apify.com/sdk/js)

## Plugin Structure

```
plugins/actor-development/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── skills/
│   └── actor-dev/
│       └── SKILL.md         # Comprehensive Actor development guide
└── README.md                # This file
```

## Support

For issues or questions:
- GitHub: https://github.com/apify/claude-code-plugins
- Email: support@apify.com
- Apify Console: https://console.apify.com

## License

Apache-2.0
