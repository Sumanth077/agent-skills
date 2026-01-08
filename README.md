# Apify Claude Code plugin marketplace

Official Apify plugin marketplace for Claude Code - enabling web scraping, data extraction, and automation directly from Claude's CLI.

## Installation

### Add the marketplace

```bash
/plugin marketplace add https://github.com/apify/claude-code-plugins
```

### Install a plugin

```bash
/plugin install lead-generation@apify
```

### Verify installation

Run `/skills` to check if the plugin was installed successfully. If you don't see the skill listed, try restarting Claude Code.

## Prerequisites

1. **Apify Account**: Sign up at [apify.com](https://apify.com)
2. **API Token**: Get your token from [Apify Console > Integrations](https://console.apify.com/account/integrations)
3. **Set Environment Variable**: Add to your `.env` file:
   ```
   APIFY_TOKEN=your_token_here
   ```

## Available plugins

### lead-generation

Generate and enrich B2B/B2C leads using Apify scrapers across Google Maps, social media, and websites.

#### Skills

The `lead-generation` skill allows Claude to automatically invoke lead generation when you ask for prospects, leads, or business contacts.

**Example prompts:**
- "Find me coffee shops in Seattle"
- "Get contact info from these websites"
- "Build a lead list for fitness influencers"


## Supported Apify Actors

| Platform | Actor | Use Case |
|----------|-------|----------|
| **Google** | Google Maps Scraper | Find local businesses |
| | Google Maps Email Extractor | Direct email extraction |
| | Google Search Scraper | Broad lead discovery |
| **Instagram** | Instagram Profile Scraper | Influencer discovery |
| | Instagram Scraper | Posts, comments, hashtags |
| | Instagram Search Scraper | Places, users, hashtags |
| | Instagram Tagged Scraper | Mentions tracking |
| **TikTok** | TikTok Scraper | Videos, hashtags, profiles |
| | Free TikTok Scraper | Free alternative |
| | TikTok Profile Scraper | Creator metrics |
| | TikTok User Search | Find users by keywords |
| | TikTok Followers Scraper | Audience analysis |
| **Facebook** | Facebook Pages Scraper | Business page data |
| | Facebook Page Contacts | Contact extraction |
| | Facebook Groups Scraper | Community prospecting |
| | Facebook Events Scraper | Event networking |
| **YouTube** | YouTube Scraper | Creator partnerships |
| **Websites** | Contact Info Scraper | Emails & socials from URLs |

## Output format

All commands export data to CSV format for easy import into CRMs, spreadsheets, or other tools.

## Pricing

Apify Actors use pay-per-result pricing. Check individual Actor pricing on [apify.com](https://apify.com).

## Future plugins

### Outcome-based
- `brand-monitoring` - Review tracking, sentiment analysis
- `competitor-intelligence` - Benchmarking, feature comparison
- `influencer-discovery` - Find and vet influencers
- `trend-analysis` - Hashtag tracking, viral content

### Platform-based
- `google-intelligence` - Maps, Search, Trends, Booking
- `instagram-intelligence` - Profiles, Posts, Reels, Hashtags
- `facebook-intelligence` - Pages, Posts, Groups, Ads
- `tiktok-intelligence` - Profiles, Videos, Hashtags, Sounds
- `youtube-intelligence` - Channels, Videos, Shorts, Comments

## Contributing

1. Fork this repository
2. Create your plugin in `plugins/your-plugin-name/`
3. Add entry to `.claude-plugin/marketplace.json`
4. Submit a pull request


## Support

- [Apify Documentation](https://docs.apify.com)
- [Apify Discord](https://discord.gg/jyEM2PRvMU)
